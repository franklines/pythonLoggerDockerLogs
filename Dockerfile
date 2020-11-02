FROM debian:buster-slim
LABEL maintainer="Franklin Escobar"
LABEL github="https://github.com/franklines"

RUN apt-get update && \
    apt-get install -y \
    procps \
    python3 \
    wget 

COPY scripts/logtest.py /usr/local/bin/
RUN chmod +x /usr/local/bin/logtest.py

CMD ["tail", "-f", "/dev/null"]