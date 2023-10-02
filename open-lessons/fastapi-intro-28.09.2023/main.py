from fastapi import FastAPI

from views import router_api_v1

app = FastAPI()
app.include_router(router_api_v1)


@app.get("/")
def root():
    return {"message": "Hello Index!"}


@app.get("/hello/")
def hello(name: str):
    return {"message": f"Hello {name}!"}
