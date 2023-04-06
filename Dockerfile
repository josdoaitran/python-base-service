FROM python:3.8-alpine
// or public.ecr.aws/sam/build-python3.8:1
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
EXPOSE 3000-400
CMD ["python", "app.py"]
