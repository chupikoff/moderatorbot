FROM python:3.8-slim
RUN mkdir -p /opt/app/
COPY requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
WORKDIR /opt/app
RUN rm -rf /tmp/* \
    && rm -rf /tmp/.cache/pip/*
COPY bot.py /opt/app/

COPY settings.py /opt/app/


ENTRYPOINT [ "python", "bot.py" ]