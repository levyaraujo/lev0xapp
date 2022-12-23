FROM python:3.10.9-slim
ENV FLASK_APP=src.app:create_app
ENV APP_ENV=docker
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["flask", "run", "--host=0.0.0.0"]
EXPOSE 5000