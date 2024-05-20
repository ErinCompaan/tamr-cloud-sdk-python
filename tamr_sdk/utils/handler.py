"""Wrapper(s) for API response handling."""
from __future__ import annotations
from typing import Callable, TypeVar

import grpc
from typing_extensions import Concatenate, ParamSpec

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from tamr_sdk.api_client import TamrApiClient
    from tamr_sdk.jobs.jobs_client import JobsClient

    SelfT = TypeVar("SelfT", JobsClient, TamrApiClient)
    ArgT = ParamSpec("ArgT")
    ReturnT = TypeVar("ReturnT")


def exception_handler(
    func: Callable[Concatenate[SelfT, ArgT], ReturnT],
) -> Callable[Concatenate[SelfT, ArgT], ReturnT]:
    """Wrapper to handle gRPC exceptions.

    Args:
        func: gRPC-calling method to be wrapped

    Returns:
        input function with additional error handling

    Raises:
        ValueError: if gRPC returns not-found
        ConnectionError: if gRPC returns unavailable
        ConnectionRefusedError: if gRPC returns authentication error
    """

    def handle_grpc_status_codes(
        _self: SelfT, *args: ArgT.args, **kwargs: ArgT.kwargs
    ) -> ReturnT:
        """Wrapped function with additional error handling.

        Args:
            _self:
            args: args of the func
            kwargs: keyword args of the func

        Returns:
            same type as original func
        """
        grpc_stack_trace = _self.grpc_stack_trace
        try:
            return func(_self, *args, **kwargs)
        except grpc._channel._InactiveRpcError as e:  # type: ignore[attr-defined]
            new_err: Exception
            if e.code() == grpc.StatusCode.NOT_FOUND:
                new_err = ValueError(e.details())
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                new_err = ConnectionError(e.details())
            elif e.code() == grpc.StatusCode.UNAUTHENTICATED:
                new_err = ConnectionRefusedError(
                    "Error connecting to client. Authentication is not valid"
                )
            else:
                new_err = e

            raise new_err from (e if grpc_stack_trace else None)

    return handle_grpc_status_codes
