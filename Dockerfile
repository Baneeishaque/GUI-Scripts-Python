FROM python:3.12.2

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./Tkinter_demo.py" ]
