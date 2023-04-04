FROM python:3

RUN pip isntall requirements.txt

ENTRYPOINT python bot.py
