FROM python:3

COPY . /var/app
WORKDIR /var/app
RUN pip install --no-cache-dir -r setup/requirements.txt
ENV FLASK_APP=app/main.py
ENV FLASK_DEBUG=1


CMD [ "flask", "run", "--host=0.0.0.0"]