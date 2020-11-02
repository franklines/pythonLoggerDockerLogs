# Python Logger Docker/Kubectl Logs Workaround

`docker logs -f <container>` & `kubectl logs -f <pod name>` stream the stdout of the PID 1 process running on the container. If you have a script that writes to stdout but is not running under the PID 1 process, you will not see logs for them. This repo has a workaround example, basically a Python script that logs to PID 1's stdout.

## Build & Run Docker Container

```bash
# build
docker build -t test:latest .

# run
docker run -d --name testing test:latest
```

## Running Python Logger Script

```bash
# shell
docker exec -it testing bash

# run script
python3 /usr/local/bin/logtest.py

# log output
docker logs -f testing


2020-11-02 03:15:26,537 - root - INFO - Log message sent from Python logger script to pid 1 stdout
2020-11-02 03:23:52,849 - root - INFO - Log message sent from Python logger script to pid 1 stdout
2020-11-02 03:25:55,910 - root - INFO - Log message sent from Python logger script to pid 1 stdout
```