"""gRPC Client for Jobs API."""

from typing import List, Optional, Tuple

import grpc

from tamr.api.v1beta1 import jobs_pb2 as jobs
from tamr.api.v1beta1.jobs_pb2_grpc import JobsStub
from tamr_sdk.utils.handler import exception_handler


class JobsClient:
    """gRPC client for the Jobs API."""

    def __init__(
        self, host: str, metadata: List[Tuple[str, str]], grpc_stack_trace: bool = False
    ):
        """Initialize the Jobs client.

        Args:
            host: host address for the client
            metadata: additional configuration for the client
            grpc_stack_trace: whether to log full gRPC stack trace on error
        """
        credentials: grpc.ChannelCredentials = grpc.ssl_channel_credentials()
        channel: grpc.Channel = grpc.secure_channel(host, credentials)
        self.metadata = metadata
        self.stub = JobsStub(channel)
        self.grpc_stack_trace: bool = grpc_stack_trace

    @exception_handler
    def get_job(self, job_id: str) -> jobs.Job:
        """Get a specific job by ID.

        Args:
            job_id: the ID of the Job to be fetched

        Returns:
            job information
        """
        request = jobs.GetJobRequest(job_id=job_id)
        j: jobs.Job = self.stub.GetJob(request, metadata=self.metadata)
        return j

    @exception_handler
    def list_jobs(
        self, page_size: int = 10, page_token: Optional[str] = None
    ) -> jobs.ListJobsResponse:
        """Get a list of all jobs from the client.

        Args:
            page_size: the number of jobs to return
            page_token: token indicating which page to retrieve

        Returns:
            list of job information
        """
        request = jobs.ListJobsRequest(page_size=page_size, page_token=page_token)
        r: jobs.ListJobsResponse = self.stub.ListJobs(request, metadata=self.metadata)
        return r

    @exception_handler
    def stop_job(self, job_id: str) -> jobs.StopJobResponse:
        """Send a request to stop a job.

        Args:
            job_id: the ID of the job to be stopped.

        Returns:
            result of request to stop job
        """
        request = jobs.StopJobRequest(job_id=job_id)
        r: jobs.StopJobResponse = self.stub.StopJob(request, metadata=self.metadata)
        return r

    @exception_handler
    def create_job(self, job_definition: jobs.Job) -> jobs.Job:
        """Send a request to start a job.

        Args:
            job_definition: information about what job to start.

        Returns:
            result of request to start a job
        """
        request = jobs.CreateJobRequest(job=job_definition)
        r: jobs.Job = self.stub.CreateJob(request, metadata=self.metadata)
        return r
