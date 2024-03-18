from VkBotState import VkBotState
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotEventType


class VkBotStateHandler:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot

    def init_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.get_vk().messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=init_state_keyboard().get_keyboard(),
                message=MESSAGES['init_state'],
                attachment=self.vk_bot.get_attachments()['init_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'SHS1':
                self.vk_bot.set_state(VkBotState.SHS1_STATE)
                self.shs1_state_edit(event)
            elif event.object.payload.get('type') == 'SHS2':
                self.vk_bot.set_state(VkBotState.SHS2_STATE)
                self.shs2_state_edit(event)
            elif event.object.payload.get('type') == 'SHS3':
                self.vk_bot.set_state(VkBotState.SHS3_STATE)
                self.shs3_state_edit(event)
            elif event.object.payload.get('type') == 'SHS4':
                self.vk_bot.set_state(VkBotState.SHS4_STATE)
                self.shs4_state_edit(event)
            elif event.object.payload.get('type') == 'DEANERY':
                self.deanery_clicked_handler(event)

    def init_state_edit(self, event):
        self.vk_bot.get_vk().messages.edit(
            peer_id=event.obj.peer_id,
            message=MESSAGES['init_state'],#чтобы при нажатии кнопки "назад" снова показывалось приветственное сообщение
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.vk_bot.get_attachments()['init_state']
        )

    def shs1_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.get_vk().messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs1_keyboard().get_keyboard(),
                message=MESSAGES['shs1_state'],
                attachment=self.vk_bot.get_attachments()['shs1_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'back':
                self.vk_bot.set_state(VkBotState.INIT_STATE)
                self.init_state_edit(event)
            else:
                try:
                    message = MESSAGES[event.object.payload.get('type')]
                    self.vk_bot.get_vk().messages.edit(
                        peer_id=event.obj.peer_id,
                        message=message,
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=shs1_keyboard().get_keyboard(),
                        attachment=self.vk_bot.get_attachments()['shs1_state']
                    )
                except KeyError:
                    print('Error: unknown button clicked in SHS1')

    def shs1_state_edit(self, event):
        self.vk_bot.get_vk().messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs1_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.get_attachments()['shs1_state'],
            keyboard=shs1_keyboard().get_keyboard()
        )

    def shs2_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.get_vk().messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs2_keyboard().get_keyboard(),
                message=MESSAGES['shs2_state'],
                attachment=self.vk_bot.get_attachments()['shs2_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'back':
                self.vk_bot.set_state(VkBotState.INIT_STATE)
                self.init_state_edit(event)
            else:
                try:
                    message = MESSAGES[event.object.payload.get('type')]
                    self.vk_bot.get_vk().messages.edit(
                        peer_id=event.obj.peer_id,
                        message=message,
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=shs1_keyboard().get_keyboard(),
                        attachment=self.vk_bot.get_attachments()['shs2_state']
                    )
                except KeyError:
                    print('Error: unknown button clicked in SHS2')

    def shs2_state_edit(self, event):
        self.vk_bot.get_vk().messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs2_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.get_attachments()['shs2_state'],
            keyboard=shs2_keyboard().get_keyboard()
        )

    def shs3_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.get_vk().messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs3_keyboard().get_keyboard(),
                message=MESSAGES['shs3_state'],
                attachment=self.vk_bot.get_attachments()['shs3_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'back':
                self.vk_bot.set_state(VkBotState.INIT_STATE)
                self.init_state_edit(event)
            else:
                try:
                    message = MESSAGES[event.object.payload.get('type')]
                    self.vk_bot.get_vk().messages.edit(
                        peer_id=event.obj.peer_id,
                        message=message,
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=shs3_keyboard().get_keyboard(),
                        attachment=self.vk_bot.get_attachments()['shs3_state']
                    )
                except KeyError:
                    print('Error: unknown button clicked in SHS3')

    def shs3_state_edit(self, event):
        self.vk_bot.get_vk().messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs3_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.get_attachments()['shs3_state'],
            keyboard=shs3_keyboard().get_keyboard()
        )

    def shs4_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.get_vk().messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs4_keyboard().get_keyboard(),
                message=MESSAGES['shs4_state'],
                attachment=self.vk_bot.get_attachments()['shs4_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'back':
                self.vk_bot.set_state(VkBotState.INIT_STATE)
                self.init_state_edit(event)
            else:
                try:
                    message = MESSAGES[event.object.payload.get('type')]
                    self.vk_bot.get_vk().messages.edit(
                        peer_id=event.obj.peer_id,
                        message=message,
                        conversation_message_id=event.obj.conversation_message_id,
                        keyboard=shs4_keyboard().get_keyboard(),
                        attachment=self.vk_bot.get_attachments()['shs4_state']
                    )
                except KeyError:
                    print('Error: unknown button clicked in SHS4')

    def shs4_state_edit(self, event):
        self.vk_bot.get_vk().messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs4_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.get_attachments()['shs4_state'],
            keyboard=shs4_keyboard().get_keyboard()
        )

    def deanery_clicked_handler(self, event):
        self.vk_bot.get_vk().messages.edit(
            peer_id=event.obj.peer_id,
            message=MESSAGES['deanery'],
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.vk_bot.get_attachments()['init_state']
        )


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


def shs1_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_callback_button(
        label="Заведующий кафедрой",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs1_head_of_dep"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Научная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs1_scientific_work"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Учебная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs1_academic_work"}
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Назад",
        color=VkKeyboardColor.NEGATIVE,
        payload={"type": "back"}
    )
    return keyboard


def shs2_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_callback_button(
        label="Заведующий кафедрой",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs2_head_of_dep"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Научная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs2_scientific_work"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Учебная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs2_academic_work"}
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Назад",
        color=VkKeyboardColor.NEGATIVE,
        payload={"type": "back"}
    )
    return keyboard


def shs3_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_callback_button(
        label="Заведующий кафедрой",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs3_head_of_dep"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Научная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs3_scientific_work"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Учебная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs3_academic_work"}
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Назад",
        color=VkKeyboardColor.NEGATIVE,
        payload={"type": "back"}
    )
    return keyboard


def shs4_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_callback_button(
        label="Заведующий кафедрой",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs4_head_of_dep"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Научная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs4_scientific_work"},
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Учебная работа",
        color=VkKeyboardColor.PRIMARY,
        payload={"type": "shs4_academic_work"}
    )
    keyboard.add_line()
    keyboard.add_callback_button(
        label="Назад",
        color=VkKeyboardColor.NEGATIVE,
        payload={"type": "back"}
    )
    return keyboard


