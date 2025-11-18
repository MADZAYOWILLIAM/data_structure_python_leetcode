from fastapi import FastAPI

app=FastAPI()


@app.routes("/")
async def home():
    return "hello"


if __name__=="__main__":
    