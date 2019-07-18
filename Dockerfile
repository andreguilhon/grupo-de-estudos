FROM python:3.7-slim
MAINTAINER guilhon@pwx.cloud
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
