from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


class Start:

    class Exist:

        text = "Добро пожаловать!"

        builder = ReplyKeyboardBuilder()
        builder.row(
            *[
                types.KeyboardButton(
                    text="Редактировать User ID"
                ),
                types.KeyboardButton(
                    text="Редактировать Token"
                ),
                types.KeyboardButton(
                    text="Редактировать Currencies"
                ),
                types.KeyboardButton(
                    text="Редактировать Payment"
                ),
                types.KeyboardButton(
                    text="Редактировать Amount"
                )
            ],
            width=2
        )

    class NotExist:

        text = "Введите User ID с ByBit:"

        builder = types.ReplyKeyboardRemove()


class Edit:

    builder = ReplyKeyboardBuilder()
    builder.add(
        *[
            types.KeyboardButton(
                text="Отмена"
            )
        ]
    )

    class UserID:

        text = "Введите новый User ID:"

    class Token:

        text = "Выберите новый Token:"

    class Currencies:

        text = "Выберите новые Currencies:"
