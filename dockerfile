FROM python:3.11

WORKDIR \app

COPY final_model.pkl .
COPY pipeline.pkl .
COPY requirements.txt . 
COPY web.py . 

RUN pip install -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "web.py","--server.port=8501","--server.address=0.0.0.0"]

