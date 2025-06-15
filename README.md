# hypergrpc

A hypermodern python package starter template to start with a Python gRPC server<=>client w/ Protobufs.

## Generate Protos

```bash
uv run python -m grpc_tools.protoc -I ./protos --python_out=src --grpclib_python_out=src --pyi_out=src protos/ping.proto   
```

## Examples

There are two examples - the server and client implementations of the ping service. They can be run as:

```bash
uv run python ./examples/server.py
```

Then you can simulate a ping to the service by using:

```bash
uv run python ./examples/client.py
```