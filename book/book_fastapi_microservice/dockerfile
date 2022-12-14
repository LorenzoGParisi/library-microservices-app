FROM python:latest
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
ADD ./app /code/app
WORKDIR /code/app
CMD ["python", "main.py"]