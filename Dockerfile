FROM python:3.8.9-alpine3.13

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --update build-base bash libffi-dev libressl-dev musl-dev openssl-dev curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN pip install --upgrade pip
RUN pip install --upgrade pipenv setuptools wheel twine

RUN mkdir app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --dev --system

COPY . ./app

WORKDIR app
