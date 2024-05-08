from typing import List, Tuple
from tamr_sdk.jobs.jobs_client import JobsClient


class TamrApiClient:
    def __init__(self, host: str, metadata: List[Tuple[str, str]]) -> None:
        self.host = host
        self.metadata = metadata

    def jobs(self) -> JobsClient:
        return JobsClient(self.host, self.metadata)
