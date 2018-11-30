from __future__ import print_function

import grpc

import services_pb2_grpc
import services_pb2


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = services_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(services_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()