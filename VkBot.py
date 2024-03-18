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
Её преподавательский состав преподаёт дисциплину «История России» всем студентам Бауманки\n
Кафедра основана в 1959 г.\n
В процессе преподавания курса «История России» особое внимание уделяется вопросам истории науки и техники, инженерно
го дела, истории МГТУ.
Активно используются мультимедийные, интерактивные и информационные технологии. 
Организуются посещения музеев и исторических выставок, в т.ч. музея истории МГТУ.""",

    'shs2_state': """Кафедра занимается подготовкой кадров по направлению «Социалогия.» 
Образовательной программой данной кафедры является «Социалогия техники и инженерной деятельности».\n
Выпускники кафедры востребованы в таких местах, как:\n",
1. В органах государственной и муниципальной власти;\n",
2. В экспертных структурах и в информационно-аналитических центрах;\n",
3. В агентствах по найму и управлению персоналом;""",
    'shs1_head_of_dep':"""Заведующий кафедры:  доктор исторических наук, профессор Виталий Юрьевич Захаров\n
тел. 499-263-68-00  e-mail: vu.zakharov@bmstu.ru\n
Заместитель заведующего по учебно-методической работе Даниил Викторович Лобач,\n
тел. 499-263-65-42\n
Заместитель заведующего по научной работе Татьяна Романовна Суздалева,\n
тел. 499-263-65-42\n
Организационной работой занимается специалист по учебно-методической работе Ольга Александровна Мишина\n
Тел.: 499-263-65-42, e-mail: mishinaoa@bmstu.ru""",
    'shs1_scientific_work': '''Научная работа\n
Научная работа кафедры строится в соответствии с Перспективно-инновационным планом развития кафедры.\n

Кафедра поддерживает творческие связи с ведущими университетами страны и научными учреждениями Российской Академией 
Наук.\n

 Монографии и учебные пособия \n

2021\n

• История России. Под ред: Б. Н. Земцова. Изд-во МГТУ им. Н.Э. Баумана. 2021.\n

•  Земцов Б. Н.  Быковская, Г. А., Будрейко Е. Н. , Гвоздецкий В. Л. , Крылов А. О., Лобач Д. В. , Отрокова О.Ю. , 
Суздалева Т. Р. , Федоров К. В. История науки и техники России. Под ред: Б. Н. Земцова.. Изд-во МГТУ им. Н.Э. 
Баумана. 2021.\n

2019\n

• Земцов Б.Н. История отечественного государства и права Саратов: Ай Пи Эр Медиа, 2019. — 498 c.  Режим доступа: 
http://www.iprbookshop.ru/78221.html\n

• Земцов Б.Н. История отечественного государства и права: советский период (Учебник). СПб.: Изд – во Лань. 2018.
 — 214 с.\n

• Земцов Б.Н. История России. М.: Инфра-М. 2019. – 457 с. /250 с. (в соавторстве с Шубиным А.В., Данилевским И.Н.)\n

2017\n

• История ремесла, технических наук, и промышленности России в социальном контексте.Под ред. Б. Н. Земцова М.:
 Изд-во МГТУ им. Н.Э. Баумана, 2017. 204 с.\n

2014\n

• Российская империя XVIII — начала XX веков: формирование полиэтнического пространства. Учебное пособие под ред. 
Земцова Б.Н. М., МГТУ, 2014. – 89 с.\n

• Земцов Б.Н.  Philosophy and history of the Soviet right. Saarbrücken, 2014.\n

2013\n

• Земцов Б , А. Шубин А., Данилевский И..  История России для студентов технических ВУЗов. Учебное пособие. СПб., 
Питер, 2013\n

• Земцов Б.Н. История политических и правовых учений. М., МЭСИ, 2013.\n

•   Федоров К.В., Суздалева Т.Р., Давлетшина Н.В. Россия и мир во второй половине XX – начале XXI века: поиск 
модели развития. М., МГТУ, 2013.\n

2012\n

• Земцов Б.Н. История России с древнейших времен до начала XX века. Учебное пособие. М., Издательство IDO, 2012.\n

• История науки и техники. Учебное пособие. М., МГТУ, 2012 Электронный ресурс.\n

2011\n

• История науки и техники в России. В 3 Ч.  Под ред. К.В. Федорова, Б.Н. Земцова. – МГТУ, 2011. — 292 c.\n

•  Факультет «Социальные и гуманитарные науки» Московского государственного технического университета им. Н.Э. 
Баумана.    М., 2011. 128 с.\n

 2010\n

• Спецкурсы по Отечественной истории: Учебно-методическое пособие / Под ред. К.В. Федорова. М., МГТУ. 2010. 112 c.\n
''',
    'shs1_academic_work': '''Учебная работа\n
Кафедра представляет собой составную часть факультета «Социально-гуманитарные науки» (ФСГН). Главными целями 
преподавания является формирование у студентов:\n
-компетенций, позволяющих им самостоятельно анализировать современные социально-политические процессы в России и мире;\n
-способности разбираться в тенденциях исторического процесса,\n
-понимания места человека в историческом процессе,\n
-осознания влияния научно-технических процессов на развитие общества,\n
-практических навыков применения исторических знаний в повседневной жизни и инженерной деятельности.\n
На кафедре разработаны учебные программы для подготовки студентов всех уровней: бакалавриата, магистратуры и 
специалитета. Программы кафедры полностью соответствуют современным требованиям системы образования, состояния науки и 
профиля МГТУ им. Н.Э. Баумана.  Учебный процесс строится на основе модульно-рейтинговой системы. Активно используются 
инновационные обучающие технологии, современные методики преподавания истории, широко применяются современные 
технические средства обучения, разработаны эффективные методы контроля усвоения студентами курса кафедры.\n

В связи с присвоением в 2009 г. МГТУ им. Н.Э. Баумана статуса Федерального научно-исследовательского университета 
техники и технологии наряду с образовательными и воспитательными задачами приоритетным направлением работы кафедры 
«История» становится научно-исследовательская деятельность. На кафедре трудятся как уже известные ученые, получившие 
признание в России и за рубежом, так и талантливые перспективные ученые.''',
    'shs2_head_of_dep': '''Акимова Ирина Александровна

Заведующая кафедрой социологии и культурологии, кандидат философских наук, доцент
Образование:
МГУ им. М.В. Ломоносова, преподаватель философии

Научная и экспертная деятельность:
Член Ученого совета факультета социальных и гуманитарных наук МГТУ им Н.Э. Баумана.
Член комиссии «Лучший преподаватель МГТУ им. Н.Э. Баумана»
Член Российского общества социологов
Награждена Почетной грамотой Министерством образования и науки РФ

Ведет дисциплины:
Культурология, Социология коммуникаций

Персональная страница преподавателя на сайте университета:
https://bmstu.ru/ps/~akimova/

Электронная почта преподавателя:
akimova@bmstu.ru
''',
    'shs2_scientific_work': '''О кафедре
Багдасарьян Н.Г., доктор философских наук, профессор, зав. кафедрой в 1987-2006 гг.

Кафедра «Социологии и культурологии» появилась в МГТУ им. Н.Э. Баумана в 1987 г., на старте постсоветского этапа жизни Отечества. Она стала первой в технических вузах России кафедрой, чья учебная деятельность направлялась на принципиально неидеологическую сферу социально-гуманитарного знания. Бесспорное лидерство кафедры было обеспечено разработкой уникальной структуры и логики учебного курса культурологии, нашедших отражение в коллективном учебнике для технических вузов. Он, выдержав несколько изданий, стал образцом для сотни профильных вузов. Позже, в издательстве «Юрайт» вышли новые издания учебников «Культурология» и «Социология», представляющие собой современные учебно-методические комплексы дисциплин. Их особенность – в сочетании институционального и культурологического подходов к анализу социальных явлений. Ежегодное массовое переиздание учебников свидетельствует об их высокой востребованности.

Интеллектуальный потенциал и профессиональные навыки преподавателей, осваивающих никогда прежде не существовавшие дисциплины, обеспечили решение сложнейшей задачи - институционализации социогуманитарной компоненты инженерного образования.

Акимова И.А., кандидат философских наук, доцент, зав. кафедрой с 2006 г. по н.в.

В 2016 г. кафедра одной из первых в системе высшего технического образования, начала подготовку специалистов-социологов в предметной области социологии техники и технологий. Открыто обучение бакалавров по программе «Социология техники и инженерной деятельности» и магистров по программе «Социальный анализ технологических инноваций и рисков». Это новые и перспективные междисциплинарные программы подготовки специалистов для изучения, объяснения и понимания проблем современной техносферы, что требует углубленных знаний социологии техники, информационных систем и цифровых технологий.

В рамках международной образовательной и исследовательской кооперации по инициативе кафедры был заключен договор о сотрудничестве с одним из старейших вузов Европы – Технологическим институтом г. Карлсруэ (Германия) – KIT. Плотная работа ведется с его структурным подразделением – Институтом оценки технологий и системного анализа – ITAS, принявшего наших студентов на стажировку, в рамках которой они посетили бюро по оценке технологий при Бундестаге (TAB).


Качество образовательного процесса обеспечивает высококвалифицированный состав преподавателей – доктора и кандидаты наук, в том числе PhD, профессора и доценты, а также специалисты-практики, сочетающие молодость и зрелость, большой опыт и инициативу, исследовательский потенциал и интерес к своей работе.


''',
    'shs2_academic_work': '''С 2016 году на кафедре была открыта специальность 39.03.01 «Социология» - подготовка бакалавра (профиль «Социология техники и инженерной деятельности»). В 2020 году состоялся первый выпуск.


Студенты кафедры принимают активное участие в научной жизни кафедры, университета, страны: ежегодно участвуют в конференции «Студенческая весна», Всероссийском форуме научной молодежи «Богатство России», Всероссийском конкурсе научно-исследовательских работ в области инженерных и гуманитарных наук, Всероссийской инновационной молодежной научно-инженерной выставке «Политехника», занимая почетные призовые места.


В 2020 году на кафедре открыта магистратура по направлению подготовки 39.04.01 «Социология»'''
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
                self.shs1_state_edit(event)#для избежания вечного редактирования сообщения вынес в отдельный метод
                self.shs1_clicked_handler(event)

            elif event.object.payload.get('type') == 'SHS2':

                self.state = VkBotState.SHS2_CLICKED
                self.shs2_state_edit(event)#аналогично
                self.shs2_clicked_handler(event)

            elif event.object.payload.get('type') == 'SHS3':

                self.state = VkBotState.SHS3_CLICKED
                self.shs3_clicked_handler(event)

            elif event.object.payload.get('type') == 'SHS4':

                self.state = VkBotState.SHS4_CLICKED
                self.shs4_clicked_handler(event)

            elif event.object.payload.get('type') == 'DEANERY':

                self.deanery_clicked_handler(event)

    def shs1_keyboard(self):
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

    def shs2_keyboard(self):
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

    def back_keyboard(self):
        #клавиатура, если требуется чтобы из условной вкладки "Заведующий кафедрой" можно было бы перейти только в иннит
        keyboard = VkKeyboard(one_time=False, inline=True)
        keyboard.add_callback_button(
            label="Назад",
            color=VkKeyboardColor.NEGATIVE,
            payload={"type": "back"}
        )
        return keyboard
    def shs1_state_edit(self, event):
        self.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs1_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.attachments['shs1_state'],
            keyboard=self.shs1_keyboard().get_keyboard()
        )

    def shs2_state_edit(self, event):
        self.vk.messages.edit(
            peer_id=event.object.peer_id,
            message=MESSAGES['shs2_state'],
            conversation_message_id=event.obj.conversation_message_id,
            attachment=self.attachments['shs2_state'],
            keyboard=self.shs2_keyboard().get_keyboard()
        )

    def init_state_edit(self,event):
        self.vk.messages.edit(
            peer_id=event.obj.peer_id,
            message='сгн3 рулит!',
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.attachments['init_state']
        )

    def shs1_clicked_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=self.shs1_keyboard().get_keyboard(),
                message=MESSAGES['shs1_state'],
                attachment=self.attachments['shs1_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'shs1_head_of_dep':
                last_id = self.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs1_head_of_dep'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=self.shs1_keyboard().get_keyboard(),
                    attachment=self.attachments['shs1_state']
                )
            elif event.object.payload.get('type') == 'shs1_scientific_work':
                last_id = self.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs1_scientific_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=self.shs1_keyboard().get_keyboard(),
                    attachment=self.attachments['shs1_state']
                )
            elif event.object.payload.get('type') == 'shs1_academic_work':
                last_id = self.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs1_academic_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=self.shs1_keyboard().get_keyboard(),
                    attachment=self.attachments['shs1_state']
                )
            elif event.object.payload.get('type') == 'back':

                self.state = VkBotState.INIT_STATE
                self.init_state_edit(event)
                self.init_state_handler(event)

    def shs2_clicked_handler(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            self.vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                peer_id=event.obj.message['from_id'],
                keyboard=self.shs2_keyboard().get_keyboard(),
                message=MESSAGES['shs2_state'],
                attachment=self.attachments['shs2_state']
            )
        elif event.type == VkBotEventType.MESSAGE_EVENT:
            if event.object.payload.get('type') == 'shs2_head_of_dep':
                last_id = self.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs2_head_of_dep'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=self.shs2_keyboard().get_keyboard(),
                    attachment=self.attachments['shs2_state']
                )
            elif event.object.payload.get('type') == 'shs2_scientific_work':
                last_id = self.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs2_scientific_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=self.shs2_keyboard().get_keyboard(),
                    attachment=self.attachments['shs2_state']
                )
            elif event.object.payload.get('type') == 'shs2_academic_work':
                last_id = self.vk.messages.edit(
                    peer_id=event.obj.peer_id,
                    message=MESSAGES['shs2_academic_work'],
                    conversation_message_id=event.obj.conversation_message_id,
                    keyboard=self.shs2_keyboard().get_keyboard(),
                    attachment=self.attachments['shs2_state']
                )
            elif event.object.payload.get('type') == 'back':

                self.state = VkBotState.INIT_STATE
                self.init_state_edit(event)
                self.init_state_handler(event)

    def shs3_clicked_handler(self, event):
        pass

    def shs4_clicked_handler(self, event):
        pass

    def deanery_clicked_handler(self, event):
        last_id = self.vk.messages.edit(
            peer_id=event.obj.peer_id,
            message=MESSAGES['init_state'],
            conversation_message_id=event.obj.conversation_message_id,
            keyboard=init_state_keyboard().get_keyboard(),
            attachment=self.attachments['init_state']
        )
