from fastapi import FastAPI

app = FastAPI()  # Ensure this line is present

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
  m
  
