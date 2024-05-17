"""Example script for polling a job from the Jobs API."""

import time
import json
from google.protobuf.json_format import MessageToJson
from tamr_sdk.api_client import TamrApiClient
from datetime import datetime

timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"

tamr_client = TamrApiClient(
    "<host-name>", [("x-api-key", "<api-key>")], grpc_stack_trace=True
)


def calculate_runtime(start_str, stop_str):
    start = datetime.strptime(start_str, timestamp_format)
    stop = datetime.strptime(stop_str, timestamp_format)
    difference = stop - start
    hours, remainder = divmod(difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return hours, minutes, seconds


def check_for_done(job_id):
    while True:
        # Check for the string 'DONE' in the get job response
        job = tamr_client.jobs().get_job(job_id)
        state = json.loads(MessageToJson(job))["status"]["state"]
        if state == "DONE":
            stop = json.loads(MessageToJson(job))["status"]["stateStartTime"]
            start = json.loads(MessageToJson(job))["statusHistory"][-1][
                "stateStartTime"
            ]
            hours, minutes, seconds = calculate_runtime(stop, start)
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
