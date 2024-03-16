import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from enum import Enum


class VkBotState(Enum):
    INIT_STATE = 0
    SHS1_CLICKED = 1
    SHS2_CLICKED = 2
    SHS3_CLICKED = 3
    SHS4_CLICKED = 4

class VkBot:
    def __init__(self, group_id, group_token):
        self.state = VkBotState.INIT_STATE
        self.vk_session = vk_api.VkApi(token=group_token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=group_id)

    def start(self):
        for event in self.longpoll.listen():
            self.step(event)

    def step(self, event):
        if self.state == VkBotState.INIT_STATE:

            self.init_state_handler(event)

        elif self.state == VkBotState.SHS1_CLICKED:

            self.shs1_clicked_handler(event)

        elif self.state == VkBotState.SHS2_CLICKED:

            self.shs2_clicked_handler(event)

        elif self.state == VkBotState.SHS3_CLICKED:

            self.shs3_clicked_handler(event)

        else:

            self.shs4_clicked_handler(event)

    messages = [
        {
            "text1": 'Добро пожаловать на факультет "Социальные и Гуманитарные Науки"!',
            "text2": 'Нажмите на кнопку, чтобы узнать о его кафедрах.',
            "photo": "photo_url",
            "buttons": ["СГН1", "СГН2", "СГН3", "СГН4"]
        },
        {
            "text": 'Кафедра СГН1 преподаёт дисциплину "История России" всем студентам Бауманки.',
            "photo": "photo_url",
            "buttons": ["Заведующий кафедрой СГН1", "Преподавательский состав"]
        },
        {
            "text": "Описание кафедры СГН2",
            "photo": "photo_url",
            "buttons": ["Заведующий кафедрой СГН2", "Преподавательский состав"]
        },
        {
            "text": "Описание кафедры СГН3",
            "photo": "photo_url",
            "buttons": ["Заведующий кафедрой СГН3", "Преподавательский состав"]
        },
        {
            "text": "Описание кафедры СГН4",
            "photo": "photo_url",
            "buttons": ["Заведующий кафедрой СГН4", "Преподавательский состав"]
        },
        {
            "text": "Контактная информация заведующего кафедрой СГН1",
            "photo": "photo_url",
            "buttons": ["Назад"]
        },
        {
            "text": "Контактная информация заведующего кафедрой СГН2",
            "photo": "photo_url",
            "buttons": ["Назад"]
        },
        {
            "text": "Контактная информация заведующего кафедрой СГН3",
            "photo": "photo_url",
            "buttons": ["Назад"]
        },
        {
            "text": "Контактная информация заведующего кафедрой СГН4",
            "photo": "photo_url",
            "buttons": ["Назад"]
        }
    ]

    def init_state_handler(self, event):
        pass

    def shs1_clicked_handler(self, event):
        pass

    def shs2_clicked_handler(self, event):
        pass

    def shs3_clicked_handler(self, event):
        keyboard = VkKeyboard(inline=True)
        keyboard.add_callback_button("Заведующий кафедрой", color=VkKeyboardColor.SECONDARY)
        keyboard.add_line()
        keyboard.add_callback_button("Преподавательский состав", color=VkKeyboardColor.GREEN)
        keyboard.add_line()
        keyboard.add_button("Назад", color=VkKeyboardColor.NEGATIVE)



        #message = messages[3]
        #self.send_message(event.object.peer_id, message["text"], message["photo"], message["buttons"])
        #self.vk.messages.send(
        #    peer_id=event.object.peer_id,
        #    random_id=get_random_id(),
        #    message=message,
        #    keyboard=keyboard)

    def shs4_clicked_handler(self, event):
        pass
