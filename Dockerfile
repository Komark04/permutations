FROM python:3

WORKDIR /home

RUN pip install pandas more-itertools requests openpyxl

COPY Cars.py CarsData.xlsx ./

CMD python Cars.py  
