FROM python:3

WORKDIR /usr/src/app


RUN pip install --no-cache-dir -r -y requirements.txt


CMD [ "python", "bot.py" ]
