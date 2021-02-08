FROM python:3.8.2-alpine3.11

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --update build-base bash libffi-dev libressl-dev musl-dev openssl-dev curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN pip install --upgrade pip
RUN pip install --upgrade pipenv setuptools wheel twine

RUN mkdir app

COPY Pipfile Pipfile.lock ./
RUN pipenv lock --dev -r > requirements.txt
RUN pip install -r requirements.txt

COPY . ./app

WORKDIR app
