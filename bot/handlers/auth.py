from typing import Optional

from aiogram import Router, types
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from bot import db, texts


router = Router(name="Auth")


class Auth(StatesGroup):
    user_id = State()


async def send_welcome_message(msg: types.Message, state: FSMContext, user_status: Optional[db.User]):
    if not user_status:
        await msg.answer(
            text=texts.Start.NotExist.text,
            reply_markup=texts.Start.NotExist.builder
        )

        await state.set_state(Auth.user_id)
    else:
        await msg.answer(
            text=texts.Start.Exist.text,
            reply_markup=texts.Start.Exist.builder.as_markup(resize_keyboard=True)
        )


@router.message(CommandStart())
async def start(msg: types.Message, state: FSMContext, session: db.AsyncSession):
    await state.clear()

    user = await db.get_user(msg.from_user.id, session)

    await send_welcome_message(msg, state, user)


@router.message(Auth.user_id)
async def handle_user_id_and_create_user(msg: types.Message, state: FSMContext, session: db.AsyncSession):
    if not msg.text.isdigit():
        user = None
    else:
        user = await db.insert_user(int(msg.text), msg.from_user.id, session)

    await send_welcome_message(msg, state, user)
