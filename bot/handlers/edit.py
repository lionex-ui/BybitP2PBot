from aiogram import Router, types
from aiogram.filters import CommandStart

from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StatesGroup, State

from bot import db, texts


router = Router(name="Edit")


class Edit(StatesGroup):
    type_of_edit = State()
    value = State()
