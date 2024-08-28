FROM python:3.10-slim

ENV DockerHOME=/home/hubspotuser
ENV HUBSPOT_TOKEN=''
ENV DEBUG=True
ENV ALLOWED_HOSTS=*

RUN groupadd -r hubspotgroupe && useradd -r -g hubspotgroupe hubspotuser

RUN mkdir -p $DockerHOME  
WORKDIR $DockerHOME  
COPY . $DockerHOME 
RUN chown -R hubspotuser:hubspotgroupe  $DockerHOME
RUN chmod -R 755 $DockerHOME 
USER hubspotuser
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000  
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver",  "0.0.0.0:8000"]




