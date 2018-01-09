FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 9.3.0

# Install nvm with node and npm - needed to build wagtail static assets (until 2.0 is released on pypi)
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

COPY requirements.txt /usr/src/app/
# Different src directory for pip to prevent 'pip install -e' packages to be installed in /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt --src /usr/local/src

# [1] http://docs.wagtail.io/en/latest/contributing/developing.html
RUN . $NVM_DIR/nvm.sh && cd /usr/local/src/wagtail && npm install && npm run build

COPY . /usr/src/app

CMD ["/usr/src/app/docker/cmd-webserver.sh"]

EXPOSE 8000
