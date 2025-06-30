#!/usr/bin/python3
"""Delete all State objects with a name containing
the letter 'a' from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database}',
        pool_pre_ping=True
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = (session.query(State)
                        .filter(State.name.like('%a%'))
                        .order_by(State.id).all())

    for state in states_to_delete:
        session.delete(state)
    session.commit()

    session.close()
