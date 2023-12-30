FROM orgoro/dlib-opencv-python:3.7
WORKDIR /code
# COPY poetry.lock /code/
# COPY pyproject.toml /code/
# RUN pip install poetry
# RUN poetry config virtualenvs.create true
# RUN poetry install
COPY . /code/
RUN pip install -r req.txt
RUN pip install python-multipart
ENV GOOGLE_APPLICATION_CREDENTIALS "/code/admit_key.json"
EXPOSE 8080
CMD [ "uvicorn","server:app","--port","8080","--host","0.0.0.0" ]
