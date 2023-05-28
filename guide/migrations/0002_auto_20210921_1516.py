from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import migrations

from datetime import datetime, timedelta
import time

def new_tetstask(apps, schema_editor):
    user = User.objects.create_superuser(username='root', email='manual280523@mail.ru', password='SsNn5678+-@')
    managers = Group.objects.get_or_create(name = 'Managers')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    print("Суперпользователь создан")

    user = User.objects.create_user(username='manager', password='Ss0066+-')
    my_group = Group.objects.get(name='Managers')    
    my_group.user_set.add(user)
    print("Менеджер создан")

    # Простые пользователи (заявители) id3-27
    user = User.objects.create_user(username='user1', password='Uu0066+-', email='user1@mail.ru', first_name='Асхат', last_name='Бекназар', last_login=datetime.now())
    user = User.objects.create_user(username='user2', password='Uu0066+-', email='user2@mail.ru', first_name='Владислав', last_name='Канавец', last_login=datetime.now())
    user = User.objects.create_user(username='user3', password='Uu0066+-', email='user3@mail.ru', first_name='Шадияр', last_name='Иманов', last_login=datetime.now())
    user = User.objects.create_user(username='user4', password='Uu0066+-', email='user4@mail.ru', first_name='Игорь', last_name='Костылев', last_login=datetime.now())
    user = User.objects.create_user(username='user5', password='Uu0066+-', email='user5@mail.ru', first_name='Сабыр', last_name='Темиржанов', last_login=datetime.now())
    user = User.objects.create_user(username='user6', password='Uu0066+-', email='user6@mail.ru', first_name='Тлеген ', last_name='Жангалиев', last_login=datetime.now())
    user = User.objects.create_user(username='user7', password='Uu0066+-', email='user7@mail.ru', first_name='Расыл ', last_name='Турдыкожанов', last_login=datetime.now())
    user = User.objects.create_user(username='user8', password='Uu0066+-', email='user8@mail.ru', first_name='Владислав', last_name='Пилипенко', last_login=datetime.now())
    user = User.objects.create_user(username='user9', password='Uu0066+-', email='user9@mail.ru', first_name='Владислав', last_name='Елизаров', last_login=datetime.now())
    user = User.objects.create_user(username='user10', password='Uu0066+-', email='user10@mail.ru', first_name='Адиль', last_name='Малтуганов', last_login=datetime.now())
    print("Пользователи созданы")

    Category = apps.get_model("guide", "Category")

    category = Category()
    category.id = 1
    category.title = 'Основы Информационной безопасности'   
    category.save()
    print("Категории созданы")

    # Тестовые задания и вопросы к ним#
    
    Teststask = apps.get_model("guide", "Teststask")
    Question = apps.get_model("guide", "Question")

    ##########

    teststask = Teststask()
    teststask.id = 1
    teststask.category_id = 1
    teststask.title = 'Тест №1'
    teststask.details = 'Техника безопасности - тест №1'
    teststask.minutes = 10
    teststask.limit = 80
    teststask.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'На работах с повышенной опасностью работники проходят обучение и проверку знаний по вопросам охраны труда:'
    question.reply1 = 'До начала выполнения должностных обязанностей и в дальнейшем один раз в год.'
    question.ok1 = True
    question.reply2 = 'Периодически раз в 3 года.'
    question.ok2 = False
    question.reply3 = 'Периодически раз в 5 лет.'
    question.ok3 = False
    question.reply4 = 'По указанию администрации.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
        
    question = Question()
    question.teststask = teststask
    question.question = 'Вводный инструктаж по охране труда с вновь принятыми работниками проводит:'
    question.reply1 = 'Сотрудник отдела кадров.'
    question.ok1 = False
    question.reply2 = 'Специалист по охране труда.'
    question.ok2 = True
    question.reply3 = 'Непосредственный руководитель.'
    question.ok3 = False
    question.reply4 = 'Председатель профкома.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Повторный инструктаж по охране труда на работах без повышенной опасности проводится один раз:'
    question.reply1 = ' В месяц.'
    question.ok1 = False
    question.reply2 = 'На квартал.'
    question.ok2 = False
    question.reply3 = 'В полугодие.'
    question.ok3 = True
    question.reply4 = 'По указанию государственного инспектора.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'Инструктаж студентов по охране труда при проведении лабораторных работ проводит:'
    question.reply1 = 'Преподаватель'
    question.ok1 = True
    question.reply2 = 'Инженер по охране труда'
    question.ok2 = False
    question.reply3 = 'Ст. лаборант.'
    question.ok3 = False
    question.reply4 = 'Куратор.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Когда проводится целевой инструктаж по охране труда?'
    question.reply1 = 'При переводе работника из одного цеха в другой.'
    question.ok1 = False
    question.reply2 = 'При изменении технологии или после несчастного случая.'
    question.ok2 = False
    question.reply3 = 'После выхода из перерыва.'
    question.ok3 = False
    question.reply4 = 'При направлении на выполнение разовой или временной работы.'
    question.ok4 = True
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Кто может отменить предписание специалиста по охране труда?'
    question.reply1 = 'Руководитель предприятия.'
    question.ok1 = True
    question.reply2 = 'Профсоюзный комитет.'
    question.ok2 = False
    question.reply3 = 'Суд.'
    question.ok3 = False
    question.reply4 = 'Прокуратура.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'Кем осуществляется расследование несчастных случаев на производстве?'
    question.reply1 = 'Отделом охраны труда.'
    question.ok1 = False
    question.reply2 = 'Комиссией, назначенной руководителем предприятия'
    question.ok2 = True
    question.reply3 = 'Инспектором Госгорпромнадзора.'
    question.ok3 = False
    question.reply4 = 'Профсоюзным комитетом.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'После какого срока комиссия должна составить акт о несчастном случае на производстве по форме Н-1?'
    question.reply1 = 'Трое суток.'
    question.ok1 = True
    question.reply2 = 'Одни сутки.'
    question.ok2 = False
    question.reply3 = 'После окончания расследования.'
    question.ok3 = False
    question.reply4 = 'Определяет руководитель.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Расследуется несчастный случай, о котором пострадавший своевременно не сообщил?'
    question.reply1 = 'не расследуется.'
    question.ok1 = False
    question.reply2 = 'Расследуется, если с момента происшествия прошло не более одного месяца.'
    question.ok2 = False
    question.reply3 = 'Расследуется по заявлению потерпевшего.'
    question.ok3 = True
    question.reply4 = 'В случае смерти потерпевшего.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'В каком размере предприятие платит штраф в случае установления попытки сокрытия работодателем несчастного случая?'
    question.reply1 = 'В 5-кратном размере.'
    question.ok1 = False
    question.reply2 = 'В 20-кратном размере.'
    question.ok2 = False
    question.reply3 = 'В 10-кратном размере.'
    question.ok3 = True
    question.reply4 = 'В 15-кратном размере.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'В каком случае выносится постановление о наложении штрафа на предприятие?'
    question.reply1 = 'По итогам комплексной проверки состояния охраны труда предприятия'
    question.ok1 = True
    question.reply2 = 'По итогам проверки инспектором Госгорпромнадзора.'
    question.ok2 = False
    question.reply3 = 'По решению трудового коллектива'
    question.ok3 = False
    question.reply4 = 'по итогам министерской проверке'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    ##########

    teststask = Teststask()
    teststask.id = 2
    teststask.category_id = 1
    teststask.title = 'Тест №2'
    teststask.details = 'Техника безопасности - тест №2'
    teststask.minutes = 10
    teststask.limit = 80
    teststask.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Кто обеспечивает выполнение мероприятий по созданию здоровых и безопасных условий труда, соблюдения противопожарного режима во время проведения: аудиторных занятий, в лабораториях, мастерских и др.?'
    question.reply1 = 'Проректор по учебной работе.'
    question.ok1 = True
    question.reply2 = 'Проректор по административно-хозяйственной работе.'
    question.ok2 = False
    question.reply3 = 'Отдел охраны труда.'
    question.ok3 = False
    question.reply4 = 'Студенческий профком.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Кто в высшем учебном заведении составляет заявки на спецодежду и другие средства индивидуальной защиты?'
    question.reply1 = 'Зав. кафедрой.'
    question.ok1 = True
    question.reply2 = 'Инженер по охране труда.'
    question.ok2 = False
    question.reply3 = 'Заведующий хозяйством.'
    question.ok3 = False
    question.reply4 = 'Заведующий складом.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Кто подтверждает (устанавливает) право работников на льготное пенсионное обеспечение, дополнительный отпуск, сокращенный рабочий день?'
    question.reply1 = 'Отдел охраны труда.'
    question.ok1 = False
    question.reply2 = 'Профком предприятия.'
    question.ok2 = False
    question.reply3 = 'Комиссия по аттестации рабочих мест.'
    question.ok3 = True
    question.reply4 = 'Органы соцстраха.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'На предприятиях, применяющих в работе радиоактивные вещества, контроль облучения его персонала осуществляется:'
    question.reply1 = 'Городской СЭС.'
    question.ok1 = False
    question.reply2 = 'Службой радиационной безопасности предприятия.'
    question.ok2 = True
    question.reply3 = 'Службой охраны труда предприятия.'
    question.ok3 = False
    question.reply4 = 'Специалистом гражданской обороны.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'С увеличением силы тока, проходящего через тело человека, поражения человека:'
    question.reply1 = 'Уменьшается.'
    question.ok1 = False
    question.reply2 = 'Не изменяется.'
    question.ok2 = False
    question.reply3 = 'Когда как.'
    question.ok3 = False
    question.reply4 = 'Увеличивается.'
    question.ok4 = True
    question.reply5 = 'True'
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'Защитное заземление или зануление обеспечивает:'
    question.reply1 = 'Защиту человека от поражения электрическим ударом.'
    question.ok1 = True
    question.reply2 = 'Защиту оборудования от короткого замыкания.'
    question.ok2 = False
    question.reply3 = 'Защиту помещения от удара молнии.'
    question.ok3 = False
    question.reply4 = 'Защита от коррозии оборудования'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'На какие классы по степени опасности поражения электрическим током помещения подразделяются:'
    question.reply1 = 'Влажные, пылевые, взрывоопасные.'
    question.ok1 = False
    question.reply2 = 'Без повышенной опасности, с повышенной опасностью, особо опасные. '
    question.ok2 = True
    question.reply3 = 'Заземлены, незаземленные, занулении.'
    question.ok3 = False
    question.reply4 = 'Опасные, не опасные, очень опасные'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'Электротехническому персоналу после обучения и экзаменов по вопросам электробезопасности:'
    question.reply1 = 'Выдается диплом электромонтера.'
    question.ok1 = False
    question.reply2 = 'Присваивается квалификационный разряд.'
    question.ok2 = False
    question.reply3 = 'Присваивается группа по электробезопасности. '
    question.ok3 = True
    question.reply4 = 'Предоставляется право самостоятельного обслуживания электроустановки.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Средства защиты от опасных факторов: ограждения, предупредительная сигнализация, блокировочные устройства, защитные экраны, ограничители и предохранители называются:'
    question.reply1 = 'Коллективными. '
    question.ok1 = True
    question.reply2 = 'Индивидуальными.'
    question.ok2 = False
    question.reply3 = 'Основными.'
    question.ok3 = False
    question.reply4 = 'Обязательными.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Назовите санитарные нормы для учебных помещений зимой (влажность, температура, скорость движения воздуха):'
    question.reply1 = '40-60%, 16-18С, 02,-0,5 м/с '
    question.ok1 = True
    question.reply2 = '70-80%, 22-25 С, 1-2 м/с'
    question.ok2 = False
    question.reply3 = '20-30%, 10-15 С, 0,05-0,1 м/с'
    question.ok3 = False
    question.reply4 = '50-70%, 18-19 С, 0,7-1 м/с'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    ##########

    teststask = Teststask()
    teststask.id = 3
    teststask.category_id = 1
    teststask.title = 'Тест №3'
    teststask.details = 'Техника безопасности - тест №3'
    teststask.minutes = 10
    teststask.limit = 80
    teststask.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Предварительные медицинские осмотры (при приеме на работу) и обязательные периодические медицинские осмотры (в течение трудовой деятельности) проводятся для:'
    question.reply1 = 'Работников со слабым здоровьем.'
    question.ok1 = False
    question.reply2 = 'Работников занятых на вредных и опасных работах, и там где необходимо специальный профессиональный отбор.'
    question.ok2 = True
    question.reply3 = 'Всех работников.'
    question.ok3 = False
    question.reply4 = 'Лиц, состоящих на диспансерном учете.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Назовите нормы освещения в аудитории (лаборатории): на доске, на рабочем столе, в комнате преподавателей?'
    question.reply1 = '0500 лк, 300 лк, 200 лк.'
    question.ok1 = True
    question.reply2 = '200 лк, 100 лк, 50 лк.'
    question.ok2 = False
    question.reply3 = '1000 лк, 600 лк, 300 лк.'
    question.ok3 = False
    question.reply4 = 'В зависимости от количества ламп.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Первая помощь при ранении — остановить кровотечение, предотвратить заражение, для чего необходимо:'
    question.reply1 = 'Промыть рану водой и перевязать.'
    question.ok1 = False
    question.reply2 = 'Засыпать рану порошком и заклеить клеем.'
    question.ok2 = False
    question.reply3 = 'Рану обработать спиртосодержащим раствором и наложить повязку. '
    question.ok3 = True
    question.reply4 = 'Протереть рану тканью и оставить открытой.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()

    question = Question()
    question.teststask = teststask
    question.question = 'Части производственного оборудования, которые могут стать источником опасных и (или) вредных факторов окрашиваются в:'
    question.reply1 = 'Красный цвет.'
    question.ok1 = False
    question.reply2 = 'Черно-белый цвет.'
    question.ok2 = False
    question.reply3 = 'Зеленый цвет'
    question.ok3 = False
    question.reply4 = 'Желтый цвет.'
    question.ok4 = True
    question.reply5 = ''
    question.ok5 = False
    question.save()
 
    question = Question()
    question.teststask = teststask
    question.question = 'Утечки воздуха через щели в: окнах, дверях, перекрытиях называется:'
    question.reply1 = 'Аэрация.'
    question.ok1 = False
    question.reply2 = 'Инфильтрация.'
    question.ok2 = True
    question.reply3 = 'Конвекция.'
    question.ok3 = False
    question.reply4 = 'Сквозняк.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    question = Question()
    question.teststask = teststask
    question.question = 'Назовите критический уровень кислорода в воздухе во время пожара, ниже которого является угроза жизни человека?'
    question.reply1 = ' 14%.'
    question.ok1 = True
    question.reply2 = '12%.'
    question.ok2 = False
    question.reply3 = '10%.'
    question.ok3 = False
    question.reply4 = '5%.'
    question.ok4 = False
    question.reply5 = ''
    question.ok5 = False
    question.save()
    
    #question = Question()
    #question.teststask = teststask
    #question.question = ''
    #question.reply1 = ''
    #question.ok1 = False
    #question.reply2 = ''
    #question.ok2 = False
    #question.reply3 = ''
    #question.ok3 = False
    #question.reply4 = ''
    #question.ok4 = False
    #question.reply5 = ''
    #question.ok5 = False
    #question.save()

    print("Тестовые задания созданы")
    print("Вопросы к тестовым заданиям созданы")

    # Протокол
    
    Protocol = apps.get_model("guide", "Protocol")

    protocol = Protocol()
    protocol.teststask_id = 1
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 10, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 11
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=10);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 2
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 10, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 12
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=9);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 1
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 10, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 3
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=8);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 2
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 90
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 90, (90.0 %). Тестовое задание завершено'
    protocol.user_id = 4
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=8);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 3
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 6. Отвечено вопросов: 6. Правильно отвечено: 6, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 5
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=6);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 1
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 10, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 6
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=10);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 2
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 80
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 8, (80.0 %). Тестовое задание завершено'
    protocol.user_id = 7
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=9);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 1
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 10, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 8
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=8);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 2
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 90
    protocol.details = 'Всего вопросов: 10. Отвечено вопросов: 10. Правильно отвечено: 9, (90.0 %). Тестовое задание завершено'
    protocol.user_id = 9
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=8);
    protocol.save()

    protocol = Protocol()
    protocol.teststask_id = 3
    #protocol.datep = datetime.now() - timedelta(days=25);
    protocol.result = 100
    protocol.details = 'Всего вопросов: 6. Отвечено вопросов: 6. Правильно отвечено: 6, (100.0 %). Тестовое задание завершено'
    protocol.user_id = 10
    protocol.save()
    protocol.datep = datetime.now() - timedelta(days=6);
    protocol.save()

    print("Пртокол создан")
   
class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(new_tetstask),
    ]
