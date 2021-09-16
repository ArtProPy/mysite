FROM alpine:3.13

MAINTAINER Artem Protsenko <ArtProPy@gmail.com>

ENV BRANCH main

ENV HOME /root

COPY id_ed25519 "${HOME}"

COPY id_ed25519.pub "${HOME}"

RUN echo https://mirror.yandex.ru/mirrors/alpine/v3.12/main/       > /etc/apk/repositories \
 && echo https://mirror.yandex.ru/mirrors/alpine/v3.12/community/ >> /etc/apk/repositories \
 && apk --update add \
    git \
    openssh \
    python3 \
    python3-dev \
    py3-pip \
    uwsgi\
 \
 && mkdir "${HOME}"/.ssh \
 && mv "${HOME}"/id_ed25519 "${HOME}"/.ssh \
 && mv "${HOME}"/id_ed25519.pub "${HOME}"/.ssh \
 && ssh-keyscan github.com > "${HOME}"/.ssh/known_hosts \
 \
 && git clone -b $BRANCH --depth 1 https://github.com/ArtProPy/mysite \
 && cd mysite \
 \
 && pip install -r requirements.txt\
 && apk del \
    git \
    openssh 

WORKDIR mysite/

COPY docker-entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
