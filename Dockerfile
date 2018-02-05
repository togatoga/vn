FROM python:latest

RUN pip install click crayons requests prompt_toolkit beautifulsoup4 lxml
RUN git clone https://github.com/togatoga/vn
WORKDIR "vn"
