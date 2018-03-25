import requests
import time

url = 'http://localhost:8000/localityadd/'

names = ['Абрамовка',
         # 'Автономовка',
         # 'Актай',
         # 'Албазинка',
         # 'Албазино',
         # 'Алгач',
         # 'Александровка',
         # 'Алексеевка',
         # 'Алексеевка',
         # 'Алексеевка',
         # 'Амаранка',
         # 'Амуро-Балтийское',
         # 'Амурское',
         # 'Амуткачи',
         # 'Ангарич',
         # 'Андреевка',
         # 'Анновка',
         # 'Аносово',
         # 'Аносовский',
         # 'Антоновка',
         # 'Антоновка',
         # 'Апрельский',
         # 'Арга',
         # 'Арсентьевка',
         # 'Архара',
         # 'Асташиха',
         # 'Аяк',
         # 'Базисная',
         # 'Бам',
         # 'Бахирево',
         # 'Безозерный',
         # 'Бейтоново',
         # 'Беленькая',
         # 'Беловеж',
         # 'Белогорка',
         # 'Белогорск',
         # 'Белогорье',
         # 'Белоцерковка',
         # 'Белоярово',
         # 'Белый Яр',
         # 'Беляковка',
         # 'Березники',
         # 'Березовка',
         # 'Березовка',
         # 'Берея',
         # 'Бибиково',
         # 'Бичура',
         # 'Благовещенск',
         # 'Богородское',
         # 'Богословка',
         # 'Богучан',
         # 'Болдыревка',
         # 'Большая Омутная',
         # 'Большая Сазанка',
         # 'Большеозерка',
         # 'Бомнак',
         # 'Борисово',
         # 'Борисоглебка',
         # 'Борисполь',
         # 'Бочкаревка',
         # 'Братолюбовка',
         # 'Бугорки',
         # 'Бур',
         # 'Бурея',
         # 'Буринда',
         # 'Буссе',
         # 'Бысса',
         # 'Валуево',
         # 'Варваровка',
         # 'Васильевка',
         # 'Васильки',
         # 'Введеновка',
         # 'Великокнязевка',
         # 'Верное',
         # 'Верхнезейск',
         # 'Верхнеполтавка',
         # 'Верхний',
         # 'Верхний Уртуй',
         # 'Верхняя Ларба',
         # 'Веселая',
         # 'Веселое',
         # 'Веселый',
         # 'Винниково',
         # 'Виноградовка',
         # 'Водораздельное',
         # 'Возжаевка',
         # 'Вознесеновка',
         # 'Войково',
         # 'Волково',
         # 'Вольное',
         # 'Вольный',
         # 'Воробьевка',
         # 'Воронжа',
         # 'Воскресеновка',
         # 'Воскресеновка',
         # 'Восточная Нива',
         # 'Восточный',
         # 'Высокий',
         # 'Высокое',
         # 'Высокое',
         # 'Гарь',
         # 'Георгиевка',
         # 'Гильчин',
         # 'Глубокий',
         # 'Глухари',
         # 'Голубая',
         # 'Гомелевка',
         # 'Гонжа',
         # 'Горный',
         # 'Грибовка',
         # 'Грибское',
         # 'Гродеково',
         # 'Грязнушка',
         # 'Гудачи',
         # 'Гулик',
         # 'Гуликовка',
         # 'Гуран',
         # 'Дактуй',
         # 'Дальневосточный',
         # 'Дамбуки',
         # 'Даниловка',
         # 'Демьяновка',
         # 'Державинка',
         # 'Джалинда',
         # 'Джатва',
         # 'Джелтулак',
         # 'Джиктанда',
         # 'Дим',
         # 'Дипкун',
         # 'Дмитриевка',
         # 'Дмитриевка',
         # 'Дмитриевка',
         # 'Добрянка',
         # 'Домикан',
         # 'Дорожный',
         # 'Дубовка',
         # 'Дубовка',
         # 'Дубовое',
         # 'Дугда',
         # 'Духовское',
         # 'Егорьевка',
         # 'Екатеринославка',
         # 'Ерахта',
         # 'Ерофей Павлович',
         # 'Есауловка',
         # 'Жариково',
         # 'Желтоярово',
         # 'Житомировка',
         # 'Журавлевка',
         # 'Журбан',
         # 'Завитая',
         # 'Завитинск',
         # 'Заган',
         # 'Загорная Селитьба',
         # 'Заречная',
         # 'Заречное',
         # 'Заречный',
         # 'Зеленый Бор',
         # 'Зенковка',
         # 'Зея',
         # 'Зиговка',
         # 'Златоустовск',
         # 'Знаменка',
         # 'Золотая Гора',
         # 'Зорино',
         # 'Ивановка',
         # 'Ивановка',
         # 'Ивановка',
         # 'Ивановский',
         # 'Ивановское',
         # 'Игнатьево',
         # 'Игнашино',
         # 'Известковый',
         # 'Иликан',
         # 'Ильиновка',
         # 'им. Ленина',
         # 'Инагли',
         # 'Инжан',
         # 'Иннокентьевка',
         # 'Иса',
         'Источный',
         'Иташино',
         'Кавказ',
         'Казанка',
         'Казановка',
         'Казачий',
         'Калашниково',
         'Калинино',
         'Калиновка',
         'Калиновка',
         'Каменушка',
         'Камышевка',
         'Камышинка',
         'Кани-Курган',
         'Карьерный',
         'Касаткино',
         'Каховка',
         'Кивдинский',
         'Кипара',
         'Кировский',
         'Кировский',
         'Климовка',
         'Климоуцы',
         'Ключи',
         'Ключи',
         'Ключики',
         'Коболдо',
         'Коврижка',
         'Козьмодемьяновка',
         'Кольцово',
         'Комисаровка',
         'Константиновка',
         'Константиноградовка',
         'Короли',
         'Корфово',
         'Коршуновка',
         'Косицына',
         'Кострома',
         'Костюковка',
         'Красная Горка',
         'Красная Падь',
         'Красное',
         'Красноярово',
         'Красный Восток',
         'Красный Исток',
         'Красный Луч',
         'Красный Май',
         'Красный Яр',
         'Крестовка',
         'Крестовоздвиженка',
         'Крещеновка',
         'Круглое',
         'Крутой',
         'Кувыкта',
         'Кузнецово',
         'Куликовка',
         'Кулустай',
         'Кумара',
         'Кундур',
         'Куприяновка',
         'Куприяново',
         'Купури',
         'Курбатовский',
         'Курган',
         'Кустанаевка',
         'Кутилово',
         'Лагунай',
         'Лазаревка',
         'Лапри',
         'Ларба',
         'Лебяжье',
         'Ленинское',
         'Лермонтовка',
         'Лермонтово',
         'Лесной',
         'Лиманное',
         'Лиманное',
         'Липовка',
         'Липовка',
         'Лозовая',
         'Лозовой',
         'Локшак',
         'Лопча',
         'Луговое',
         'Луговое',
         'Луговой',
         'Лукинда',
         'Лукьяновка',
         'Любимое',
         'Магдагачи',
         'Мадалан',
         'Мазаново',
         'Майский',
         'Максимовка',
         'Малая Сазанка',
         'Малиновка',
         'Маргаритовка',
         'Мари',
         'Марково',
         'Маркучи',
         'Марьяновка',
         'Милехино',
         'Михайловка',
         'Михайловка',
         'Михайловка',
         'Михайловка',
         'Могилевка',
         'Могоктак',
         'Могот',
         'Молчаново',
         'Москвитино',
         'Мостовое',
         'Мостовой',
         'Муртыгит',
         'Мухино',
         'Мухинский',
         'Нагорный',
         'Надежденское',
         'Натальино',
         'Невер',
         'Некрасовка',
         'Некрасовка',
         'Некрасовский',
         'Нижний',
         'Нижняя Ильиновка',
         'Николаевка',
         'Николаевка',
         'Николоалександровка',
         'Никольское',
         'Нина',
         'Новая Кумара',
         'Новинка',
         'Новоалександровка',
         'Новоалексеевка',
         'Новоалексеевка',
         'Новобурейский',
         'Нововоскресеновка',
         'Нововысокое',
         'Новогеоргиевка',
         'Новое',
         'Новоивановка',
         'Новокиевский Увал',
         'Новолиствянка',
         'Новомихайловка',
         'Новоназаровка',
         'Новоникольск',
         'Новоохочье',
         'Новопетровка',
         'Новопетровка',
         'Новопокровка',
         'Новопокровка',
         'Новопокровка',
         'Новорайчихинск',
         'Новороссийка',
         'Новоселитьба',
         'Новосергеевка',
         'Новосергеевка',
         'Новоспасск',
         'Новостепановка',
         'Новотроицкое',
         'Новотроицкое',
         'Новочесноково',
         'Новоямполь',
         'Новый',
         'Новый Благовещенский',
         'Новый Быт',
         'Норск',
         'Нюкжа',
         'Нюкжа',
         'Обка',
         'Овсянка',
         'Огоджа',
         'Огорон',
         'Озерное',
         'Озеряне',
         'Октябрьский',
         'Октябрьский',
         'Октябрьский Прииск',
         'Олонгро',
         'Ольгинск',
         'Ольдой',
         'Орлецкий',
         'Орловка',
         'Орловка',
         'Орловка',
         'Осежино',
         'Островной',
         'Отважное',
         'Отроги',
         'Павловка',
         'Павловка',
         'Панино',
         'Пашково',
         'Первомайский',
         'Первомайское',
         'Передовой',
         'Перемыкино',
         'Переселенец',
         'Переясловка',
         'Петровка',
         'Петропавловка',
         'Петропавловка',
         'Петропавловка',
         'Петропавловка',
         'Петруши',
         'Пионер',
         'Платово',
         'Подоловка',
         'Поздеевка',
         'Покровка',
         'Поляковский',
         'Поляна',
         'Поляна',
         'Поповка',
         'Поселок Геологов',
         'Поселок Геологов',
         'Поярково',
         'Правая Райчиха',
         'Правовосточный',
         'Преображеновка',
         'Преображеновка',
         'Прибрежный',
         'Привольный',
         'Пригородное',
         'Пригородный',
         'Придорожное',
         'Придорожное',
         'Призейская',
         'Приозерное',
         'Прядчино',
         'Пурикан',
         'Путятино',
         'Пушкино',
         'Раздольное',
         'Раздольное',
         'Разливная',
         'Райгородка',
         'Райчиха',
         'Ракитное',
         'Рачи',
         'Рогачевка',
         'Рогозовка',
         'Родионовка',
         'Рождественка',
         'Романовка',
         'Ромны',
         'Рублевка',
         'Рычково',
         'Савельевка',
         'Сагибово',
         'Садовый',
         'Сапроново',
         'Саскаль',
         'Светиловка',
         'Светильное',
         'Свободное',
         'Свободный',
         'Святоруссовка',
         'Сгибнева',
         'Северный',
         'Северный',
         'Сегачама',
         'Селемджа',
         'Селеткан',
         'Семеновка',
         'Семеновка',
         'Семидомка',
         'Семиозерка',
         'Сергеевка',
         'Сергеевский',
         'Серебрянка',
         'Серышево',
         'Сиан',
         'Сиваки',
         'Сивачкан',
         'Сигикта',
         'Симоново',
         'Скобельцино',
         'Сковородино',
         'Слава',
         'Слава',
         'Случайное',
         'Смелое',
         'Смирновка',
         'Соколовка',
         'Солнечное',
         'Солнечный',
         'Соловьевск',
         'Сосновка',
         'Сосновый',
         'Сосновый Бор',
         'Спицыно',
         'Среднебелая',
         'Среднебелое',
         'Среднерейновский',
         'Средняя Нюкжа',
         'Степановка',
         'Стойба',
         'Стрелка',
         'Стретенка',
         'Сухотино',
         'Сычевка',
         'Тавричанка',
         'Таёжный',
         'Талакан',
         'Талали',
         'Талая',
         'Талдан',
         'Тамбовка',
         'Татакан',
         'Татьяновка',
         'Тахтамыгда',
         'Токур',
         'Толбузино',
         'Толстовка',
         'Томичи',
         'Томское',
         'Троицкое',
         'Трудовое',
         'Трудовой',
         'Тур',
         'Тыгда',
         'Тымерсоль',
         'Тында',
         'Увальный',
         'Угловое',
         'Угольный',
         'Удобный',
         'Украина',
         'Украинка',
         'Украинка',
         'Улунга',
         'Улунга',
         'Ульручьи',
         'Улягир',
         'Улятка',
         'Унаха',
         'Ураловка',
         'Урил',
         'Уркан',
         'Урожайное',
         'Уруша',
         'Успеновка',
         'Успеновка',
         'Успеновка',
         'Усть-Ивановка',
         'Усть-Кивда',
         'Усть-Нюкжа',
         'Усть-Тыгда',
         'Усть-Умлекан',
         'Усть-Уркима',
         'Ушаково',
         'Ушумшун',
         'Фарт',
         'Февральск',
         'Федоровка',
         'Федоровка',
         'Фроловка',
         'Халан',
         'Хани',
         'Харьковка',
         'Хвойный',
         'Хорогочи',
         'Хохлатское',
         'Цветковка',
         'Целинный',
         'Чагоян',
         'Чалганы',
         'Черемушки',
         'Черемхово',
         'Черкасовка',
         'Черниговка',
         'Черниговка',
         'Черноберезовка',
         'Черняево',
         'Чесноково',
         'Чеугда',
         'Чигири',
         'Чильчи',
         'Читкан',
         'Чудиновка',
         'Чуевка',
         'Шимановск',
         'Широкий',
         'Широкий Лог',
         'Шумиловка',
         'Шурино',
         'Экимчан',
         'Экскаваторный',
         'Эльгакан',
         'Эргель',
         'Юбилейный',
         'Южный',
         'Юктали',
         'Юхта',
         'Ядрино',
         'Яносовка',
         'Ясная Поляна',
         'Ясный',
         ]

name = ''
for name in names:
    data = ({"name": name})
    res = requests.post(url, json=data)
    time.sleep(1)



