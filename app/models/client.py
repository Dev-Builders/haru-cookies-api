import enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from app.db.base import Base

class ClientSource(enum.Enum):
    IFOOD = "ifood"
    ALPHAVIEW = "alphaview"
    NOVA_BARUERI = "nova_barueri"
    EXTERNO = "externo"

class Clients(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    adress = Column(String, nullable=False)
    source = Column(Enum(ClientSource), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
