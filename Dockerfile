FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD python3 dictionary2.0.py
