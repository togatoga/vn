FROM python:latest

RUN pip install git+https://github.com/togatoga/vn.git
RUN [ "python", "-c", "import nltk; nltk.download('wordnet')" ]
