""" 
main app for project
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid

# TODO add logging for proper debugging.

app = FastAPI()

class Book(BaseModel):
    """ 
    Inheriting BaseModel to create a book object for POST operations
    """
    id: uuid.UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=101)

BOOKS = []

@app.get("/")
async def read_api():
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
async def update_book(book_id: uuid.UUID, book: Book):
    """ 
    take in a path parameter of a UUID and a nook request body
    """
    counter = 0
    for item in BOOKS:
        counter += 1
        if item.id == book_id:
            BOOKS[counter - 1] == book
            return BOOKS[counter - 1]
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} : Does not exist."
    )