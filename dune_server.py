import example_pb2_grpc
import example_pb2
import random
import grpc
from concurrent import futures


class Dune(example_pb2_grpc.DuneServicer):
    def __init__(self):
        self.choices = ["yes", "no"]

    def isMuadDib(self, request, context):
        response = random.choice(self.choices).upper()
        name = request.message
        return example_pb2.DidYouReally(message=f"Hello minion, You ask me if this {name} is the Muad'dib .... {response}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    example_pb2_grpc.add_DuneServicer_to_server(Dune(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()