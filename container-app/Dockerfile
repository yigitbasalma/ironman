FROM alpine:3.7 as base

ENV PYTHONUNBUFFERED 1

RUN apk add --update \
	python3 \
	py3-pip

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY app/requirements.txt /requirements.txt
RUN pip3 install --install-option="--prefix=/install" -r /requirements.txt

FROM base

RUN pip3 install gunicorn

COPY --from=builder /install/lib/python3.6/site-packages /usr/lib/python3.6/site-packages
COPY app /app

WORKDIR /app

CMD ["gunicorn", "-w 4", "app:app", "-b", "0.0.0.0:3000"]