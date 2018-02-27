FROM python:3.6.4

# -- Install Pipenv:
RUN set -ex && pip install pipenv --upgrade

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --deploy --system

COPY . /app

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
ENV IS_AWS_ENV=true

# Run app.py when the container launches
#CMD ["python", "app.py"]

ENTRYPOINT ["python"]
CMD ["app.py"]
#CMD flask run --host=0.0.0.0 --port=5000