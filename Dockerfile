FROM python:3.11 AS requirements-stage
WORKDIR /tmp

RUN pip install poetry poetry-plugin-export
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.11
WORKDIR /app

RUN apt update && apt install -y libxxf86vm-dev libxfixes-dev libxi-dev libxkbcommon-dev libegl-dev && apt-get clean

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# docker build --tag blender .
#  docker run --rm -it --mount type=bind,source=${PWD},target=/app blender bash

# will not work on m1... https://github.com/docker/for-mac/issues/6047
# docker buildx build --platform=linux/amd64 --tag blender .
# docker run --rm -it --platform linux/amd64 --mount type=bind,source=${PWD},target=/app blender bash
