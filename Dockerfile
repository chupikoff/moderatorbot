FROM python:3.8
COPY . /opt/
RUN pip3.8 install --no-cache-dir -r /opt/requirements.txt

CMD [ "python3.8", "/opt/bot.py" ]