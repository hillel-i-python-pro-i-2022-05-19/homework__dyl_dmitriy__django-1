FROM python:3.10

ENV PYTHONUNBUFFERED=1 TIMEZONE=UTC+2
RUN apt-get update

RUN mkdir -p /usr/src/app/
ARG WORKDIR=/usr/src/app/

WORKDIR ${WORKDIR}

RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install --requirement requirements.txt

COPY --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh
COPY --chmod=755 ./docker/app/start.sh /start.sh

COPY . /usr/src/app/

ARG USER=user
ARG UID=1000


RUN useradd --system ${USER} --uid=${UID}

RUN chown --recursive ${USER} ${WORKDIR}


ENTRYPOINT ["/entrypoint.sh"]
CMD ["/start.sh"]

EXPOSE 8000