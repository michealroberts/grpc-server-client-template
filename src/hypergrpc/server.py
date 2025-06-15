# **************************************************************************************

# @package        hypergrpc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

from grpclib.reflection.service import ServerReflection
from grpclib.server import Server
from grpclib.utils import graceful_exit

from .services.ping import PingService

# **************************************************************************************


async def run_server(host: str = "0.0.0.0", port: int = 50051) -> None:
    services = ServerReflection.extend([PingService()])
    server = Server(services)
    with graceful_exit([server]):
        await server.start(host=host, port=port)
        await server.wait_closed()


# **************************************************************************************
