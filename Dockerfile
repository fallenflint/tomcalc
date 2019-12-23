FROM selenium/standalone-chrome

RUN sudo mkdir /code

WORKDIR /code

COPY requirements.txt .

RUN sudo apt-get update && sudo apt-get install -yq python3-pip

RUN pip3 install -r requirements.txt

COPY docker-entry.sh /code
ENTRYPOINT ["/code/docker-entry.sh"]
