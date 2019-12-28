FROM python:3.8.1-alpine3.11

RUN apk add --update build-base bash libffi-dev openssl-dev && pip install pipenv setuptools twine

RUN mkdir app

COPY Pipfile Pipfile.lock ./
RUN pipenv lock --dev -r > requirements.txt
RUN pip install -r requirements.txt

COPY . ./app

WORKDIR app
