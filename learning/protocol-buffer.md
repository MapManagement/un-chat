# Protocol Buffers
## Summary
Protocol Buffers (or protobufs) is a format like JSON or XML but simpler:  
example.proto  
There is also an own language for this format:  
proto2/proto3 ([docs](https://developers.google.com/protocol-buffers/docs/proto))
## Messages
When requesting data from a server you normally specify the request with a **message type**.
A message type can include multiple **fields** which contain the **name** and the **data type**.
Defining a so called **unique number** for each field are for identification purposes.
```
message ExampleRequest {
    string userName = 1;
    string mailAddress = 2;
    int32 age = 3;
}
```
There are also **field rules**:
- **required** means, that a message need one and not more of this filed
- **repeated** means, that this field can be repeated as often as necessary
- **optional** means, that a message can have either one or none of this field
```
message ExampleRequest {
    required string userName = 1;
    repeated string friend = 2;
    optional int32 age = 3;
}
```
Of course, you can define multiple message within one .proto file.
```
message Book {
    required string title = 1;
    repeated string author = 2;
    optional int32 pages = 3;
}

message Movie {
    required string title = 1;
    optional string directorName = 2;
}
```
All available "Scalar Value Types" can be found [here](https://developers.google.com/protocol-buffers/docs/proto3#scalar).

## Services
## Compiler / Dependencies
Since gRPC is only working with ``.proto`` files, you need to install a specific compiler.
That is why I link you the [Protocol Buffer Compiler Installation](https://grpc.io/docs/protoc-installation/) from the
official documentation. Everything important is explained extensively.
Also, you should not forget to install the proper libraries. Since I will use Python, I need to install following ones:
```
pip install grpcio
pip install grpcio-tools
```

