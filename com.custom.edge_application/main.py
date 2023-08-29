import json, time, random
from opentelemetry import trace, baggage
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import Status, StatusCode
from opentelemetry.sdk.extension.aws.trace import AwsXRayIdGenerator

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")
trace.set_tracer_provider(TracerProvider(active_span_processor=BatchSpanProcessor(otlp_exporter), id_generator=AwsXRayIdGenerator()))
tracer = trace.get_tracer(__name__)

@tracer.start_as_current_span("Upload_to_s3")
def upload_to_s3(result): print(f"upload to s3 : {result}")

def main():
    while True:
        with tracer.start_as_current_span('Edge ML application') as parent:
            with tracer.start_as_current_span('Edge data processing') as span:
                print('create random number ')
                random_number = random.randint(0,5)
            with tracer.start_as_current_span('Inference') as child: 
                print(f'divide 5 by random number : {random_number}')
                try:
                    result = 5 / random_number
                except Exception as ex:
                    child.set_status(Status(StatusCode.ERROR))
                    child.record_exception(ex)
                    parent.set_status(Status(StatusCode.ERROR))
                    result, msg = 0, "ERROR"
                    print(msg)
            upload_to_s3(result)
            time.sleep(5)

if __name__ == '__main__': main()
