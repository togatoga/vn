FROM python:latest

RUN pip install click crayons requests prompt_toolkit
RUN git clone https://github.com/togatoga/vn
WORKDIR "vn"
