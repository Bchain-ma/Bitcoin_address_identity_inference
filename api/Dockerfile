FROM python:3.6

WORKDIR /app

ENV FLASK_APP=api.py 

ENV FLASK_ENV=development

COPY ./requirements.txt ./model.pkl ./BitcoinHeistData.csv ./api.py .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "api.py" ]