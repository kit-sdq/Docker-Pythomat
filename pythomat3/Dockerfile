FROM alpine

RUN apk update && apk upgrade && apk add \
  python3 openjdk8

ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV PATH=$PATH:$JAVA_HOME/bin

# COPY /chardet /
# COPY /fakeomat /
# COPY /pythomat /
# COPY /usage /
COPY / /

WORKDIR /usage/praktomat
RUN python3 test_sample_solution.py -o out.html
CMD cat out.html
