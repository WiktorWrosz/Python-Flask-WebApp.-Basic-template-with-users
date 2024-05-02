FROM python:3.10

# Install PostgreSQL client libraries
RUN apt-get update && \
    apt-get install -y libpq-dev

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python ./main.py
