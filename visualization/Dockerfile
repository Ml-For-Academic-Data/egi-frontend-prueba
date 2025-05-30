FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["panel", "serve", "app.py", "--address=0.0.0.0", "--port=5000", "--allow-websocket-origin=localhost:5000"]
