FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

# Temporarily do wagtail installation from local package, until 2.0 is out
COPY packages/wagtail-2.0a0-py3-none-any.whl /usr/src/packages/wagtail-2.0a0-py3-none-any.whl
RUN pip install /usr/src/packages/wagtail-2.0a0-py3-none-any.whl

# Different src directory for pip to prevent 'pip install -e' packages to be installed in /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt --src /usr/local/src

COPY . /usr/src/app

CMD ["/usr/src/app/docker/cmd-webserver.sh"]

EXPOSE 8000
