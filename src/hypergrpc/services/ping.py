# **************************************************************************************

# @package        hypergrpc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from grpclib import GRPCError
from grpclib.const import Status
from grpclib.server import Stream

from ping_grpc import PingServiceBase
from ping_pb2 import PingRequest, PongReply

# **************************************************************************************


class PingService(PingServiceBase):
    async def Ping(self, stream: Stream[PingRequest, PongReply]) -> None:
        request = await stream.recv_message()

        if request is None:
            raise GRPCError(Status.INVALID_ARGUMENT, "PingRequest must not be null")

        message = f"{request.message}"
        await stream.send_message(PongReply(message=message))

    async def UnaryStreamPing(self, stream: Stream[PingRequest, PongReply]) -> None:
        await self.Ping(stream=stream)


# **************************************************************************************
