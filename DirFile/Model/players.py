import sqlalchemy.orm
from sqlalchemy.ext.orderinglist import ordering_list

from DirFile.DBGlaobal.base import SqlAlchemyBase


class Player(SqlAlchemyBase):
    __tablename__ = "Player"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String, index=True)

    points = sqlalchemy.orm.relationship('Points', back_populates='Player',
                                         order_by='Points.display_order',
                                         collection_class=ordering_list('display_order'),
                                         cascade='all')





# venv\Scripts\activate
# # hug -f app.py
