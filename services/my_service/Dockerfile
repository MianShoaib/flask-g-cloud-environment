FROM python:3.8.9

ENV PYTHONUNBUFFERED true
ENV PYTHONAPP /app

WORKDIR /app/services/my_service

RUN pip install -r requirements.txt

COPY ./../lib/src /src

CMD exec gunicorn --bind :PORT --workers 1 --threads 8 --timeout 0 'src.app:create_app()'