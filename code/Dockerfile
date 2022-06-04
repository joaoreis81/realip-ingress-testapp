FROM python:3.10-slim

# set working directory
WORKDIR /code

# add and install requirements
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY ./main.py /code/main.py

# port to expose
EXPOSE 8000

# add user
RUN useradd -ms /usr/sbin/nologin appuser

# change to user
USER appuser

# run server
CMD ["uvicorn", "main:app", "--proxy-headers", "--forwarded-allow-ips","0.0.0.0/0","--host", "0.0.0.0", "--port", "8000"]
