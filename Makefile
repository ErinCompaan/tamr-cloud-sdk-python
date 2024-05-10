build/dependencies/googleapis:
	mkdir -p build/dependencies
	cd build/dependencies && git clone https://github.com/googleapis/googleapis

installProto: build/dependencies/googleapis
	bash install_proto.sh

linkPythonGRPC: installProto
	bash link_python_grpc_plugin.sh

generateProto: linkPythonGRPC
	protoc proto/tamr/api/**/*.proto \
	    -I='proto' \
	    -I='build/dependencies/googleapis' \
	    -I='proto/protoc-gen-openapiv2/options' \
	    --grpc_python_out=. \
	    --python_out=.
	protoc proto/protoc-gen-openapiv2/options/*.proto \
    	-I='proto' \
    	-I='build/dependencies/googleapis' \
    	--grpc_python_out=. \
    	--python_out=.

clean:
	rm -rf build
	rm -rf tamr
	rm -rf protoc_gen_openapiv2
