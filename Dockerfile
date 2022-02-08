FROM python:3.11.0a2-bullseye
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN chmod +x ./start.sh
RUN pip install --upgrade pip 
RUN pip install --upgrade -r requirements.txt 
EXPOSE 80
CMD ["./start.sh"]
