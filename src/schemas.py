from pydantic import BaseModel, EmailStr

class ItemBase(BaseModel):
    title: str
    description: str = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    is_active: bool = True

    class Config:
        orm_mode = True

class UserInDB(UserBase):
    id: int

    class Config:
        orm_mode = True
    
class User(UserBase):
    id: int
    items: list[Item] = []
    
    class Config:
        orm_mode = True

class ItemUser(ItemBase):
    id: int
    owner: UserInDB

    class Config:
        orm_mode = True