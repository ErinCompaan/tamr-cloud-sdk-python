import grpc

def exception_handler(func):
    def handle_grpc_status_codes(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except grpc._channel._InactiveRpcError as e:
            if e.code() == grpc.StatusCode.NOT_FOUND:
                raise ValueError(e.details())
            elif e.code() == grpc.StatusCode.UNAVAILABLE:
                raise ConnectionError(e.details())
            elif e.code() == grpc.StatusCode.UNAUTHENTICATED:
                raise ConnectionRefusedError("Error connecting to client. Authentication is not valid")
            else:
                raise e

    return handle_grpc_status_codes