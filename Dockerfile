FROM python:3.10-alpine

VOLUME /app/src
EXPOSE 8000
WORKDIR /app

COPY requirements.lock .
RUN sed '/-e/d' requirements.lock > requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "src.catboard.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
