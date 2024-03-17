import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api import VkUpload
from enum import Enum

MESSAGES = {
    'init_state': """❕Кабинеты деканата располагаются в УЛК на 7 этаже.\n
    Декан: Ремарчук Валерий Николаевич (кабинет 703л)\n
    Зам. декана по молодёжной политике\n
    и воспитательной деятельности: Гаврилова Юлия Викторовна""",

    'shs1_state': """Кафедра СГН1 занимается исключительно преподавателькой деятельностью.\n
    Её преподавательский состав преподаёт дисциплину «История России» всем студентам Бауманки""",

    'shs2_state': """Кафедра занимается подготовкой кадров по направлению «Социалогия.»
    Образовательной программой данной кафедры является «Социалогия техники и инженерной деятельности».
    Выпускники кафедры востребованы в таких местах, как:\n
    1. В органах государственной и муниципальной власти;\n
    2. В экспертных структурах и в информационно-аналитических центрах;\n
    3. В агентствах по найму и управлению персоналом;""",

    'shs3_state': """Кафедра занимается подготовкой кадров по направлению «Прикладная информатика».
    Образовательной программой кафедры является «Информационная аналитика и политические технологии».
    Здесь студентов учат не только информатике, программированию, но и аналитике данных.
    Выпускники кафедры могут устроиться работать аналитиками данных в такие компании, как:
    Яндекс, ВК, Сбер, Аналитический Центр при Правительстве РФ, ВТБ, РЖД, и прочие. """,

    'shs4_state': """Кафедра СГН4 в основном нацелена на аспирантов Бауманки.\n
    Она занимается подготовкой аспирантов по дисциплинам:\n,
    1. «Социальная и политическая философия»\n
    2. «Философия науки и техники».\n
    Для студентов бакалавриата кафедра несёт исключительно преподавательский характер.\n
    Преподаватели ведут такие дисциплины, как «Логика» и «Философия».""",
}


class VkBotState(Enum):
    INIT_STATE = 0
    SHS1_CLICKED = 1
    SHS2_CLICKED = 2
    SHS3_CLICKED = 3
    SHS4_CLICKED = 4


def upload_photo(vk_session, photo):
    upload = VkUpload(vk_session)
    response = upload.photo_messages(photo)[0]
    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    return attachment


def init_state_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_callback_button(label='СГН1', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS1"})
    keyboard.add_callback_button(label='СГН2', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS2"})
    keyboard.add_line()
    keyboard.add_callback_button(label='СГН3', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS3"})
    keyboard.add_callback_button(label='СГН4', color=VkKeyboardColor.PRIMARY, payload={"type": "SHS4"})
    keyboard.add_line()
    keyboard.add_callback_button(label='Деканат', color=VkKeyboardColor.POSITIVE, payload={"type": "DEANERY"})
    return keyboard


class VkBot:
    def __init__(self, group_id, group_token):
        self.state = VkBotState.INIT_STATE
        self.vk_session = vk_api.VkApi(token=group_token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=group_id)
        self.attachments = {
            'init_state': upload_photo(self.vk_session, 'resources/sgn.jpg'),
            'shs1_state': upload_photo(self.vk_session, 'resources/sgn1.png'),
            'shs2_state': upload_photo(self.vk_session, 'resources/sgn2.png'),
            'shs3_state': upload_photo(self.vk_session, 'resources/sgn3.png'),
            'shs4_state': upload_photo(self.vk_session, 'resources/sgn4.png'),
        }

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

    def init_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=init_state_keyboard().get_keyboard(),
                message='СГН3 рулит!',
                attachment=self.attachments['init_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'SHS1':

                self.state = VkBotState.SHS1_CLICKED
                self.shs1_clicked_handler(event)

            elif event.object.payload.get('type') == 'SHS2':

                self.state = VkBotState.SHS2_CLICKED
                self.shs2_clicked_handler(event)

            elif event.object.payload.get('type') == 'SHS3':

                self.state = VkBotState.SHS3_CLICKED
                self.shs3_clicked_handler(event)

            elif event.object.payload.get('type') == 'SHS4':

                self.state = VkBotState.SHS4_CLICKED
                self.shs4_clicked_handler(event)

            elif event.object.payload.get('type') == 'DEANERY':

                self.deanery_clicked_handler(event)

    def shs1_clicked_handler(self, event):
        pass

    def shs2_clicked_handler(self, event):
        pass

    def shs3_clicked_handler(self, event):
        self.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs3_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.attachments['shs3_state'],
            keyboard=self.shs3_keyboard().get_keyboard()
        )

    def shs3_keyboard(self):
        keyboard = VkKeyboard(one_time=False, inline=True)
        keyboard.add_callback_button(
            label="Заведующий кафедрой",
            color=VkKeyboardColor.POSITIVE,
            payload={"type": "open_link", "link": "http://fsgn.bmstu.ru/rem.htm"},
        )
        keyboard.add_line()
        keyboard.add_callback_button(
            label="Научная работа",
            color=VkKeyboardColor.POSITIVE,
            payload={"type": "open_link", "link": "http://fsgn.bmstu.ru/analytics/index.php?p=science"},
        )
        keyboard.add_line()
        keyboard.add_callback_button(
            label="Учебная работа",
            color=VkKeyboardColor.POSITIVE,
            payload={"type": "open_link", "link": "https://e-learning.bmstu.ru/sgn/course/index.php?categoryid=4"}
        )
        keyboard.add_line()
        keyboard.add_callback_button(
            label="Назад",
            color=VkKeyboardColor.NEGATIVE,
            payload={"type": "back"}
        )
        return keyboard

    def shs4_clicked_handler(self, event):
        self.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs4_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.attachments['shs4_state'],
            keyboard=self.shs4_keyboard().get_keyboard()
        )

    def shs4_keyboard(self):
        keyboard = VkKeyboard(one_time=False, inline=True)
        keyboard.add_callback_button(
            label="Заведующий кафедрой",
            color=VkKeyboardColor.POSITIVE,
            payload={"type": "open_link", "link": "http://sgn4.bmstu.ru/ivlev"},
        )
        keyboard.add_line()
        keyboard.add_callback_button(
            label="Назад",
            color=VkKeyboardColor.NEGATIVE,
            payload={"type": "back"}
        )
        return keyboard

    def deanery_clicked_handler(self, event):
        last_id = self.vk.messages.edit(
            peer_id=event.obj.peer_id,
            message=MESSAGES['init_state'],
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.attachments['init_state']
        )


