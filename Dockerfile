FROM python
MAINTAINER evanfpearson
WORKDIR /game

COPY requirements.txt requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]


COPY src /game/src
WORKDIR src

CMD ["python3", "main.py"]
