from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}

# comando para run -> fastapi dev workout/app.py
# 127.0.0.1:8000/docs
# 127.0.0.1:8000/redoc
