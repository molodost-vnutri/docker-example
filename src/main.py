from fastapi import FastAPI
from controllers.posts import router

app = FastAPI()


app.include_router(router)