# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import loadtest_pb2 as loadtest__pb2


class LoadtestWorkerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Start = channel.unary_unary(
        '/google.pubsub.loadtest.LoadtestWorker/Start',
        request_serializer=loadtest__pb2.StartRequest.SerializeToString,
        response_deserializer=loadtest__pb2.StartResponse.FromString,
        )
    self.Check = channel.unary_unary(
        '/google.pubsub.loadtest.LoadtestWorker/Check',
        request_serializer=loadtest__pb2.CheckRequest.SerializeToString,
        response_deserializer=loadtest__pb2.CheckResponse.FromString,
        )


class LoadtestWorkerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Start(self, request, context):
    """Starts a worker
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Check(self, request, context):
    """Check the status of a load test worker.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LoadtestWorkerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Start': grpc.unary_unary_rpc_method_handler(
          servicer.Start,
          request_deserializer=loadtest__pb2.StartRequest.FromString,
          response_serializer=loadtest__pb2.StartResponse.SerializeToString,
      ),
      'Check': grpc.unary_unary_rpc_method_handler(
          servicer.Check,
          request_deserializer=loadtest__pb2.CheckRequest.FromString,
          response_serializer=loadtest__pb2.CheckResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.pubsub.loadtest.LoadtestWorker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
