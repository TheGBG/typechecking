from typing import Optional, TypedDict

class CV(TypedDict):    
    title: str
    YOE: Optional[int]

class User(TypedDict):
    name: str
    age: int
    cv: CV
