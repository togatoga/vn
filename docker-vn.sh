#!/bin/bash
# git clone https://github.com/togatoga/vn
# cd vn; "docker build -t vn ."

function docker-build-vn() {
	pushd
	rm -rf /tmp/vn
	git clone https://github.com/togatoga/vn /tmp/vn
	cd /tmp/vn
	git pull origin master
	docker build --no-cache=true -t vn .
	popd
}
alias vn="docker run -it --rm vn python cmd.py"
alias vni="docker run -it --rm vn python cmd.py translate --interactive"
alias vnt="docker run -it --rm vn python cmd.py translate $*"
