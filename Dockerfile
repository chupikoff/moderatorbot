FROM python:3.8-slim
COPY word_count.db /opt/
COPY bot.py /opt/
COPY settings_testing.py /opt/
COPY requirements.txt /opt/
RUN pip3.8 install --no-cache-dir -r /opt/requirements.txt

CMD [ "python3.8", "/opt/bot.py" ]
