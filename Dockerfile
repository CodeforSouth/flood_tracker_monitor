FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./app/ /app/
RUN adduser --disabled-login myuser
USER myuser
CMD gunicorn -b 0.0.0.0:$PORT "iot:create_app()"