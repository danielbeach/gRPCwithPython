import grpc
import example_pb2_grpc
import example_pb2


def run():
  channel = grpc.insecure_channel('localhost:50051')
  dune = example_pb2_grpc.DuneStub(channel)
  response = dune.isMuadDib(example_pb2.DidYouReally(message='Daniel Beach'))
  print("Greeter client received: " + response.message)


if __name__ == '__main__':
    run()
