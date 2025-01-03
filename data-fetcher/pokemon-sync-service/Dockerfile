# Build Stage
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Final Stage
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
CMD ["python", "main.py"]
