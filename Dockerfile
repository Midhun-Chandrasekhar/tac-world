FROM python:3.8

ADD tac /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000

# Initializing Redis server and Gunicorn server from supervisord
# CMD ["supervisord","-c","/src/supervisor/service_script.conf"]