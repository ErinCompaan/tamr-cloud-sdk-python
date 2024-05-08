from tamr_sdk.api_client import TamrApiClient
import time

start = time.time()
tamr_client = TamrApiClient("<host-name>", [("x-api-key", "<api-key>")])
one = time.time()


jobs = tamr_client.jobs()
two = time.time()

response = jobs.list_jobs()
three = time.time()

response = jobs.get_job(job_id="<job-id>")
four = time.time()

print(response)
print(
    f"APIClient took {one -start}; JobsClient took {two-one} and api call took {three-two} and second is {four-three}"
)
