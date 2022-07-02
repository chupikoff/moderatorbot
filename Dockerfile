FROM python:3.8
COPY . ./chupikoffbot
RUN pip3.8 install --no-cache-dir -r /chupikoffbot/requirements.txt

CMD [ "python3.8", "/chupikoffbot/bot.py" ]