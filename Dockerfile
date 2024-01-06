#FROM python:3.8-slim-buster

#RUN apt update -y && apt install awscli -y
#WORKDIR /app

#COPY . /app
#RUN pip install -r requirements.txt

#CMD ["python3", "streamlit run app.py"]

FROM python:3.8-slim-buster

EXPOSE 8501

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]