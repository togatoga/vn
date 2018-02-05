FROM python:latest

RUN pip install click crayons requests prompt_toolkit beautifulsoup4 lxml nltk
RUN [ "python", "-c", "import nltk; nltk.download('wordnet')" ]
RUN git clone https://github.com/togatoga/vn
WORKDIR "vn"
