FROM python:3.9.5

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY myapp.py .

VOLUME /app/

EXPOSE 5000

CMD python myapp.py
