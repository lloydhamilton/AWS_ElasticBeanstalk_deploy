FROM python:3.9-slim
COPY ./fit_app.py /deploy/
COPY ./requirements.txt /deploy/
WORKDIR /deploy/
RUN pip install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run"]
CMD ["fit_app.py"]