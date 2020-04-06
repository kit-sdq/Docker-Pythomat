FROM alpine

RUN apk update && apk add \
  python3 openjdk11
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk
ENV PATH=$PATH:$JAVA_HOME/bin

COPY / /
WORKDIR /usage/praktomat
RUN ./package.sh
CMD python3 pythomat.zip -o /prod/target/solution.html /prod/solution
