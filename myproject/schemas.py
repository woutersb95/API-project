from pydantic import BaseModel


class PlayerBase(BaseModel):
    first_name: str
    last_name: str
    position: str


class PlayerCreate(PlayerBase):
    team_id: int


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str
    home_state: str


class TeamCreate(TeamBase):
    pass


class Team(TeamBase):
    id: int
    players: list[Player] = []

    class Config:
        orm_mode = True

