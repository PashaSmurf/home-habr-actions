FROM python:3.7-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update && apt-get upgrade -y && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get clean
COPY habr_actions ./habr_actions
EXPOSE 8080
ENTRYPOINT python3.7 -m habr_actions.app
