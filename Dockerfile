FROM python:3.9-slim
COPY ./models/rf_clf.joblib /deploy/
COPY ./scripts/flask_api.py /deploy/
COPY poetry.lock pyproject.toml /deploy/
WORKDIR /deploy/
ENV YOUR_ENV=${YOUR_ENV} POETRY_VERSION=1.1.11
RUN pip install "poetry==${POETRY_VERSION}"
RUN poetry config virtualenvs.create false
RUN poetry install
EXPOSE 80
ENTRYPOINT ["python", "flask_api.py"]