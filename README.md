# vn
vn is terminal tool to help people learn English

## Install

### Docker

```bash
git clone https://github.com/togatoga/vn
cd vn
docker build -t vn .

alias vnt="docker run -it --rm vn python vn.py translate $*"

```
