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

def upload_photo(vk, photo):
        upload = VkUpload(vk)
        response = upload.photo_messages(photo)[0]
        owner_id = response['owner_id']
        photo_id = response['id']
        access_key = response['access_key']

        return owner_id, photo_id, access_key

def send_message(vk, peer_id, owner_id, photo_id, access_key, message):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
    random_id=get_random_id(),
    peer_id=peer_id,
    message=message,
    attachment=attachment
)



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


    def init_state_handler(self, event):
        self.vk.messages.send(user_id=event.obj.message['from_id'], random_id=get_random_id(), peer_id=event.obj.message['from_id'], keyboard=self.get_keyboard_1(), message=event.obj.message['text'])
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
                deanery_clicked_handler(self, event)

    def shs1_clicked_handler(self, event):
        pass

    def shs2_clicked_handler(self, event):
        pass

    def shs3_clicked_handler(self, event):
        pass

    def shs4_clicked_handler(self, event):
        pass

    def deanery_clicked_handler(self, event):
        last_id = self.vk.messages.edit(peer_id=event.obj.peer_id, message='❕Кабинеты деканата располагаются в УЛК на 7 этаже.\n Декан: Ремарчук Валерий Николаевич (кабинет 703л)\nЗам. декана по молодёжной политике\n и воспитательной деятельности: Гаврилова Юлия Викторовна', conversation_message_id=event.obj.conversation_message_id)

    
        




