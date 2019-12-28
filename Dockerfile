FROM python:3.8.1-alpine3.11

RUN apk add --update build-base bash && pip install pipenv

RUN mkdir app

COPY Pipfile Pipfile.lock ./
RUN pipenv lock --dev -r > requirements.txt
RUN pip install -r requirements.txt

COPY . ./app

WORKDIR app
