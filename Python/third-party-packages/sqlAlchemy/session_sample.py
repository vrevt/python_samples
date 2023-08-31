from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://vrevt:12311231@localhost/")


some_object = {'a': 1, 'b': 2}
some_other_object = {'c': 3, 'd': 4}

# create session and add objects
with Session(engine) as session:
    session.add(some_object)
    session.add(some_other_object)
    session.commit()


with Session(engine) as session:
    session.begin()
    try:
        session.add(some_object)
        session.add(some_other_object)
    except:
        session.rollback()
        raise
    else:
        session.commit()
