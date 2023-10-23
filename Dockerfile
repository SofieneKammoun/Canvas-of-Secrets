FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

ADD notePicGenreation.py .
ADD MainNote.py .
ADD test_required_files.py .
COPY ./wav ./wav
COPY ./notes ./notes

RUN python ./notePicGenreation.py
# Run the first Python script and then the second one
CMD ["python" ,"./MainNote.py" ]
