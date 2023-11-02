## AWS IoT Greengrass - Observability at the Edge

This repository contains custom Greengrass component recipes and a sample application for monitoring and observability of edge applications using AWS IoT Greengrass and AWS Distro for OpenTelemetry (ADOT).

## Structure

This repository consists of two AWS IoT Greengrass Development Kit Command-Line Interface (GDK CLI) projects:

- `com.custom.aws_otel_collector`: Contains the AWS Distro for OpenTelemetry (ADOT) Collector component.
- `com.custom.edge_application`: Represents the custom application logic running on the edge.

For more information on GDK CLI, please refer to the [AWS IoT Greengrass Development Kit Command-Line Interface](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-development-kit-cli.html).

## Reference

For a detailed walkthrough on how to use the components and samples in this repository, please refer to the [Monitor edge application performance using AWS IoT Greengrass and AWS Distro for OpenTelemetry](https://aws.amazon.com/blogs/iot/monitor-edge-application-performance-using-aws-iot-greengrass-and-aws-distro-for-opentelemetry/) blog post.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

