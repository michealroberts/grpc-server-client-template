# **************************************************************************************

# @package        hypergrpc
# @license        MIT License Copyright (c) 2025 Michael J. Roberts

# **************************************************************************************

import asyncio
from argparse import ArgumentParser
from typing import cast

from hypergrpc import run_server

# **************************************************************************************


async def main(host: str, port: int) -> None:
    await run_server(
        host=host,
        port=port,
    )


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
