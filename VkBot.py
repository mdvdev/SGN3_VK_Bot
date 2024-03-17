import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
from enum import Enum


class VkBotState(Enum):
    INIT_STATE = 0
    SHS1_CLICKED = 1
    SHS2_CLICKED = 2
    SHS3_CLICKED = 3
    SHS4_CLICKED = 4
    DEANERY_CLICKED = 5


def get_keyboard_1():
    settings = dict(one_time=False, inline=True)
    keyboard_1 = VkKeyboard(**settings)
    keyboard_1.add_callback_button(label='СГН1', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS1"})
    keyboard_1.add_line()
    keyboard_1.add_callback_button(label='СГН2', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS2"})
    keyboard_1.add_line()
    keyboard_1.add_callback_button(label='СГН3', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS3"})
    keyboard_1.add_line()
    keyboard_1.add_callback_button(label='СГН4', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS4"})
    keyboard_1.add_line()
    keyboard_1.add_callback_button(label='Деканат', color=VkKeyboardColor.POSITIVE, payload={"type": "DEANERY"})


def get_keyboard_2():
    settings = dict(one_time=False, inline=True)
    keyboard_2 = VkKeyboard(**settings)
    keyboard_2.add_callback_button(label='Заведующий', color=VkKeyboardColor.POSITIVE, payload={"type": "HEAD_OF_DEPARTMENT"})
    keyboard_2.add_line()
    keyboard_2.add_callback_button(label='Научная работа', color=VkKeyboardColor.PRIMARY, payload={"type": "SCIENTIFIC_WORK"})
    keyboard_2.add_line()
    keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "BACK"})


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

        elif self.state == VkBotState.SHS4_CLICKED:

            self.shs4_clicked_handler(event)

        elif self.state == VkBotState.DEANERY_CLICKED:

            self.deanery_clicked_handler(event)

    def init_state_handler(self, event):
        self.vk.messages.send(user_id=event.obj.message['from_id'], random_id=get_random_id(), peer_id=event.obj.message['from_id'], keyboard=get_keyboard_1(), message=event.obj.message['text'])
        if event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'SHS1':
                self.state = VkBotState.SHS1_CLICKED
            elif event.object.payload.get('type') == 'SHS2':
                self.state = VkBotState.SHS2_CLICKED
            elif event.object.payload.get('type') == 'SHS3':
                self.state = VkBotState.SHS3_CLICKED
            elif event.object.payload.get('type') == 'SHS4':
                self.state = VkBotState.SHS4_CLICKED
            elif event.object.payload.get('type') == 'DEANERY':
                self.state = VkBotState.DEANERY_CLICKED

    def send_message(self, message_text, event):
        image = "sgn.jpg"
        upload = VkUpload(self)
        attachments = []
        upload_image = upload.photo_messages(photos=image)[0]
        attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
        self.vk.messages.send(user_id=event.obj.from_id, random_id=get_random_id(), peer_id=event.obj.peer_id, message=message_text, attachment=attachments)

    def shs1_clicked_handler(self, event):
        pass

    def shs2_clicked_handler(self, event):
        pass

    def shs3_clicked_handler(self, event):
        image = "sgn3.png"
        upload = VkUpload(self)
        attachments = []
        upload_image = upload.photo_messages(photos=image)[0]
        message = shs_messages[3]
        attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))
        self.vk.messages.send(
            peer_id=event.object.peer_id,
            random_id=get_random_id(),
            message=message,
            keyboard=get_keyboard_2(),
            attachment=attachments
        )

    def shs4_clicked_handler(self, event):
        pass


shs_messages = [
    {
        "text11": "Кафедра СГН1 занимается исключительно преподавателькой деятельностью. ",
        "text12": "Её преподавательский состав преподаёт дисциплину История России всем студентам Бауманки",
        "photo": " "
    },
    {
        "text21": "Кафедра занимается подготовкой кадров по направлению Социалогия. ",
        "text22": "Образовательной программой данной кафедры является Социалогия техники и инженерной деятельности. ",
        "photo": " "
    },
    {
        "text31": "Кафедра занимается подготовкой кадров по направлению Прикладная информатика. ",
        "text32": "Образовательной программой кафедры является Информационная аналитика и политические технологии. ",
        "text33": "Здесь студентов учат не только информатике, программированию, но и ",
        "photo": "sgn3.png"
    },
    {
        "text41": "Кафедра СГН4 занимается преподавателькой деятельностью. ",
        "text42": "Преподаватели ведут такие дисциплины, как Логика и Философия, которые изучают студенты бакалавры. ",
        "text43": "Учит аспирантов дисциплинам социальная и политическая философия, философия науки и техники.",
        "photo": "sgn4.png"
    }
]

