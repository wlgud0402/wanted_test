FROM python:3.7

WORKDIR /app
RUN apt -y update
RUN apt -y install sqlite3

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY .  ./

EXPOSE 8000

CMD ["python", "./app.py"]
