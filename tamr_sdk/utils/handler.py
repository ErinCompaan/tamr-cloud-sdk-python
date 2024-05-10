from typing import Callable, TypeVar

import grpc
from typing_extensions import Concatenate, ParamSpec

SelfT = TypeVar("SelfT")
ArgT = ParamSpec("ArgT")
ReturnT = TypeVar("ReturnT")


def exception_handler(
    func: Callable[Concatenate[SelfT, ArgT], ReturnT]
) -> Callable[Concatenate[SelfT, ArgT], ReturnT]:
    def handle_grpc_status_codes(
        _self: SelfT, *args: ArgT.args, **kwargs: ArgT.kwargs
    ) -> ReturnT:
        grpc_stack_trace = _self.grpc_stack_trace
        try:
            return func(_self, *args, **kwargs)
        except grpc._channel._InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                if not grpc_stack_trace:
                    raise ValueError(e.details()) from None
                else:
                    raise ValueError(e.details())
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                if not grpc_stack_trace:
                    raise ConnectionError(e.details()) from None
                else:
                    raise ConnectionError(e.details())
            elif e.code() == grpc.StatusCode.UNAUTHENTICATED:
                if not grpc_stack_trace:
                    raise ConnectionRefusedError("Error connecting to client. Authentication is not valid") from None
                else:
                    raise ConnectionRefusedError("Error connecting to client. Authentication is not valid")
            else:
                raise e

    return handle_grpc_status_codes