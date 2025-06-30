#!/usr/bin/python3
"""List all State objects that contain the letter 'a' from the database"""

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

    results = (session.query(State)
               .filter(State.name.like('%a%'))
               .order_by(State.id).all())

    for state in results:
        print(f"{state.id}: {state.name}")

    session.close()
