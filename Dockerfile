#FROM python:3.8-slim-buster

#RUN apt update -y && apt install awscli -y
#WORKDIR /app

#COPY . /app
#RUN pip install -r requirements.txt

#CMD ["python3", "streamlit run app.py"]

FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY . /app

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
