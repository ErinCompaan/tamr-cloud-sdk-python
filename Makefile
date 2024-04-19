build/dependencies/googleapis:
	mkdir -p build/dependencies
	cd build/dependencies && git clone https://github.com/googleapis/googleapis

generateProto: build/dependencies/googleapis
	mkdir -p build/generated/python_grpc
	mkdir -p build/generated/python
	protoc proto/tamr/api/v1beta1/*.proto \
	    -I='proto' \
	    -I='build/dependencies/googleapis' \
	    -I='protoc-gen-openapiv2/dependencies/googleapis'
	    --grpc_python_out='build/generated/python_grpc'
	    --python_out='build/generated/python'

clean:
	rm -rf build