FROM python:2

RUN \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      libprotobuf-dev \
      protobuf-compiler \
  && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/

ENV \
  MYSQLXPB_PROTOC=/usr/bin/protoc \
  MYSQLXPB_PROTOBUF_INCLUDE_DIR=/usr/include/google/protobuf \
  MYSQLXPB_PROTOBUF_LIB_DIR=/usr/lib/x86_64-linux-gnu

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT [ "./run.py" ]
