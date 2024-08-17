FROM python:3.12.5-alpine3.20 AS builder

COPY requirements.txt ./
RUN pip install --no-cache -r requirements.txt
RUN pip uninstall -y setuptools wheel pip


FROM python:3.12.5-alpine3.20

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/

WORKDIR /app
COPY src ./

CMD ["python", "/app/main.py"]