from fastapi import FastAPI
from routers import user, item

app = FastAPI()

app.include_router(user.router)
app.include_router(item.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
