import hug
from sqlalchemy.orm.session import Session
from DirFile.DBGlaobal.context import DbSessionFactory
# import config


@hug.directive()  # register single hug directive
class SqlalchemySession(Session):

    def __new__(cls, rel_folder='DB', *args, context: DbSessionFactory = None, **kwargs):
        return context.global_init(rel_folder)
