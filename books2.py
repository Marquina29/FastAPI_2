from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()

class book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating 

class BookRequest(BaseModel):
    id: Optional[int] = None
    title:str = Field(min_length=3)
    author:str = Field(min_length=1)
    description:str = Field(min_length=1, max_length=100)
    rating:int = Field(gt=0,lt=6)

BOOKS=[
    book(1,"Computer","author one","a very nice book",4.8),
    book(2,"English","author two","a very nice book",4.4),
    book(3,"Science","author two","a average book",3.5),
    book(4,"History","author four","a nice book",3.8),
    book(5,"English","author one","a very nice book",4.2)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create_books")
async def create_book(book_req:BookRequest):
    new_book = book(**book_req.model_dump())
    BOOKS.append(find_id(new_book))

def find_id(book:book):
    if len(BOOKS)>0:
        book.id = BOOKS[-1].id +1
    else:
        book.id=1

    return book 