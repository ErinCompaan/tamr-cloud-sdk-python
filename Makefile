# Python path retrieval for lint/format command 
VENV           = .sdk_env
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
# If virtualenv exists, use it. If not, find python using PATH
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))

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
		--python_out=. \
		--pyi_out=.
	protoc proto/protoc-gen-openapiv2/options/*.proto \
		-I='proto' \
		-I='build/dependencies/googleapis' \
		--grpc_python_out=. \
		--python_out=. \
		--pyi_out=.

.sdk_env_touchfile: requirements.txt requirements_dev.txt
	$(PYTHON) -m pip install --upgrade pip && \
	$(PYTHON) -m pip install -r requirements.txt && \
	$(PYTHON) -m pip install -r requirements_dev.txt
	touch .sdk_env_touchfile

pythonEnv: .sdk_env_touchfile

# Commands for isort, linting, and formatting
lintAndFormat: pythonEnv
	@if [ "$(checkOnly)" = "true" ]; then \
			$(PYTHON) -m ruff check && \
			$(PYTHON) -m ruff format --check; \
	else \
			$(PYTHON) -m ruff check --select I --fix && \
			$(PYTHON) -m ruff check && \
			$(PYTHON) -m ruff format; \
	fi

clean:
	rm -f .sdk_env_touchfile
	rm -rf build
	rm -rf tamr
	rm -rf protoc_gen_openapiv2
