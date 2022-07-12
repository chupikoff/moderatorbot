FROM python:3.8
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY bot.py /opt/app
COPY requirements.txt /opt/app/
COPY settings.py /opt/app/
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "bot.py" ]