from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    """
    -> Used to provice configurations to Pydantic
    -> Setting a config value, not declaring a type
    
        Using this, the Pydantic model is compatible with ORMs, and you can just declare it in the `response_model`
    argument in your path operations.

    使用`orm_mode=True`可以让Pydantic知道这个模型是一个ORM模型，并按照ORM模型模式处理输入数据。着对于从数据库中读取数据并将其转换为Python对象非常有用
    """
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
