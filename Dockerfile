FROM python:3.9-slim
COPY ./models/rf_clf.joblib /deploy/
COPY ./scripts/flask_api.py /deploy/
COPY poetry.lock pyproject.toml /deploy/
WORKDIR /deploy/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 80
ENTRYPOINT ["python", "flask_api.py"]