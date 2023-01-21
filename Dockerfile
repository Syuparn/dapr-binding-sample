FROM python
WORKDIR /app
COPY . . 
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["main.py"]
