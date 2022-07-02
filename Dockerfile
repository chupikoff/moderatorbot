FROM python:3.8
COPY . ./opt/app
RUN pip3.8 install --no-cache-dir -r /opt/app/requirements.txt

CMD [ "python3.8", "/opt/app/bot.py" ]