import datetime
import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, nullable=True, index=True, unique=True)
    hashed_password = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    news = orm.relationship('News', back_population="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)