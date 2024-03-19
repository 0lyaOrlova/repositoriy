from flask import Flask, render_template
import sqlalchemy.orm as orm
from data import db_session

SqlAlchemyBase = orm.declarative_base()

__factory = None


def global_init(db_file: str) -> None:
    global __factory

    if __factory:
        return
    if not db_file or not db_file.strip():
        raise Exception('Search file bd')
    conn_str = f'sqlite://{db_file.strip()}?check_thread=False'
    print(f'Successfuly with bd in adress{conn_str}')

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()