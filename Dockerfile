
FROM python:3.12

WORKDIR /app

ADD A4.py /app/

CMD ["python", "A4.py"]

