FROM python:3

WORKDIR /home

RUN pip install pandas more-itertools requests openpyxl

COPY copyT.py CarsData.xlsx ./

CMD python copyT.py  
