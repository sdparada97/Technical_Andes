FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim

WORKDIR /Technical_Andes

COPY . /Technical_Andes/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]