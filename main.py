from fastapi import FastAPI
from controllers import card_controller

app = FastAPI(title="API integracao Pipefy")
app.include_router(card_controller.router)