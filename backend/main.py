from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_jokes():
    return {"joke": "Why did the scarecrow win an award? Because he was outstanding in his field!"}