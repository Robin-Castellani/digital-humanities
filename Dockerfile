FROM python:3.9.1-slim

WORKDIR /usr/src/app

# install poetry to manage the dependencies
RUN pip install poetry==1.1.3

# copy all the files into the image
COPY . .

# install the core dependencies on the Docker's Python (no virtualenvs)
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# this is the command exposed through the image
# while using it, you just need to interact with the CLI
ENTRYPOINT ["python", "-m", "medicus_politicus.main"]

# label to be recognized in the GitHub Container Registry
LABEL org.opencontainers.image.source https://github.com/robin-castellani/digital-humanities
