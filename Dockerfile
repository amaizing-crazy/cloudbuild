FROM python:3-alpine
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["main.py"]