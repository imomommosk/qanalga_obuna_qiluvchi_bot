from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    NewPost = State()
    Confirm = State()