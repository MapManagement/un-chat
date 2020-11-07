@echo off
echo Generating Python code...
python -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs\chat_message.proto
echo Successfully generated Python code!