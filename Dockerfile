FROM pypy:3.9-bullseye
ARG PIP_INDEX=https://pypi.python.org/simple
RUN pip config set global.index-url $PIP_INDEX
WORKDIR /opt/jobaggrv/
COPY ./requirements.txt /opt/jobaggrv/requirements.txt
RUN pip install -r ./requirements.txt
COPY . /opt/jobaggrv/
WORKDIR /opt/jobaggrv/

ENTRYPOINT ["python","-m","scrapy","crawl"]
