from typing import Optional, Union
from pydantic import BaseModel

class Posts(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    likes: int = 0

class CreatePost(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    is_hiden: bool = False

class DeletePost(BaseModel):
    id: int

class UpdatePost(BaseModel):
    id: int
    title: str
    description: Optional[str]
    is_hiden: bool