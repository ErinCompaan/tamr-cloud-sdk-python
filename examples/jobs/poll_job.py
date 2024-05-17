"""Example script for polling a job from the Jobs API."""

import json
import time
from datetime import datetime

from google.protobuf.json_format import MessageToJson

from tamr_sdk.api_client import TamrApiClient

timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"

tamr_client = TamrApiClient(
    "<host-name>", [("x-api-key", "<api-key>")], grpc_stack_trace=True
)


def calculate_runtime(job_id):
    """Calculates runtime (hours, minutes, seconds) for a job.

    Args:
        job_id: job_id string (e.g. 'job_*********')
    """
    job = json.loads(MessageToJson(tamr_client.jobs().get_job(job_id)))
    stop = job["status"]["stateStartTime"]
    start = job["statusHistory"][-1]["stateStartTime"]
    start = datetime.strptime(start, timestamp_format)
    stop = datetime.strptime(stop, timestamp_format)
    difference = stop - start
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return hours, minutes, seconds


def check_for_done(job_id):
    """Polls job and returns runtime when finished, or returns status if the job is not running, pending, or done.

    Args:
        job_id: job_id string (e.g. 'job_*********')
    """
    while True:
        # Check for the string 'DONE' in the get job response
        job = json.loads(MessageToJson(tamr_client.jobs().get_job(job_id)))
        state = job["status"]["state"]
        if state == "DONE":
            hours, minutes, seconds = calculate_runtime(job_id)
            print(
                f"'{job_id}' finished in {hours} hours, {minutes} minutes, {seconds} seconds"
            )
            break
        if state not in ["DONE", "RUNNING", "PENDING"]:
            print(f"'{job_id}' is {state}")
            break

        # Wait for 5 seconds before checking again
        time.sleep(5)


job_id = "<job-id>"
check_for_done(job_id)
