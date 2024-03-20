import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
from VkBotStateHandler import VkBotStateHandler
from VkBotState import VkBotState


class VkBot:
    def __init__(self, group_id, group_token):
        self.vk_session = vk_api.VkApi(token=group_token)
        self.vk = self.vk_session.get_api()
        self.longpoll = VkBotLongPoll(self.vk_session, group_id=group_id)
        self.states = {}
        self.state_handler = VkBotStateHandler(self)
        self.attachments = {
            'init_state': upload_photo(self.vk_session, 'resources/sgn.jpg'),
            'shs1_state': upload_photo(self.vk_session, 'resources/sgn1.JPG'),
            'shs2_state': upload_photo(self.vk_session, 'resources/sgn2.JPG'),
            'shs3_state': upload_photo(self.vk_session, 'resources/sgn3.JPG'),
            'shs4_state': upload_photo(self.vk_session, 'resources/sgn4.JPG')
        }

    def set_state(self, state, user_id):
        self.states[user_id] = state

    def get_vk(self):
        return self.vk

    def get_attachments(self):
        return self.attachments

    def start(self):
        for event in self.longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW or event.type == VkBotEventType.MESSAGE_EVENT:
                self.step(event)

    def step(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            user_id = event.obj.message['from_id']
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            user_id = event.obj.user_id
        else:
            print('Invalid event occured in FSM step')
            return

        if user_id not in self.states:
            self.states[user_id] = VkBotState.INIT_STATE

        state = self.states[user_id]

        if state == VkBotState.INIT_STATE:
            self.state_handler.init_state_handler(event)
        elif state == VkBotState.SHS1_STATE:
            self.state_handler.shs1_state_handler(event)
        elif state == VkBotState.SHS2_STATE:
            self.state_handler.shs2_state_handler(event)
        elif state == VkBotState.SHS3_STATE:
            self.state_handler.shs3_state_handler(event)
        elif state == VkBotState.SHS4_STATE:
            self.state_handler.shs4_state_handler(event)


def upload_photo(vk_session, photo):
    try:
        upload = VkUpload(vk_session)
        photo = upload.photo_messages(photo)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        return attachment
    except vk_api.exceptions.ApiError as e:
        print(e)
