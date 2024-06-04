from fastapi import APIRouter, HTTPException, status
from models.posts import Posts, CreatePost
from typing import Union

router = APIRouter()

posts: list[Posts] = []

@router.get('/posts/{id}')
async def get_one_post(id: int):
    try:
        return posts[id]
    except:
        return HTTPException(status_code=404)

@router.post('/posts', status_code=status.HTTP_201_CREATED)
async def create(payload: CreatePost):
    try:
        post = Posts(id=len(posts), title=payload.title, description=payload.description)
        posts.append(post)
        return post
    except:
        return HTTPException(status_code=503, detail="Не удалось создать пост")