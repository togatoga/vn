FROM python:latest

RUN pip install click crayons requests
RUN git clone https://github.com/togatoga/vn
WORKDIR "vn"
