FROM python:3
MAINTAINER Colin Newell <colin.newell@gmail.com>

RUN groupadd -r cookies && useradd -r -d /home/cookies -g cookies cookies
COPY requirements.txt /opt/cookies/
RUN pip install -r /opt/cookies/requirements.txt
COPY *.py templates/ /opt/cookies/
COPY *.py /opt/cookies/
COPY templates /opt/cookies/templates
WORKDIR /opt/cookies/
COPY entrypoint.sh /entrypoint.sh
USER cookies
CMD /entrypoint.sh

