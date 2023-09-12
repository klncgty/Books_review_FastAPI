from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title": "Title one", "author": "author one", "category": "science"},
    {"title": "Title two", "author": "author two", "category": "science"},
    {"title": "Title three", "author": "author three", "category": "math"},
    {"title": "Title four", "author": "author four", "category": "math"},
    {"title": "Title five", "author": "author five", "category": "history"},

]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book["title"].casefold() == book_title.casefold():
            return book

@app.get("/books")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book["category"].casefold() == category.casefold()
            books_to_return.append(book)
        return books_to_return

@app.get("/books/{book_author}")
async def read_author_category_by_query(category: str, author=str)
    books_to_return = []
    for book in BOOKS:
        if book["author"].casefold() == author.casefold() and \
            book["category"].casefold() == category.casefold()
            books_to_return.append(book)
        return books_to_return
    
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)
    
@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i]["title"].casefold() == updated_book["title"].casefold():
           BOOKS[i] = update_book
