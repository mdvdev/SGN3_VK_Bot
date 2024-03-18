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
    прикладной информатики и социологии техники. ФСГН осуществляет глубокую гуманитарную подготовку студентов
    во всём ВУЗе.\n
    На факультете осваивают профессию студенты двух кафедр:\n
    1. СГН2 «Социология и культурология»\n
    2. СГН3 «Информационная аналитика и политические технологии»\n
    🖌️ Основная особенность обучения на ФСГН состоит в совмещении социально-гуманитарных и технических наук.\n
    Такое разностороннее развитие студентов открывает широкие возможности для их будущей карьеры.""",

    'shs1_state': """
    ⚪️ основана в 1959 году;
    ⚪️ преподаёт курс «История» на всех факультетах МГТУ;
    ⚪️ особое внимание уделяется вопросам истории науки и техники, истории университета;
    ⚪️ занимается организацией посещения исторических музеев и выставок.""",

    'shs2_state': """
    ⚪️ основана в 1987 году;
    ⚪️ осуществляет подготовку специалистов-социологов;
    ⚪️ открыто обучение бакалавров по программе «Социология техники и инженерной деятельности» и магистров по программе 
    «Социальный анализ технологических инноваций и рисков»;
    ⚪️ сотрудничает с одним из старейших вузов Европы — Технологическим институтом г. Карлсруэ (Германия) — KIT.""",

    'shs1_academic_work': """Учебная деятельность:\n
    📚 На кафедре разработаны учебные программы для подготовки студентов всех уровней: бакалавриата, магистратуры и специалитета. 
    Программы кафедры полностью соответствуют современным требованиям системы образования, состояния науки и профиля МГТУ им. Н.Э. Баумана.\n
    Главными целями преподавания является формирование у студентов:
    * компетенций, позволяющих им самостоятельно анализировать современные социально-политические процессы в России и мире;
    * способности разбираться в тенденциях исторического процесса,
    * понимания места человека в историческом процессе,
    * осознания влияния научно-технических процессов на развитие общества,
    * практических навыков применения исторических знаний в повседневной жизни и инженерной деятельности."""

    'shs1_head_of_dep': """📎 Кафедра СГН1
    «История»""",

    'shs1_scientific_work': """Научная деятельность:\n
    🔍 Научная работа СГН1 строится в соответствии с Перспективно-инновационным планом развития кафедры.
    Кафедра поддерживает творческие связи с ведущими университетами страны и научными учреждениями Российской Академией Наук. 
    Издано множество монографий и учебных пособий по дисциплине истории.""",

    'shs2_scientific_work': """Научная деятельность:\n
    🔍 Социологические исследования на кафедре велись с первых месяцев ее основания. Первоначально опросы проводила инициативная группа студентов-бауманцев, 
    которая анкетировала молодежь по самым разным направлениям. 
    Мониторинговые программы «Абитуриент» и «Пятикурсник» способствовали осмыслению интенсивных перемен в стране и высшей школе, а также корректировке учебных курсов.
    На сегодняшний день регулярно проводят социологические исследования д.с.н., профессор Субочева О.Н., к.с.н, доцент Семина М.В., к.пс.н., доцент Малолетнева И.В.""",

    'shs2_head_of_dep': """📎 Кафедра СГН2 
    «Социология и культурология»""",

    'shs2_academic_work': """Учебная деятельность:\n
    📚 В 2016 г. кафедра одной из первых в системе высшего технического образования, начала подготовку специалистов-социологов в предметной области социологии техники и технологий. 
    Она стала первой в технических вузах России кафедрой, чья учебная деятельность направлялась на принципиально неидеологическую сферу социально-гуманитарного знания На кафедре осуществляется 
    обучение бакалавров и магистров по новым и перспективным междисциплинарным программам.""",

    'shs3_state': """
    ⚪️ основана в 1963 году;
    ⚪️ готовит специалистов-аналитиков, успешно справляющихся с проектированием информационно-аналитических систем и и созданием прикладных программных продуктов;
    ⚪️ открыто обучение бакалавров по программе «Информационная аналитика» и магистров по программе «Информационно-аналитические технологии в системе социального управления»;
    ⚪️ занимается исследованием проблем информационного влияния на общества, изучением аналитики как инструмент исследования и управления информационным обществом.""",

    'shs3_head_of_dep': """📎 Кафедра СГН3
    «Информационная аналитика и политические технологии»""",

    'shs3_scientific_work': """Научная деятельность:\n
    🔍 Коллектив кафедры ведет активную работу по следующим научным направлениям:
    * Актуальные проблемы научной и научно-технической политики государства;
    * Политико-правовые основы политической системы современной России;
    * Политическая социализация молодёжи.\n
    Проводятся ежегодные студенческие научные конференции, научно-методические семинары.\n
    В 1965 году при кафедре была создана «Школа лектора международника», которая выросла в настоящий институт серьезной профессиональной подготовки молодых лекторов, 
    пропагандистов, будущих учёных.""",

    'shs3_academic_work': """Учебная деятельность:\n
    📚 Подготовка выпускников ведется на стыке трех научно-инженерных областей: исследование социальных процессов, освоение математических методов информационного анализа и разработка прикладных информационно-аналитических программных продуктов.  
    Кафедра ставит своей целью выпуск специалистов - носителей высокой инновационной технологической культуры, способных не только к самостоятельной работе, но и к эффективному управлению творческими коллективами в государственных структурах, 
    науке и наукоемком производстве.""",

    'shs4_state': """📎 Кафедра СГН4
    «Философия»\n
    ⚪️ основана в 1958 году;
    ⚪️ осуществляет глубокую подготовку студентов университета по дисциплинам «Философия», «Логика», «Методология научного познания», «История и философия науки», «Теория и практика аргументации», «Психология и педагогика»;
    ⚪️ выпускает аспирантов по специальностям «Философия науки и техники», «Социальная и политическая философия».""",

    'shs4_head_of_dep': """📎 Кафедра СГН4
    «Философия»""",

    'shs4_scientific_work': """Научная деятельность:\n
    🔍 Кафедра СГН4 в рамках Международного симпозиума «Уникальные феномены и универсальные ценности культуры» проводит множество научных конференций.
    Под руководством и редакцией профессора В.В.Ильина подготовлен и опубликован ряд трудов по актуальной философской проблематике с участием большинства 
    преподавателей кафедры, в том числе «Философия в системе культуры. Исторические типы философии».\n
    Направления научных исследований:
    * философия;
    * методология научного познания;
    * логика и т.д.""",

    'shs4_academic_work': """Учебная деятельность:\n
    📚 СГН4 ведёт подготовку аспирантов по дисциплинам социальная и политическая философия, философия науки и техники. 
    На кафедре был разработан новый курс, включающий историко-философское введение и современную философскую проблематику, а также спецкурсы по выбору, учитывающие индивидуальные интересы студентов. 
    Реализации новых задач способствовала организация научно-теоретических и методических семинаров для преподавателй кафедры с приглашением ведущих специалистов из МГУ им.Ломоносова, Института философии РАН и др."""
}

