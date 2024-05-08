from typing import List, Optional, Tuple
import grpc

from google.protobuf.internal.containers import RepeatedCompositeFieldContainer

import types_jobs as types
from tamr.api.v1beta1.jobs_pb2_grpc import JobsStub
from tamr.api.v1beta1 import jobs_pb2 as jobs


class JobsClient:
    def __init__(self, host: str, metadata: List[Tuple[str, str]]) -> None:
        credentials: grpc.ChannelCredentials = grpc.ssl_channel_credentials()
        channel: grpc.Channel = grpc.secure_channel(host, credentials)
        self.metadata = metadata
        self.stub = JobsStub(channel)

    def get_job(self, job_id: str) -> types.Job:
        request = jobs.GetJobRequest(job_id=job_id)
        return self.stub.GetJob(request, metadata=self.metadata)

    def list_jobs(
        self, page_size: int = 10, page_token: Optional[str] = None
    ) -> types.ListJobsResponse:
        request = jobs.ListJobsRequest(page_size=page_size, page_token=page_token)
        return self.stub.ListJobs(request, metadata=self.metadata)

    def stop_job(self, job_id: str) -> types.StopJobResponse:
        request = jobs.StopJobRequest(job_id=job_id)
        return self.stub.StopJob(request, metadata=self.metadata)

    def create_job(
        self, job_definition: types.CreateJobRequest
    ) -> types.CreateJobResponse:
        request = jobs.CreateJobRequest(job=job_definition)
        return self.stub.CreateJob(request, metadata=self.metadata)
