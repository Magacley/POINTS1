import datetime
import sqlalchemy.orm


from DirFile.DBGlaobal.base import SqlAlchemyBase


class Point(SqlAlchemyBase):
    __tablename__ = 'Points'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    gameName = sqlalchemy.Column(sqlalchemy.String, index=True)
    year = sqlalchemy.Column(sqlalchemy.Integer, index=True)
    # created = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, index=True)
    old_high_score = sqlalchemy.Column(sqlalchemy.Integer)
    days_high_score = sqlalchemy.Column(sqlalchemy.Integer)
    personal_score = sqlalchemy.Column(sqlalchemy.Integer)
    display_order = sqlalchemy.Column(sqlalchemy.Integer, index=True)

    player_Id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('Player.id'))
    player = sqlalchemy.orm.relationship('Player', back_populates='points')
