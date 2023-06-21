FROM python:alpine

RUN mkdir testing_folder
RUN cd testing_folder
WORKDIR /testing_folder

ADD app.py .

CMD ["python3", "-u", "app.py"]


