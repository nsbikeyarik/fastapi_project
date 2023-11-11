FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

EXPOSE 8080
ENTRYPOINT [ "python3", "-m", "uvicorn", "main:app" ]
CMD [ "--host", "0.0.0.0", "--port", "8080" ]