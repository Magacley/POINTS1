import hug
from DirFile.DBGlaobal.context import DbSessionFactory
from DirFile.DBGlaobal.directives import SqlalchemySession
from DirFile.Model.playerPoints import Point
from DirFile.Model.players import Player
import sqlalchemy.orm


# import app


# from DirFile.SerialMash.mashallin import dump_data


@hug.context_factory()  # to register a contaxt factory
def create_context(*args, **kwargs):
    return DbSessionFactory()


@hug.local(Gamedb=False)  # localy to intialize
def initialize(db: SqlalchemySession, rel_folder):
    session = DbSessionFactory.create_session()
    admin = Player(username="admin")
    pplayer = Point(gameName="faster")
    # year=2020,
    # old_high_score=20,
    # days_high_score=300,
    # personal_score=400,
    # display_order=10)
    db.add(admin)
    db.add(pplayer)
    session.add(admin)
    session.add(pplayer)
    db.flush()
    session.commit()


api = hug.API(__name__)
api.http.add_middleware(hug.middleware.CORSMiddleware(api, max_age=None))

initialize()
