FROM python:3.10.6-slim-buster

WORKDIR /app

COPY ./requirements.txt /app
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["python3", "todo_api/manage.py", "runserver", "0.0.0.0:8000"]