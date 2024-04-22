import grpc

from tamr.api.v1beta1.jobs_pb2_grpc import JobsStub
from tamr.api.v1beta1 import jobs_pb2 as jobs

class JobsClient:
    def __init__(self, host):
        channel = grpc.insecure_channel(host)
        self.stub = JobsStub(channel)

    def get_job(self, job_id):
        request = jobs.GetJobRequest(jobId=job_id)
        return self.stub.GetJob(request)

    def list_jobs(self, page_size=10, page_token=None):
        request = jobs.ListJobsRequest(
            page_size=page_size,
            page_token=page_token
        )
        return self.stub.ListJobs(request)

    def stop_job(self, job_id):
        request = jobs.StopJobRequest(jobId=job_id)
        return self.stub.StopJob(request)

    def create_job(self, job_definition):
        request = jobs.CreateJobRequest(job=job_definition)
        return self.stub.CreateJob(request)
