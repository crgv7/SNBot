FROM python:3

RUN pip install requirements.txt

ENTRYPOINT python bot.py
