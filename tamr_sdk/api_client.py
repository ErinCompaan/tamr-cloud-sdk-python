from tamr_sdk.jobs.jobs_client import JobsClient

class TamrApiClient:
    def __init__(self, host, metadata, grpc_stack_trace=False):
        self.host = host
        self.metadata = metadata
        self.grpc_stack_trace = grpc_stack_trace

    def jobs(self):
        return JobsClient(self.host, self.metadata, self.grpc_stack_trace)
