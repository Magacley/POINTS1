from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field, SQLAlchemyAutoSchema
from sqlalchemy.orm import session

from DirFile.DBGlaobal.context import DbSessionFactory
from DirFile.Model.playerPoints import Point
from DirFile.Model.players import Player
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref, session


class PointSchema(SQLAlchemySchema):
    class Meta:
        model = Point
    load_instance = True
    poitId = auto_field()
    score = auto_field()
    gameName = auto_field()
    created = auto_field()
    isPlayed = auto_field()


class PlayerSchema(SQLAlchemySchema):
    class Meta:
        model = Player
        load_instance = True
    id = auto_field()
    username = auto_field()
    password = auto_field()
    print(username)


# session = DbSessionFactory.create_session()
#
# # Desiralization
# player = Player(username="Said H F")
# player_schema = PlayerSchema()
# point = Point(gameName="JustPlay")
# session.add(point)
# session.add(player)
# session.commit()
# dump_data = player_schema.dump(player)
# print(dump_data)
