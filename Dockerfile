FROM python
RUN apt-get update
RUN apt-get install -y python python3-pip wget
RUN pip install Flask
RUN pip install requests
RUN pip install flask_mysqldb
RUN pip install jsonpickle
RUN mkdir /app
COPY . /app/
WORKDIR app
ENTRYPOINT ["python"]
CMD ["randomapp.py"]