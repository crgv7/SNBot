FROM windows:latest

RUN pip isntall requirements.txt

ENTRYPOINT python bot.py
