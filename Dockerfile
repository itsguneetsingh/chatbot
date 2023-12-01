FROM python:3.11.5

ADD main.py .
ADD requirements.txt .
ADD chatbot.py .
ADD constants.py .
ADD SpeechToText.py .
ADD pineconedb.py .


RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]