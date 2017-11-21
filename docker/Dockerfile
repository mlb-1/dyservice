FROM centos

USER root
##create dirs(etc,logs)
RUN mkdir -p /etc/dyservice
RUN mkdir -p /var/log/dyservice/api

##get source code
RUN yum install -y git gcc  epel-release python-devel net-tools
RUN yum -y install python-pip
RUN yum clean all
RUN pip install --upgrade pip
RUN pip install pbr
RUN pip install setuptools

##copy source to docker
COPY ./dyservice /dyservice

RUN pip install --no-cache-dir --retries 10 -r /monasca-api/requirements.txt
COPY ./dyservice/common/start.sh /usr/bin/start-dyservice.sh

WORKDIR /dyservice
RUN pip install -e . 

RUN chmod +x /usr/bin/start-dyservice.sh
EXPOSE 8082
ENTRYPOINT /usr/bin/start-dyservice.sh

