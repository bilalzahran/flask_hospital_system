FROM python:3.7-alpine
WORKDIR /app/
ENV FLASK_APP=app.app:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
RUN apk add --no-cache gcc musl-dev linux-headers postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD flask run