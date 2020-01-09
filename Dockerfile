FROM python:2.7
RUN pip install flask
ADD ./app /app
WORKDIR /app
EXPOSE 80
CMD ["python2", "app.py"]
