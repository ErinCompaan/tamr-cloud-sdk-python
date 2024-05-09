from google.api import annotations_pb2 as _annotations_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from tamr.api.v1beta1 import errors_pb2 as _errors_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JobState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATE_UNSPECIFIED: _ClassVar[JobState]
    PENDING: _ClassVar[JobState]
    RUNNING: _ClassVar[JobState]
    STOPPING: _ClassVar[JobState]
    DONE: _ClassVar[JobState]
STATE_UNSPECIFIED: JobState
PENDING: JobState
RUNNING: JobState
STOPPING: JobState
DONE: JobState

class CreateJobRequest(_message.Message):
    __slots__ = ("job",)
    JOB_FIELD_NUMBER: _ClassVar[int]
    job: Job
    def __init__(self, job: _Optional[_Union[Job, _Mapping]] = ...) -> None: ...

class GetJobRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class Job(_message.Message):
    __slots__ = ("job_id", "configuration", "status", "status_history")
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_HISTORY_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    configuration: JobConfiguration
    status: JobStatus
    status_history: _containers.RepeatedCompositeFieldContainer[JobStatus]
    def __init__(self, job_id: _Optional[str] = ..., configuration: _Optional[_Union[JobConfiguration, _Mapping]] = ..., status: _Optional[_Union[JobStatus, _Mapping]] = ..., status_history: _Optional[_Iterable[_Union[JobStatus, _Mapping]]] = ...) -> None: ...

class JobConfiguration(_message.Message):
    __slots__ = ("load", "update", "publish")
    class LoadJob(_message.Message):
        __slots__ = ("source_id",)
        SOURCE_ID_FIELD_NUMBER: _ClassVar[int]
        source_id: str
        def __init__(self, source_id: _Optional[str] = ...) -> None: ...
    class PublishJob(_message.Message):
        __slots__ = ("destination_id",)
        DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
        destination_id: str
        def __init__(self, destination_id: _Optional[str] = ...) -> None: ...
    class UpdateJob(_message.Message):
        __slots__ = ("data_product_id",)
        DATA_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        data_product_id: str
        def __init__(self, data_product_id: _Optional[str] = ...) -> None: ...
    LOAD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    PUBLISH_FIELD_NUMBER: _ClassVar[int]
    load: JobConfiguration.LoadJob
    update: JobConfiguration.UpdateJob
    publish: JobConfiguration.PublishJob
    def __init__(self, load: _Optional[_Union[JobConfiguration.LoadJob, _Mapping]] = ..., update: _Optional[_Union[JobConfiguration.UpdateJob, _Mapping]] = ..., publish: _Optional[_Union[JobConfiguration.PublishJob, _Mapping]] = ...) -> None: ...

class JobStatus(_message.Message):
    __slots__ = ("state", "state_start_time", "error")
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_START_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    state: JobState
    state_start_time: _timestamp_pb2.Timestamp
    error: _errors_pb2.Error
    def __init__(self, state: _Optional[_Union[JobState, str]] = ..., state_start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., error: _Optional[_Union[_errors_pb2.Error, _Mapping]] = ...) -> None: ...

class ListJobsRequest(_message.Message):
    __slots__ = ("page_size", "page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListJobsResponse(_message.Message):
    __slots__ = ("jobs", "next_page_token")
    JOBS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    jobs: _containers.RepeatedCompositeFieldContainer[Job]
    next_page_token: str
    def __init__(self, jobs: _Optional[_Iterable[_Union[Job, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class StopJobRequest(_message.Message):
    __slots__ = ("job_id",)
    JOB_ID_FIELD_NUMBER: _ClassVar[int]
    job_id: str
    def __init__(self, job_id: _Optional[str] = ...) -> None: ...

class StopJobResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
