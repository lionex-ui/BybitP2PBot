from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.models import User


async def get_user(
        telegram_id: int,
        session: AsyncSession
) -> Optional[User]:

    user: Optional[User] = await session.scalar(
        select(User)
        .filter(
            User.telegram_id == telegram_id
        )
    )

    return user


async def insert_user(
        user_id: int,
        telegram_id: int,
        session: AsyncSession
) -> User:

    user = User(
        telegram_id=telegram_id,
        user_id=user_id
    )

    session.add(user)
    await session.commit()

    return user
