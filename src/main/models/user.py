from dataclasses import dataclass


@dataclass
class UserPayload:
    name: str
    email: str


@dataclass
class User:
    id: int
    name: str
    email: str
