googleapis:
	git clone https://github.com/googleapis/googleapis

gen: googleapis
	protoc proto/tamr/api/v1beta1/*.proto -I='proto' -I='googleapis' --grpc_python_out='grpc/python_grpc' --python_out='grpc/python'
	rm -rf googleapis