FROM ubuntu:18.04
 
# アップデート＆必要なもの、その他もろもろをインストール
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install wget vim curl jq dnsutils build-essential make cmake gcc g++ zlib1g-dev zip unzip libffi-dev git openssl libssl-dev libbz2-dev libreadline-dev libsqlite3-dev nkf
 
# install pyenv
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="${HOME}/.pyenv"' >> ~/.bashrc
RUN echo 'if [ -d "${PYENV_ROOT}" ]; then' >> ~/.bashrc
RUN echo 'export PATH=${PYENV_ROOT}/bin:$PATH' >> ~/.bashrc
RUN echo 'eval "$(pyenv init -)"' >> ~/.bashrc
RUN echo 'fi' >> ~/.bashrc
 
# install python
RUN ~/.pyenv/bin/pyenv install 3.7.0
RUN ~/.pyenv/bin/pyenv global 3.7.0
 
# upgrade pip
RUN ~/.pyenv/shims/pip install --upgrade pip
 
# install numpy
RUN ~/.pyenv/shims/pip install numpy

# install mojimoji
RUN ~/.pyenv/shims/pip install mojimoji

# install janome
RUN ~/.pyenv/shims/pip install janome
