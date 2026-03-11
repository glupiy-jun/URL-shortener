from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from .crud import create_url, get_url, add_click

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/shorten")
def shorten(data: dict, db: Session = Depends(get_db)):

    url = data.get("url")

    if not url:
        raise HTTPException(status_code=400, detail="URL required")

    created = create_url(db, url)

    return {"short_id": created.short_id}

@app.get("/{short_id}")
def redirect(short_id: str, db: Session = Depends(get_db)):

    url = get_url(db, short_id)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    add_click(db, url)

    return RedirectResponse(url.original_url)

@app.get("/stats/{short_id}")
def stats(short_id: str, db: Session = Depends(get_db)):

    url = get_url(db, short_id)

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "url": url.original_url,
        "clicks": url.clicks
    }
