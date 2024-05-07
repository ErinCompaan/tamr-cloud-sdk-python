build/dependencies/googleapis:
	mkdir -p build/dependencies
	cd build/dependencies && git clone https://github.com/googleapis/googleapis

generateProto: build/dependencies/googleapis
	protoc proto/tamr/api/**/*.proto \
		-I='proto' \
		-I='build/dependencies/googleapis' \
		-I='proto/protoc-gen-openapiv2/options' \
		--grpc_python_out=. \
		--python_out=. \
		--pyi_out=.
	protoc proto/protoc-gen-openapiv2/options/*.proto \
		-I='proto' \
		-I='build/dependencies/googleapis' \
		--grpc_python_out=. \
		--python_out=. \
		--pyi_out=.

clean:
	rm -rf build
	rm -rf tamr
	rm -rf protoc_gen_openapiv2