MESSAGES = {
    'deanery': """❕Кабинеты деканата располагаются в УЛК на 7 этаже.\n
♦️Декан: Ремарчук Валерий Николаевич (кабинет 703л)\n
♦️Зам.декана по молодежной политике и воспитательной деятельности: Гаврилова Юлия Викторовна\n
☎️ Номер телефона для обращения в деканат в летний период:\n
(499)263-60-87""",

    'init_state': """Добро пожаловать на страничку бота ФСГН МГТУ им.Баумана! 👋🏻\n
📚 Факультет социальных и гуманитарных наук готовит профессионалов в сфере информационной аналитики,
прикладной информатики и социологии техники. ФСГН осуществляет глубокую гуманитарную подготовку студентов во всём ВУЗе.

На факультете осваивают профессию студенты двух кафедр:\n
1. СГН2 «Социология и культурология»\n
2. СГН3 «Информационная аналитика и политические технологии»\n
🖌️ Основная особенность обучения на ФСГН состоит в совмещении социально-гуманитарных и технических наук.\n
Такое разностороннее развитие студентов открывает широкие возможности для их будущей карьеры.""",

    'shs1_state': """_""",

    'shs2_state': """_""",

    'shs1_academic_work': """_""",

    'shs1_head_of_dep': """🔴 Заведующий кафедры:
Доктор исторических наук, профессор - Виталий Юрьевич Захаров

🎓 В 1996 году окончил Московский педагогический государственный университет (специальность «История», квалификация «Учитель истории»).

🎓 В 2002 году окончил Московский педагогический государственный университет (специальность «Юриспруденция», квалификация «Юрист»).

🏫 В МГТУ им. Н.Э. Баумана с 2021 г.

☎️ +7 499-263-68-00

✉️ vu.zakharov@bmstu.ru""",

    'shs1_scientific_work': """_""",

    'shs2_scientific_work': """_""",

    'shs2_academic_work': """_""",

<<<<<<< HEAD
    'shs3_state': """_""",

    'shs3_head_of_dep': """_""",
=======
    'shs2_head_of_dep': """🔴 Заведущая кафедры:
Профессор кафедры, доктор социологических наук, профессор - Субочева Оксана Николаевна

🎓 Окончила отделение прикладной социологии философского факультета МГУ им. М.В. Ломоносова (1989 г.), а затем 
очную аспирантуру социологического факультета, успешно защитив кандидатскую диссертацию "Социальные факторы оптимизации 
межличностных отношений в трудовом коллективе".

🎓 В 2000 г. защитила докторскую диссертацию на тему "Межличностные отношения в системе управленческой 
деятельности производственной организации" в Академии труда и социальных отношений.

🎓 В 2003 г. присвоено ученое звание профессор по кафедре социологии и правоведения. 

🏫 В МГТУ им. Н.Э. Баумана с 2014 г.

✉️ subochevaon@bmstu.ru""",

    'shs3_head_of_dep': '''🔴 Заведующий кафедры:
Декан факультета социальных и гуманитарных наук, профессор, доктор философских наук - Ремарчук Валерий Николаевич

🎓 В 1976 году закончил с отличием Курганское высшее военно-политическое авиационное училище, в 1988 
военно-педагогический факультет Военно-политической академии им. В.И. Ленина по специальности «общественные науки».

🎓 Ученая степень доктора философских наук присуждена решением Высшей аттестационной комиссией 15 октября 1999. 
В 2006 году присвоено звание профессора. 

🏫 В МГТУ им. Н.Э. Баумана с 2000 г.

✉️ dekan.fsgn@bmstu.ru
''',
>>>>>>> b493983 (heads_of_dep & init_state_edit)

    'shs3_scientific_work': """_""",

    'shs3_academic_work': """_""",

<<<<<<< HEAD
    'shs4_state': """_""",

    'shs4_head_of_dep': """_""",

    'shs4_scientific_work': """_""",

    'shs4_academic_work': """_"""
=======
    'shs4_head_of_dep': '''🔴 Заведующий кафедры:
Доктор философских наук, профессор - Ивлев Виталий Юрьевич

🎓 В 1987 г. окончил философский факультет МГУ им. М.В. Ломоносова, асп. того же ф-та (1991).

🎓 В 1997 г. защитил кандидатскую диссертацию на тему "Методологический анализ категорий необходимости, случайности
и возможности".

🎓 В 2001 г. защитил докторскую диссертацию на тему "Оформление логического инструментария в истории Русской философии 
17-начала 18 веков".

✉️ ivlev@bmstu.ru
''',

    'shs4_scientific_work': """_""",

    'shs4_academic_work': """_""",
>>>>>>> b493983 (heads_of_dep & init_state_edit)
}

