FROM python:3.6.5-slim

RUN pip install --trusted-host pypi.python.org -r requirements.txt

WORKDIR /app

ADD app.tar /app

EXPOSE 8088

CMD ["python", "app.py"]
