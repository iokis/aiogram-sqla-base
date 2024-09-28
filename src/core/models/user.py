from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Annotated
from sqlalchemy import text, UniqueConstraint, Enum, BigInteger
import datetime

from .base import Base

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class User(Base):
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    created_at: Mapped[created_at]
    role: Mapped[str] = mapped_column(Enum('admin', 'user', name="user_role"), server_default='user', nullable=False)








