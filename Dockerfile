FROM python:3.7.0

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./Tkinter_demo.py" ]
