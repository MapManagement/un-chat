# Bidirectional Stream

## Overview
gRPC's communication is based on the HTTP/2 transport and therefore it can easily work with
long lasting **bidirectional streams** between client and server. In my specific case, I will
use this feature as an advantage and try to create those bidirectional streams. But what are
they doing and why should I even use them? A normal simplex stream would be enough too, wouldn't
it? More about it in the following chapters.

## What is it?
Besides the normal **"unary RPCs"** where the client only sends **one** request and only receives
**one** response, there are some more types of communication between them. All of them include
that either the server, the client or both stream messages, but what does "stream" mean in our
context? I simply just means, that one (or both) of the communication partners will send more
than one request/response. This so called **"sequence"** can be read by the opposite until it
is able to send own messages back. There are three possible types of streaming:
### Server Streaming
The client can only send one request and the server is able to respond with a sequence of multiple
messages.
```protobuf
rpc ChatStream(ChatMessage) returns (stream ChatMessage);
```
### Client Stream
In this case, only the client streams multiple requests while the server answers with one
message.
```protobuf
rpc ChatStream(stream ChatMessage) returns (ChatMessage);
```
### Bidirectional Stream
That is the way how my program will be configured. It allows the server **and** the client to
stream a sequence of requests/responses. It does not matter how the streaming works in the end.
For example, the client could send its request, meanwhile the server waits until  it receives
the last message and answers with a sequence of responses.
````protobuf
rpc ChatStream(stream ChatMessage) returns (stream ChatMessage);
````

## RPC Life Cycle
In this context "life cycle" is the process where a client calls a sever method. The call invokes
several more steps to do. What they are and how they are done, is explained here:
### Unary
1. client calls remote method
2. server remarks the RPC invocation and receives following data: **metadata**, **method name**,
**deadline**
3. server sends own metadata or waits for client request message (depends on implementation)
4. receiving the request message, the server now does whatever it has to do and eventually
returns its response (status details are added automatically)
5. at the end the client receives the response
### Server/Client Streaming
Similar to the unary RPC but the server sends a stream of messages when a client request has
arrived. Once the client received all messages, the call can be seen a finished.    
The other way around works the client streaming. Stream of messages coming from the client,
server responding with only one message.
### Bidirectional Streaming
The client starts the connection by invoking a method. As in unary calls, it sends its metadata,
method name and the deadline and. The client sends a sequence of messages. Now the server can also
respond with a sequence of messages. How the communication works at the end, depends on the 
application. 

## Why bidirectional?
I am using the bidirectional stream because I constantly need to send messages to the server and
back. I also need the server to start a request whenever a person wants to send a message to
another one. It makes it easier when both sides are able to send a sequence of messages since any
could always just send a new message which has to be handled then.
