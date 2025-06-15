# hypergrpc

A hypermodern python package starter template to start with a Python gRPC server<=>client w/ Protobufs.

## Generate Protos

```bash
uv run python -m grpc_tools.protoc -I ./protos --python_out=src --grpclib_python_out=src --pyi_out=src protos/ping.proto   
```