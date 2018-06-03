FROM python:3

COPY . /var/app
WORKDIR /var/app
RUN pip install --no-cache-dir -r setup/requirements.txt \
    export FLASK_APP=app/main.py \


CMD [ "flask", "run"]