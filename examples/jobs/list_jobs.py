"""Example script for fetching jobs from the Jobs API."""

import logging
import os
import sys

import yaml

from tamr.api.v1beta1.jobs_pb2 import JobState
from tamr_sdk.api_client import TamrApiClient

PAGE_SIZE = 25
NUM_PAGES_TO_CHECK = 10
STATUS_STRS = ["PENDING", "RUNNING"]
STATUSES = [JobState.Value(s) for s in STATUS_STRS]

if __name__ == "__main__":
    # Set up logging
    logger = logging.getLogger()
    logger.setLevel("INFO")
    logger.addHandler(logging.StreamHandler(sys.stdout))

    # Read Tamr Cloud configurations from file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(dir_path, "..", "config.yaml")
    with open(config_path) as stream:
        config = yaml.safe_load(stream)

    # Initialize Tamr Cloud client
    tamr_client = TamrApiClient(
        config["tamr_cloud_host"],
        [("x-api-key", config["tamr_api_key"])],
        grpc_stack_trace=True,
    )
    jobs_client = tamr_client.jobs()
    logger.info("Client initialization complete.")

    # Find most recent job with status in `STATUSES`
    next_page_token = None

    for p in range(NUM_PAGES_TO_CHECK):
        list_jobs_resp = jobs_client.list_jobs(
            page_token=next_page_token, page_size=PAGE_SIZE
        )

        matches = [j.status.state in STATUSES for j in list_jobs_resp.jobs]

        if any(matches):
            first_matching_job = list_jobs_resp.jobs[matches.index(True)]
            logger.info(
                f"Most recent job with status in {STATUS_STRS} is {first_matching_job}."
            )
            break

        next_page_token = list_jobs_resp.next_page_token
        if p == NUM_PAGES_TO_CHECK - 1:
            logger.info(
                f"No job with status in {STATUS_STRS} found in recent "
                + f"{NUM_PAGES_TO_CHECK * PAGE_SIZE} jobs."
            )
