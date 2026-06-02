from fastapi import FastApi

app = FastApi()

@app.get("/hello")
def hello():
    return {"message": "Hello world!"}