"""Example script for fetching jobs from the Jobs API."""

import time

from tamr_sdk.api_client import TamrApiClient

start = time.time()
tamr_client = TamrApiClient(
    "<host-name>", [("x-api-key", "<api-key>")], grpc_stack_trace=True
)
one = time.time()


jobs = tamr_client.jobs()
two = time.time()

list_jobs_resp = jobs.list_jobs()
three = time.time()

get_job_resp = jobs.get_job(job_id="<job-id>")
four = time.time()

print(get_job_resp)
print(
    f"APIClient took {one -start}; JobsClient took {two-one} and api call took {three-two} and second is {four-three}"
)
