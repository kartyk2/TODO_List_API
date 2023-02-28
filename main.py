from app import app
import APIs


@app.get("/")
async def root_api():
    return {"works": "Fine"}


