"""gRPC client for Tamr Cloud."""

from tamr_sdk.jobs.jobs_client import JobsClient


class TamrApiClient:
    """gRPC client for Tamr Cloud."""

    def __init__(self, host: str, metadata, grpc_stack_trace=False):
        """Initialize client.

        Args:
            host: the Tamr Cloud host address
            metadata: additional information to configure the client
            grpc_stack_trace: whether to log full gRPC stack trace on errors
        """
        self.host = host
        self.metadata = metadata
        self.grpc_stack_trace = grpc_stack_trace

    def jobs(self):
        """Get a client connected to the Jobs API.

        Returns:
            a JobsClient object
        """
        return JobsClient(self.host, self.metadata, self.grpc_stack_trace)
