FROM python:3.6.5-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ADD app.tar /app

EXPOSE 8088

CMD ["python", "app.py"]
