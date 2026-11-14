from pydantic import basemodel

class MovieCreate(BaseModel):
    title: str
    director: str

    class Movie(MovieCreate)
        id: int