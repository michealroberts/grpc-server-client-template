# **************************************************************************************

# @package        hypergrpc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from ping_grpc import PingServiceBase, PingServiceStub
from ping_pb2 import PingRequest, PongReply

from .server import run_server
from .services.ping import PingService

# **************************************************************************************

__version__ = "0.0.0"

# **************************************************************************************

__license__ = "MIT"

# **************************************************************************************

__all__: list[str] = [
    "__license__",
    "__version__",
    "PingService",
    "PingServiceBase",
    "PingServiceStub",
    "PingRequest",
    "PongReply",
    "run_server",
]

# **************************************************************************************
