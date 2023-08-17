from celery import Celery


broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'

app_celery = Celery('tasks', broker='pyamqp://guest@localhost//')


@app_celery.task
def add(x, y):
    return print(x + y)
