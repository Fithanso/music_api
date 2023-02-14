FROM python

WORKDIR /music_api

COPY . .

EXPOSE 8000:8000

RUN pip install -r requirements.txt
