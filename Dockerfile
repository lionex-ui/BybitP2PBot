FROM python:3.9-slim

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install poetry==1.8.3
RUN poetry config virtualenvs.in-project true
RUN poetry install

COPY . /app

CMD ["poetry", "run", "python3", "main.py"]