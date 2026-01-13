from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from typing import List


db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    
    children: Mapped[List["FavoritePlanets"]] = relationship(back_populates="user")
    children: Mapped[List["FavoriteCharacters"]] = relationship(back_populates="user")
    children: Mapped[List["FavoriteStarships"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    planets_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    
    children: Mapped[List["FavoritePlanets"]] = relationship(back_populates="Planets")
    children: Mapped[List["Characters"]] = relationship(back_populates="Planets")


    def serialize(self):
        return {
            "id": self.id,
            "planets_name": self.planets_name,
            # do not serialize the password, its a security breach
        }
    

class Characters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    character_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    
    planets_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    parent: Mapped["Planets"] = relationship(back_populates="characters")

    children: Mapped[List["FavoriteCharacters"]] = relationship(back_populates="Characters")


    def serialize(self):
        return {
            "id": self.id,
            "character_name": self.character_name,
            "planets_id": self.planets_id
            # do not serialize the password, its a security breach
        }
    
class Starships(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    starships_name: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    
    children: Mapped[List["FavoriteStarships"]] = relationship(back_populates="Starships")

    

    def serialize(self):
        return {
            "id": self.id,
            "starships_name": self.starships_name,
            # do not serialize the password, its a security breach
        }
class FavoritePlanets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    parent: Mapped["User"] = relationship(back_populates="FavoritePlanets")
    parent: Mapped["Planets"] = relationship(back_populates="FavoritePlanets")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            # do not serialize the password, its a security breach
        }
class FavoriteCharacters(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    characters_id: Mapped[int] = mapped_column(ForeignKey("characters.id"))
    parent: Mapped["User"] = relationship(back_populates="FavoritePlanets")
    parent: Mapped["Characters"] = relationship(back_populates="FavoriteCharacters")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "characters_id": self.characters_id,
            # do not serialize the password, its a security breach
        }

class FavoriteStarships(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    starships_id: Mapped[int] = mapped_column(ForeignKey("starships.id"))
    parent: Mapped["User"] = relationship(back_populates="FavoriteStarships")
    parent: Mapped["Starships"] = relationship(back_populates="FavoriteStarships")


    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "starships_id": self.starships_id,
            # do not serialize the password, its a security breach
        }
