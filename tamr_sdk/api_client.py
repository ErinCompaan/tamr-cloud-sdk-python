from tamr_sdk.jobs.jobs_client import JobsClient

class TamrApiClient:
    def __init__(self, host, metadata):
        self.host = host
        self.metadata = metadata

    def jobs(self):
        return JobsClient(self.host, self.metadata)
