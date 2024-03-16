import vk_api
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

    def init_state_handler(self, event):
        pass

    def shs1_clicked_handler(self, event):
        pass

    def shs2_clicked_handler(self, event):
        pass

    def shs3_clicked_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.text() == "Кафедра СГН3":
                message = "Описание кафедры"
                keyboard = {
                    "one_time": False, "buttons": [
                        [
                            {
                                "action": {
                                    "type": "text",
                                    "label": "Заведующий кафедрой"
                                },
                                "color": "green"
                            },
                            {
                                "action": {
                                    "type": "text",
                                    "label": "Направление подготовки"
                                },
                                "color": "green"
                            },
                            {
                                "action": {
                                    "type": "text",
                                    "label": "Проходной балл в этом году"
                                },
                                "color": "green"
                            }
                        ],
                        [
                            {
                                "action": {
                                    "type": "text",
                                    "label": "Назад"
                                },
                                "color": "negative"
                            }
                        ]
                    ]
                }
                self.vk.messages.send(
                    peer_id=event.object.peer_id,
                    random_id=get_random_id(),
                    message=message,
                    keyboard=keyboard)

    def shs4_clicked_handler(self, event):
        pass
