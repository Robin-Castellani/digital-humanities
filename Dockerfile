FROM python:3.9.1-slim

WORKDIR /usr/src/app

# install poetry to manage the dependencies
RUN pip install poetry==1.1.3

# copy all the files into the image
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install


ENTRYPOINT ["python", "-m", "medicus-politicus.main"]

LABEL org.opencontainers.image.source https://github.com/robin-castellani/digital-humanities
