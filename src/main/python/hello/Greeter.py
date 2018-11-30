import services_pb2_grpc
import services_pb2

class Greeter(services_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return services_pb2.HelloReply(message="Hello, %s !" % request.name)
    
    def SayHelloAgain(self, request, context):
        return services_pb2.HelloReply(message='Hello again, %s!' % request.name)
