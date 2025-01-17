"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from abc import (
    ABCMeta,
    abstractmethod,
)

from grpc import (
    Channel,
    Server,
    ServicerContext,
)

from typing import (
    Iterator,
)


from .v1_pb2 import *
class HomeControlServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    def GetAssistantRoutines(self,
        request: GetAssistantRoutinesRequest,
    ) -> Iterator[GetAssistantRoutinesResponse]: ...


class HomeControlServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def GetAssistantRoutines(self,
        request: GetAssistantRoutinesRequest,
        context: ServicerContext,
    ) -> Iterator[GetAssistantRoutinesResponse]: ...


def add_HomeControlServiceServicer_to_server(servicer: HomeControlServiceServicer, server: Server) -> None: ...

class StructuresServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    def GetHomeGraph(self,
        request: GetHomeGraphRequest,
    ) -> GetHomeGraphResponse: ...


class StructuresServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def GetHomeGraph(self,
        request: GetHomeGraphRequest,
        context: ServicerContext,
    ) -> GetHomeGraphResponse: ...


def add_StructuresServiceServicer_to_server(servicer: StructuresServiceServicer, server: Server) -> None: ...

class HomeDevicesServiceStub:
    def __init__(self, channel: Channel) -> None: ...
    def GetAssistantDeviceSettings(self,
        request: GetAssistantDeviceSettingsRequest,
    ) -> Iterator[GetAssistantDeviceSettingsResponse]: ...

    def UpdateAssistantDeviceSettings(self,
        request: UpdateAssistantDeviceSettingsRequest,
    ) -> Iterator[UpdateAssistantDeviceSettingsResponse]: ...


class HomeDevicesServiceServicer(metaclass=ABCMeta):
    @abstractmethod
    def GetAssistantDeviceSettings(self,
        request: GetAssistantDeviceSettingsRequest,
        context: ServicerContext,
    ) -> Iterator[GetAssistantDeviceSettingsResponse]: ...

    @abstractmethod
    def UpdateAssistantDeviceSettings(self,
        request: UpdateAssistantDeviceSettingsRequest,
        context: ServicerContext,
    ) -> Iterator[UpdateAssistantDeviceSettingsResponse]: ...


def add_HomeDevicesServiceServicer_to_server(servicer: HomeDevicesServiceServicer, server: Server) -> None: ...
