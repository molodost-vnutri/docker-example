# 
FROM python:3.9

# 
WORKDIR /src

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./src /src

# 
CMD ["uvicorn", "src/main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]