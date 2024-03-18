from VkBotState import VkBotState
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotEventType


class VkBotStateHandler:
    def __init__(self, vk_bot):
        self.vk_bot = vk_bot

    def init_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=init_state_keyboard().get_keyboard(),
                message=MESSAGES['init_state'],
                attachment=self.vk_bot.attachments['init_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'SHS1':
                self.vk_bot.state = VkBotState.SHS1_STATE
                self.shs1_state_edit(event)
            elif event.object.payload.get('type') == 'SHS2':
                self.vk_bot.state = VkBotState.SHS2_STATE
                self.shs2_state_edit(event)
            elif event.object.payload.get('type') == 'SHS3':
                self.vk_bot.state = VkBotState.SHS3_STATE
                self.shs3_state_edit(event)
            elif event.object.payload.get('type') == 'SHS4':
                self.vk_bot.state = VkBotState.SHS4_STATE
                self.shs4_state_edit(event)
            elif event.object.payload.get('type') == 'DEANERY':
                self.deanery_clicked_handler(event)

    def init_state_edit(self, event):
        self.vk_bot.vk.messages.edit(
            peer_id=event.obj.peer_id,
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.vk_bot.attachments['init_state']
        )

    def shs1_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs1_keyboard().get_keyboard(),
                message=MESSAGES['shs1_state'],
                attachment=self.vk_bot.attachments['shs1_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'shs1_head_of_dep':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs1_head_of_dep'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs1_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs1_state']
                )
            elif event.object.payload.get('type') == 'shs1_scientific_work':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs1_scientific_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs1_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs1_state']
                )
            elif event.object.payload.get('type') == 'shs1_academic_work':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs1_academic_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs1_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs1_state']
                )
            elif event.object.payload.get('type') == 'back':
                self.vk_bot.state = VkBotState.INIT_STATE
                self.init_state_edit(event)

    def shs1_state_edit(self, event):
        self.vk_bot.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs1_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.attachments['shs1_state'],
            keyboard=shs1_keyboard().get_keyboard()
        )

    def shs2_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs2_keyboard().get_keyboard(),
                message=MESSAGES['shs2_state'],
                attachment=self.vk_bot.attachments['shs2_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'shs2_head_of_dep':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs2_head_of_dep'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs2_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs2_state']
                )
            elif event.object.payload.get('type') == 'shs2_scientific_work':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs2_scientific_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs2_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs2_state']
                )
            elif event.object.payload.get('type') == 'shs2_academic_work':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs2_academic_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs2_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs2_state']
                )
            elif event.object.payload.get('type') == 'back':
                self.vk_bot.state = VkBotState.INIT_STATE
                self.init_state_edit(event)
                self.init_state_handler(event)

    def shs2_state_edit(self, event):
        self.vk_bot.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs2_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.attachments['shs2_state'],
            keyboard=shs2_keyboard().get_keyboard()
        )

    def shs3_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=shs3_keyboard().get_keyboard(),
                message=MESSAGES['shs3_state'],
                attachment=self.vk_bot.attachments['shs3_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'shs3_head_of_dep':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs3_head_of_dep'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs3_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs3_state']
                )
            elif event.object.payload.get('type') == 'shs3_scientific_work':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs3_scientific_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs3_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs3_state']
                )
            elif event.object.payload.get('type') == 'shs2_academic_work':
                self.vk_bot.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs3_academic_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs3_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs3_state']
                )
            elif event.object.payload.get('type') == 'back':
                self.vk_bot.state = VkBotState.INIT_STATE
                self.init_state_edit(event)
                self.init_state_handler(event)

    def shs3_state_edit(self, event):
        self.vk_bot.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs3_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.attachments['shs3_state'],
            keyboard=shs3_keyboard().get_keyboard()
        )

    def shs4_state_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk_bot.messages.edit(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.peer_id,
                message=MESSAGES['shs4_state'],
                keyboard=shs4_keyboard().get_keyboard(),
                attachment=self.vk_bot.attachments['shs4_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'shs4_head_of_dep':
                self.vk_bot.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs4_head_of_dep'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs4_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs4_state']
                )
            elif event.object.payload.get('type') == 'shs4_scientific_work':
                self.vk_bot.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs4_scientific_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs4_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs4_state']
                )
            elif event.object.payload.get('type') == 'shs4_academic_work':
                self.vk_bot.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs4_academic_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=shs4_keyboard().get_keyboard(),
                    attachment=self.vk_bot.attachments['shs4_state']
                )
            elif event.object.payload.get('type') == 'back':
                self.vk_bot.state = VkBotState.INIT_STATE
                self.init_state_edit(event)
                self.init_state_handler(event)

    def shs4_state_edit(self, event):
        self.vk_bot.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs4_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.vk_bot.attachments['shs4_state'],
            keyboard=shs4_keyboard().get_keyboard()
        )

    def deanery_clicked_handler(self, event):
        self.vk_bot.vk.messages.edit(
            peer_id=event.obj.peer_id,
            message=MESSAGES['deanery'],
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.vk_bot.attachments['init_state']
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
прикладной информатики и социологии техники. ФСГН осуществляет глубокую гуманитарную подготовку студентов
во всём ВУЗе.\n
На факультете осваивают профессию студенты двух кафедр:\n
1. СГН2 «Социология и культурология»\n
2. СГН3 «Информационная аналитика и политические технологии»\n
🖌️ Основная особенность обучения на ФСГН состоит в совмещении социально-гуманитарных и технических наук.\n
Такое разностороннее развитие студентов открывает широкие возможности для их будущей карьеры.""",

    'shs1_state': """_""",

    'shs2_state': """_""",

    'shs1_academic_work': """_""",

    'shs1_head_of_dep': """_""",

    'shs1_scientific_work': """_""",

    'shs2_scientific_work': """_""",

    'shs2_head_of_dep': """_""",

    'shs2_academic_work': """_""",

    'shs3_state': """Кафедра занимается подготовкой кадров по направлению «Прикладная информатика».
Образовательной программой кафедры является «Информационная аналитика и политические технологии».
Здесь студентов учат не только информатике, программированию, но и аналитике данных.
Выпускники кафедры могут устроиться работать аналитиками данных в такие компании, как:
Яндекс, ВК, Сбер, Аналитический Центр при Правительстве РФ, ВТБ, РЖД, и прочие. """,

    'shs3_head_of_dep': """
🔴 Заведующий кафедры:
Декан факультета социальных и гуманитарных наук, профессор, доктор философских наук - Ремарчук Валерий Николаевич

🎓 В 1976 году закончил с отличием Курганское высшее военно-политическое авиационное училище, в 1988 
военно-педагогический факультет Военно-политической академии им. В.И. Ленина по специальности «общественные науки».

🎓 Ученая степень доктора философских наук присуждена решением Высшей аттестационной комиссией 15 октября 1999. 
В 2006 году присвоено звание профессора. 

🏫 В МГТУ им. Н.Э. Баумана с 2000 г.

✉️ dekan.fsgn@bmstu.ru
""",

    'shs3_scientific_work': """Кафедра была основана в 1963 году.
За это время, пройдя путь от научного педагогического становления в 1990 году, кафедра получила название «Политология».
В связи с открытием направления подготовки 09.03.03 «Прикладная информатика», профиль — информационная аналитика, 
кафедра получила название «Информационная аналитика и политические технологии». 

Теоретическую базу и практическую основу подготовки бакалавров в области информационной аналитики составляют:

6 дисциплин математического профиля;
13 дисциплин, посвящённых компьютерным технологиям;
около 40 дисциплин социально-гуманитарного профиля, раскрывающие сущности и технологии смысловой аналитической работы.

В гуманитарной сфере коллектив кафедры ведет активную работу по следующим научным направлениям:
1. Актуальные проблемы научной и научно-технической политики государства;
2. Политико-правовые основы политической системы современной России;
3. Политическая социализация молодёжи.

На кафедре работает дискуссионный студенческий клуб: «Ракурс» - руководитель Легчилин В.В.
В рамках деятельности клуба проходят встречи с интересными людьми: писателями, военными, ветеранами войны и труда, 
деятелями науки и культуры, а также посещения музеев ВС РФ, выставок, Государственной Думы, Совета Федерации и др.
Научная, учебно-воспитательная и методическая деятельность кафедры имеет интересную эволюцию. 
В 1965 году при кафедре была создана «Школа лектора международника», которая выросла в настоящий институт серьезной
профессиональной подготовки молодых лекторов, пропагандистов, будущих учёных. 
Основателем её был известный лектор, кандидат юридических наук, доцент Ни-Ли П.Н. С 1980 года школу возглавил
талантливый лектор Борисовский В.Н. 
В последующем школа обрела новое имя - Институт социально-политических технологий.
Его руководитель - к.ф.н., доцент Ореховский А.В.
В настоящее время данная структура называется дискуссионный клуб «Ракурс».
""",

    'shs3_academic_work': """не найдено.""",

    'shs4_state': """Кафедра СГН4 в основном нацелена на аспирантов Бауманки.\n
Она занимается подготовкой аспирантов по дисциплинам:\n,
1. «Социальная и политическая философия»\n
2. «Философия науки и техники».\n
Для студентов бакалавриата кафедра несёт исключительно преподавательский характер.\n
Преподаватели ведут такие дисциплины, как «Логика» и «Философия».""",

    'shs4_head_of_dep': """
🔴 Заведующий кафедры:
Доктор философских наук, профессор - Ивлев Виталий Юрьевич

🎓 В 1987 г. окончил философский факультет МГУ им. М.В. Ломоносова, асп. того же ф-та (1991).

🎓 В 1997 г. защитил кандидатскую диссертацию на тему "Методологический анализ категорий необходимости, случайности
и возможности".

🎓 В 2001 г. защитил докторскую диссертацию на тему "Оформление логического инструментария в истории Русской философии 
17-начала 18 веков".

✉️ ivlev@bmstu.ru
""",

    'shs4_scientific_work': """не найдено.""",

    'shs4_academic_work': """не найдено."""
}
