# **************************************************************************************

# @package        hypergrpc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import asyncio
from argparse import ArgumentParser
from typing import cast

from grpclib.client import Channel

from hypergrpc import PingRequest, PingServiceStub

# **************************************************************************************


async def main(host: str, port: int) -> None:
    # Interact with the unary unary ping<=>pong response:
    async with Channel(
        host=host,
        port=port,
    ) as channel:
        client = PingServiceStub(channel)
        reply = await client.Ping(PingRequest(message="Ping"))
        print(reply.message)


# **************************************************************************************

if __name__ == "__main__":
    parser = ArgumentParser(description="Run the hypergrpc demo server (Ping → Pong).")

    parser.add_argument(
        "--host",
        default="localhost",
        help="Interface to bind the gRPC server on (default: %(default)s)",
    )

    parser.add_argument(
        "--port",
        type=int,
        default=50051,
        help="Port to bind the gRPC server on (default: %(default)s)",
    )

    args = parser.parse_args()

    asyncio.run(
        main(
            host=cast(str, args.host),
            port=cast(int, args.port),
        )
    )

# **************************************************************************************
