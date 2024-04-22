from tamr_sdk.api_client import TamrApiClient

tamr_client = TamrApiClient('svc-api.tamrapi.dev:443')

tamr_client.jobs().list_jobs()
