FROM python:3.9

ADD elvaTest.py .

CMD ["python", "./elvaTest.py"]