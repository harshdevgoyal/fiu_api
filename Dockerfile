FROM python:3.8

COPY . /app
# COPY requirements.txt /requirements.txt

WORKDIR /app

RUN apt-get update \
    && pip install -r requirements.txt

# ENV PYTHONPATH=/app

EXPOSE 8000

# ENTRYPOINT ["uvicorn"]
CMD ["uvicorn","main:app", "--host", "0.0.0.0"]


