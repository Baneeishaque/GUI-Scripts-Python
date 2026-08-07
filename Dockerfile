FROM python:3.14.7

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./Tkinter_demo.py" ]
