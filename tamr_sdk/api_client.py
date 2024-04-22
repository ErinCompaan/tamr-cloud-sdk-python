from tamr_sdk.jobs.jobs_client import JobsClient

class TamrApiClient:
    def __init__(self, host):
        self.host = host

    def jobs(self):
        return JobsClient(self.host)

