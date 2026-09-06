#!/usr/bin/env python3
"""
REST API Project using FastAPI
A tiny in-memory REST API for notes with endpoints to create/read/delete notes.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Note(BaseModel):
    id: int
    title: str
    content: str

_db: List[Note] = []

@app.post('/notes', response_model=Note)
def create_note(note: Note):
    if any(n.id == note.id for n in _db):
        raise HTTPException(status_code=400, detail='ID exists')
    _db.append(note)
    return note

@app.get('/notes', response_model=List[Note])
def list_notes():
    return _db

@app.get('/notes/{note_id}', response_model=Note)
def get_note(note_id: int):
    for n in _db:
        if n.id == note_id:
            return n
    raise HTTPException(status_code=404, detail='Not found')
