FROM python
MAINTAINER evanfpearson
WORKDIR /game
RUN ["pip", "install", "flask"]
COPY src /game/src
WORKDIR src
CMD ["python3", "main.py"]
