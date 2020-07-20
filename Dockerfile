FROM ubuntu:18.04

RUN mkdir /home/work
WORKDIR /home/work

RUN apt update -y && apt install -y vim && apt install -y curl && apt install -y git && apt install -y python3 && apt install -y python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip3 install pillow && pip3 install pytesseract

RUN apt install -y tesseract-ocr && apt install -y libtesseract-dev && apt install -y sudo

RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

RUN apt install -y nodejs

RUN npm install http-server -g

RUN git clone https://github.com/arvincsh/zMEC_text_host_v1.git

WORKDIR /home/work/zMEC_text_host_v1

RUN npm install express && npm install formidable

RUN mkdir page && cd page && mkdir upload && cd ..

RUN npm install forever -g

CMD [ "forever", "server.js" ]
