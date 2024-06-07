"""Example script for polling a job from the Jobs API."""

import datetime
import logging
import os
import sys
import time

import yaml

from tamr.api.v1beta1.jobs_pb2 import Job, JobState
from tamr_sdk.api_client import TamrApiClient
from tamr_sdk.jobs.jobs_client import JobsClient

JOB_ID = "job_****************"


def calculate_runtime(job: Job) -> datetime.timedelta:
    """Calculates runtime for a job.

    Assumes current status of job is "DONE". If job is not done, returns the
    duration between start of job and beginning of job's current status.

    Args:
        job: Job object

    Returns:
        time delta object representing job duration
    """
    stop = job.status.state_start_time
    start = job.status_history[-1].state_start_time
    diff = datetime.timedelta(
        seconds=stop.seconds + stop.nanos * 1e-9 - start.seconds - start.nanos * 1e-9
    )
    return diff


def poll_job(
    *,
    jobs_client: JobsClient,
    job_id: str,
    logger: logging.Logger,
    polling_interval_sec: int = 5,
) -> None:
    """Poll job and return runtime when finished.

    Args:
        jobs_client: Client instance associated with Tamr Cloud jobs service
        job_id: job_id string (e.g. 'job_*********')
        logger: logging instance
        polling_interval_sec: how frequently to re-check job status
    """
    while True:
        # Check job status
        job = jobs_client.get_job(job_id)
        state = job.status.state
        # Print info if complete
        if state == JobState.DONE:
            runtime = calculate_runtime(job)
            logger.info(f"Job '{job_id}' finished in {runtime}.")
            if job.status.error.message:
                logger.warning(
                    f"Job '{job_id}' raised error: {job.status.error.message}."
                )
            break

        # Wait before checking again
        time.sleep(polling_interval_sec)


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

    # Initialize Tamr Cloud jobs client
    tamr_client = TamrApiClient(
        config["tamr_cloud_host"],
        [("x-api-key", config["tamr_api_key"])],
        grpc_stack_trace=True,
    )
    jobs_client = tamr_client.jobs()
    logger.info("Client initialization complete.")

    poll_job(jobs_client=jobs_client, job_id=JOB_ID, logger=logger)
