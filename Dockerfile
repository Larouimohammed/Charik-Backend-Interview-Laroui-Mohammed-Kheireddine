FROM python:3.10-slim

ENV DockerHOME=/home/app/hubspot
ENV HUBSPOT_TOKEN=''
ENV DEBUG=True
ENV ALLOWED_HOSTS=*

RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME  
COPY . $DockerHOME 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000  
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver",  "0.0.0.0:8000"]




