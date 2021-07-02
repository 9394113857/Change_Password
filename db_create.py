from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# MySQL Database:-
#engine = create_engine('mysql://root:raghu@localhost/password', echo=True)
# sqlite Database:-
engine = create_engine('sqlite:///user.db', echo = True)
meta = MetaData()

User = Table(
    'User', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), unique=True, nullable=False),
    Column('email', String(120), unique=True, nullable=False),
    Column('password', String(60), nullable=False),
)
# users = Table(
#     'users', meta,
#     Column('id', Integer(), primary_key=True, autoincrement=True),
#     Column('email', String(30), unique=True, nullable=False),
#     Column('password_plaintext', String(60), nullable=False),
# )
meta.create_all(engine)

