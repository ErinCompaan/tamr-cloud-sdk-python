PROTOC_EXISTS=$?
if [ $PROTOC_EXISTS -eq 0 ]; then
    echo "Protoc already installed"
	PROTOC_VERSION=`protoc --version`
	if [ "$PROTOC_VERSION" == "libprotoc 26.1" ]; then
		exit 0
	fi
	echo "libprotoc 26.1 required, but found: $PROTOC_VERSION"
	exit 1
fi

if [ "$(uname)" == "Darwin" ]; then
    brew install protobuf@26
elif [ `whoami` == "root" ]; then
    mkdir -p /usr/local/src/protoc
    pushd /usr/local/src/protoc
    wget https://github.com/google/protobuf/releases/download/v26.1/protoc-26.1-linux-x86_64.zip -O /usr/local/src/protoc-26.1-linux-x86_64.zip
    unzip -x ../protoc-26.1-linux-x86_64.zip
    if [ ! -e /usr/local/bin/protoc ]; then
        ln -s `pwd`/bin/protoc /usr/local/bin/protoc
    fi
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    sudo chmod a+w /usr/local/src
    mkdir -p /usr/local/src/protoc
    pushd /usr/local/src/protoc
    wget https://github.com/google/protobuf/releases/download/v26.1/protoc-26.1-linux-x86_64.zip -O /usr/local/src/protoc-26.1-linux-x86_64.zip
    unzip -x ../protoc-26.1-linux-x86_64.zip
    if [ ! -e /usr/local/bin/protoc ]; then
        sudo ln -s `pwd`/bin/protoc /usr/local/bin/protoc
    fi
    popd
fi
exit 0