from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BIGINT, Integer, String


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(BIGINT, unique=True, nullable=False)
    user_id = Column(BIGINT, nullable=False)
    token = Column(String, nullable=False, default="USDT")
    currencies = Column(String, nullable=False, default="UAH")
    payment = Column(String, nullable=False, default="43")
    amount = Column(String, nullable=False, default="")
