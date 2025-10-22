from fastapi import FastAPI

from app.api import ping, notes
from app.db import engine, database, metadata

# Create tables if not exist
metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# include routers
app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
