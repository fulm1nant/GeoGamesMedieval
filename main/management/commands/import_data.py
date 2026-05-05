from django.core.management.base import BaseCommand
from main.models import Country, Region

class Command(BaseCommand):
    help = 'Импортирует все данные о странах из views.py в базу данных'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Начинаю импорт данных...'))

    countries_data = {
        # ========== ЭРРИДИЯ ==========
        'erridia': {
            'name': 'Королевство Эрридия',
            'color': '#F0F0F0',
            'flag': '/static/images/flags/erridia/erridia_flag.jpg',
            'region_name': 'Ярлства',
            'general_info': {
                'politics': 'Торговля и установление дипломатических связей',
                'military': 'Оборона',
                'language': 'Эрридианский (новый)',
                'religion': 'Квадар',
                'income': 'Мореплавание (исследование рун и новых земель), торговля (экспорт металлических и каменных изделий)',
                'ruling_house': 'Римсайд',
                'current_ruler': 'Эррид 5й, сын Эртена Зго',
                'heir': 'Эррин Зй'
            },
            'religion': {
                'name': 'Квадар',
                'description': 'Пантеон из 4-х богов, каждый из которых отвечает за свои аспекты бытия. Формально их можно разделить на 2-х "хороших" и 2-х "плохих". Каждому богу присвоен свой орден, а также возводятся здания для поклонения.',
                'example': 'Путеводный факел в честь бога солнца Эльдурина',
                'adopted_by': ['Королевство Эрридия', 'Альк Кадир'],
                'gods': [
                    {'name': 'Хельгримнир', 'title': 'Бог войны, разрушения и зла', 'description': 'Покровительствует воинам, кровавым правителям и военному ремеслу. Его можно попросить об удаче в бою или проклятия для врага.'},
                    {'name': 'Готвальдр', 'title': 'Бог мира, добра и милосердия', 'description': 'Покровительствует правителям, дипломатам. Дает благословение от невзгод.'},
                    {'name': 'Миркарр', 'title': 'Бог луны, ночи и самой тьмы', 'description': 'Покровительствует убийцам, ворам, тем кто добивается цели не смотря на жертвы.'},
                    {'name': 'Эльдурин', 'title': 'Бог света, солнца и огня', 'description': 'Покровительствует мирным ремеслам, познанию нового и саморазвитию.'}
                ]
            },
            # === ДОБАВЛЕНО: Ярлства (как регионы) ===
            'regions': [
                {'name': 'Раустен', 'flag': '/static/images/flags/erridia/erridia_rausten.jpg', 'description': ''},
                {'name': 'Тейден', 'flag': '/static/images/flags/erridia/erridia_teyden.jpg', 'description': ''},
                {'name': 'Альден', 'flag': '/static/images/flags/erridia/erridia_alden.jpg', 'description': ''},
                {'name': 'Фоссен', 'flag': '/static/images/flags/erridia/erridia_fossen.jpg', 'description': ''},
                {'name': 'Бронтен', 'flag': '/static/images/flags/erridia/erridia_bronten.jpg', 'description': ''},
            ],
            # === Тингства (структура внутри ярлств) ===
            'jarlstvos': [
                {
                    'name': 'Ярлство Раустен',
                    'tings': [
                        {'name': 'Райстенмар', 'flag': '/static/images/flags/erridia/ting_raistenmar.png', 'desc': 'Тингство Райстенмар'},
                        {'name': 'Луннаталлен', 'flag': '/static/images/flags/erridia/ting_lunnatalia.png', 'desc': 'Тингство Луннаталлен'},
                        {'name': 'Кантерия', 'flag': '/static/images/flags/erridia/ting_kanteria.png', 'desc': 'Тингство Кантерия'},
                    ]
                },
                {
                    'name': 'Ярлство Тейден',
                    'tings': [
                        {'name': 'Тейден Энн-Кастри', 'flag': '/static/images/flags/erridia/ting_teyden.png', 'desc': 'Тингство Тейден Энн-Кастри'},
                        {'name': 'Тейден Энн-Фод', 'flag': '/static/images/flags/erridia/ting_teyden_fod.png', 'desc': 'Тингство Тейден Энн-Фод'},
                    ]
                },
                {
                    'name': 'Ярлство Альден',
                    'tings': [
                        {'name': 'Тарнор', 'flag': '/static/images/flags/erridia/ting_tarnor.png', 'desc': 'Тингство Тарнор'},
                        {'name': 'Хаустен', 'flag': '/static/images/flags/erridia/ting_hausten.png', 'desc': 'Тингство Хаустен'},
                        {'name': 'Фьяград', 'flag': '/static/images/flags/erridia/ting_fjagrad.png', 'desc': 'Тингство Фьяград'},
                        {'name': 'Нектаррен', 'flag': '/static/images/flags/erridia/ting_nektarren.png', 'desc': 'Тингство Нектаррен'},
                    ]
                },
                {
                    'name': 'Ярлство Фоссен',
                    'tings': [
                        {'name': 'Фосскофград', 'flag': '/static/images/flags/erridia/ting_fosskofgrad.png', 'desc': 'Тингство Фосскофград'},
                        {'name': 'Хаффенвирланд', 'flag': '/static/images/flags/erridia/ting_haffenvirland.png', 'desc': 'Тингство Хаффенвирланд'},
                    ]
                },
                {
                    'name': 'Ярлство Бронтен',
                    'tings': [
                        {'name': 'Соларрен', 'flag': '/static/images/flags/erridia/ting_solarren.png', 'desc': 'Тингство Соларрен'},
                        {'name': 'Фискград', 'flag': '/static/images/flags/erridia/ting_fiskgrad.png', 'desc': 'Тингство Фискград'},
                        {'name': 'Готвальдрен-Хусс', 'flag': '/static/images/flags/erridia/ting_gotvaldren_huss.png', 'desc': 'Тингство Готвальдрен-Хусс'},
                    ]
                },
            ],
            'language': {
                'name': 'Эрридианский (Erridian mál)',
                'description': 'Государственный язык Королевства Эрридия (Kinghavn Erridia). Третья редакция языка.',
                'alphabet': {
                    'letters': [
                        {'char': 'A', 'sound': '[a]', 'desc': 'Как «а» в слове «мама»'},
                        {'char': 'B', 'sound': '[b]', 'desc': 'Обычный «б»'},
                        {'char': 'D', 'sound': '[d]', 'desc': 'Твёрдый «д»'},
                        {'char': 'Ð', 'sound': '[ð]', 'desc': 'Мягкое «дь» (используется редко, ~20%)'},
                        {'char': 'E', 'sound': '[ɛ]', 'desc': 'Как русское «э» («это»)'},
                        {'char': 'Ë', 'sound': '[je]', 'desc': 'Как украинская «є» / мягкое «е»'},
                        {'char': 'Æ', 'sound': '[æ]', 'desc': 'Как в английском «cat»'},
                        {'char': 'F', 'sound': '[f]', 'desc': 'Обычный «ф»'},
                        {'char': 'G', 'sound': '[g]', 'desc': 'Обычный «г»'},
                        {'char': 'H', 'sound': '[h]', 'desc': 'Придыхательный «х»'},
                        {'char': 'I', 'sound': '[i]', 'desc': 'Как «и» в «мир»'},
                        {'char': 'Ї', 'sound': '[ji]', 'desc': 'Йотированное «йи» (поэтическая лексика)'},
                        {'char': 'J', 'sound': '[j]', 'desc': 'Как «й» в «йогурт»'},
                        {'char': 'K', 'sound': '[k]', 'desc': 'Обычный «к»'},
                        {'char': 'L', 'sound': '[l]', 'desc': 'Обычный «л»'},
                        {'char': 'M', 'sound': '[m]', 'desc': 'Обычный «м»'},
                        {'char': 'N', 'sound': '[n]', 'desc': 'Обычный «н»'},
                        {'char': 'O', 'sound': '[o]', 'desc': 'Как «о» в «дом»'},
                        {'char': 'Ø', 'sound': '[ø]', 'desc': '«Оэ» — между «о» и «э», как нем. ö'},
                        {'char': 'P', 'sound': '[p]', 'desc': 'Обычный «п»'},
                        {'char': 'R', 'sound': '[r]', 'desc': 'Вибрирующий «р» как в русском'},
                        {'char': 'S', 'sound': '[s]', 'desc': 'Обычный «с»'},
                        {'char': 'Š', 'sound': '[ʃ]', 'desc': 'Твёрдый шипящий «ш»'},
                        {'char': 'Ŝ', 'sound': '[ɕ]', 'desc': 'Мягкий шипящий «щ»'},
                        {'char': 'T', 'sound': '[t]', 'desc': 'Обычный «т»'},
                        {'char': 'Þ', 'sound': '[θ]', 'desc': '«Т» с придыханием (как англ. «think»)'},
                        {'char': 'U', 'sound': '[u]', 'desc': 'Как русское «у» («лук»)'},
                        {'char': 'V', 'sound': '[v]', 'desc': 'Обычный «в»'},
                        {'char': 'Y', 'sound': '[y]', 'desc': 'Как франц. «u» / нем. «ü» (между «и» и «ю»)'},
                        {'char': 'Z', 'sound': '[z]', 'desc': 'Звонкое «з»'},
                    ]
                },
                'grammar': {
                    'suffixes': [
                        {'suffix': '-er', 'desc': 'Мужской род (druker, vakten/vakter, grader...)'},
                        {'suffix': '-yr', 'desc': 'Женский род (drukyr, mannyr, kvindruk...)'},
                        {'suffix': '-lin', 'desc': 'Маленькое / детёныш (kattlin, ulflin...)'},
                        {'suffix': '-is', 'desc': 'Родительный или книжная форма (mális, kinghavnar...)'},
                        {'suffix': '-ris', 'desc': 'Лит. / торжественная форма (einstakliris, stridaris...)'},
                        {'suffix': '-tis', 'desc': 'Официально-абстрактная форма (новые слова)'},
                        {'suffix': '-um', 'desc': 'Место / пост / коллективное (vaktum, narenland...)'},
                        {'suffix': '-ed', 'desc': 'Будущее время 3 л. ед. ч. (ramed, skahorded...)'},
                    ],
                    'pronouns': [
                        {'word': 'Es', 'desc': 'Я (повседневное / официальное)'},
                        {'word': 'Ek', 'desc': 'Я (только ритуальное / религиозное)'},
                        {'word': 'Du', 'desc': 'Ты'},
                        {'word': 'Mæs', 'desc': 'Мы'},
                    ],
                    'prepositions': [
                        {'word': 'Tor', 'desc': 'Для'},
                        {'word': 'Un / Es', 'desc': 'В'},
                        {'word': 'Ton', 'desc': 'На'},
                        {'word': 'Van', 'desc': 'К / в направлении'},
                        {'word': 'Naren', 'desc': 'Под'},
                        {'word': 'Avren', 'desc': 'Над'},
                        {'word': 'Melz', 'desc': 'Между'},
                        {'word': 'Koss', 'desc': 'Через'},
                        {'word': 'Var', 'desc': 'У / около'},
                        {'word': 'Sin', 'desc': 'Среди'},
                        {'word': 'Bæk / Bæken', 'desc': 'За / позади'},
                    ],
                    'naming': 'Все имена жителей Эрридии начинаются с приставки Эр- (Er-) как знак уважения к народу и предкам. Имена богов (Helgrimnir, Gotvaldr, Mir\'karr, Eldurin) — исключения.'
                },
                'numbers': {
                    'units': [
                        {'num': '1', 'word': 'anet'}, {'num': '2', 'word': 'þvin'}, {'num': '3', 'word': 'þrín'},
                        {'num': '4', 'word': 'fær'}, {'num': '5', 'word': 'pan'}, {'num': '6', 'word': 'šek'},
                        {'num': '7', 'word': 'fjen'}, {'num': '8', 'word': 'atte'}, {'num': '9', 'word': 'daz'},
                    ],
                    'tens': [
                        {'num': '10', 'word': 'denzet', 'desc': 'Десяток; корень den-'},
                        {'num': '20', 'word': 'þvinvet', 'desc': 'Суффикс -vet'},
                        {'num': '30', 'word': 'þrintet', 'desc': 'Суффикс -tet'},
                        {'num': '40', 'word': 'færket', 'desc': 'Суффикс -ket'},
                        {'num': '50', 'word': 'pandet', 'desc': 'Суффикс -det'},
                        {'num': '60', 'word': 'šeknet', 'desc': 'Суффикс -net'},
                        {'num': '70', 'word': 'fjeset', 'desc': 'Суффикс -set'},
                        {'num': '80', 'word': 'atmet', 'desc': 'Суффикс -met'},
                        {'num': '90', 'word': 'dazpet', 'desc': 'Суффикс -pet'},
                    ],
                    'hundreds': [
                        {'num': '100', 'word': 'ðøset'}, {'num': '200', 'word': 'þvøset'}, {'num': '300', 'word': 'þrøset'},
                        {'num': '400', 'word': 'førset'}, {'num': '500', 'word': 'pønset'}, {'num': '1000', 'word': 'zetta'},
                    ],
                    'rule': 'Составные числа строятся: [тысячи] [сотни] [десятки+единицы]. Единицы 11–19: корень цифры + -zet.'
                },
                'dictionary': [
                    {'word': 'Es', 'trans': 'Я', 'desc': 'Личное мест. 1 л. ед. ч.; повседневная и официальная речь'},
                    {'word': 'Du', 'trans': 'Ты', 'desc': 'Личное мест. 2 л. ед. ч.'},
                    {'word': 'Mæs', 'trans': 'Мы', 'desc': 'Личное мест. 1 л. мн. ч.'},
                    {'word': 'Mann', 'trans': 'Человек / мужчина', 'desc': 'Сущ.; мн. ч. menn; с окончанием — manner'},
                    {'word': 'Mannyr', 'trans': 'Женщина', 'desc': 'Сущ.; жен. форма от mann'},
                    {'word': 'Druk', 'trans': 'Друг', 'desc': 'Сущ.; drukers — друзья; druker — дружелюбный'},
                    {'word': 'Kingsum', 'trans': 'Правитель (король/королева)', 'desc': 'Универсальный титул'},
                    {'word': 'Kinghavn', 'trans': 'Королевство', 'desc': 'Сущ. от king + havn'},
                    {'word': 'Grad', 'trans': 'Город', 'desc': 'Сущ.'},
                    {'word': 'Stragrad', 'trans': 'Порт', 'desc': 'Sstra + grad; «прибрежный город»'},
                    {'word': 'Erland', 'trans': 'Отечество / родина', 'desc': 'Er- (народ Эрридии) + land'},
                    {'word': 'Hass', 'trans': 'Дом', 'desc': 'Сущ.; hasser — домовладелец'},
                    {'word': 'Borgum', 'trans': 'Крепость', 'desc': 'Сущ.'},
                    {'word': 'Eldur', 'trans': 'Огонь / пламя', 'desc': 'Сущ.; elduris — огненный'},
                    {'word': 'Solarus', 'trans': 'Солнце', 'desc': 'Сущ.; solaris — солнечный'},
                    {'word': 'Lunes', 'trans': 'Луна', 'desc': 'Сущ.; lunelis — лунный свет'},
                    {'word': 'Jolnir', 'trans': 'Золото', 'desc': 'Сущ.; jolniris — золотой'},
                    {'word': 'Lunn', 'trans': 'Серебро', 'desc': 'Сущ.'},
                    {'word': 'Eizen', 'trans': 'Железо', 'desc': 'Сущ.'},
                    {'word': 'Vakten', 'trans': 'Страж', 'desc': 'Сущ.; vaktenyr — стражница'},
                    {'word': 'Vint', 'trans': 'Работать', 'desc': 'Глагол, инфинитив'},
                    {'word': 'Tala', 'trans': 'Говорить', 'desc': 'Глагол, инфинитив'},
                    {'word': 'Vans', 'trans': 'Идти', 'desc': 'Глагол, инфинитив; væ — иду'},
                    {'word': 'Lovd', 'trans': 'Обещаю', 'desc': 'Глагол 1 л. ед. ч.; lov — обещание'},
                    {'word': 'Sæl', 'trans': 'Привет (разг.)', 'desc': 'Приветствие; sælen — «приветствую» (офиц.)'},
                    {'word': 'Frid', 'trans': 'Мир / покой', 'desc': 'Сущ.'},
                    {'word': 'Druzis', 'trans': 'Дружба', 'desc': 'Сущ.; высокая форма от druk'},
                    {'word': 'Mál', 'trans': 'Язык / речь', 'desc': 'Сущ.'},
                    {'word': 'Falð', 'trans': 'Народ', 'desc': 'Сущ.'},
                    {'word': 'Ríki', 'trans': 'Государство', 'desc': 'Сущ.'},
                    {'word': 'Maht', 'trans': 'Мощь', 'desc': 'Сущ.; mahter — мощный'},
                    {'word': 'Sterket', 'trans': 'Сильный / крепкий', 'desc': 'Прилаг.'},
                    {'word': 'Snar', 'trans': 'Быстрый', 'desc': 'Прилаг.'},
                    {'word': 'Gamler', 'trans': 'Старый', 'desc': 'Прилаг.'},
                    {'word': 'Ren', 'trans': 'Красный', 'desc': 'Цвет; renis — прилаг.'},
                    {'word': 'Sunn', 'trans': 'Жёлтый', 'desc': 'Цвет; sunnis — прилаг.'},
                    {'word': 'Zarn', 'trans': 'Зелёный', 'desc': 'Цвет; zarnis — прилаг.'},
                    {'word': 'Švar', 'trans': 'Чёрный', 'desc': 'Цвет; švaris — прилаг.'},
                    {'word': 'Fætes', 'trans': 'Белый', 'desc': 'Цвет; fætesis — прилаг.'},
                    {'word': 'Blaren', 'trans': 'Синий', 'desc': 'Цвет; blarenis — прилаг.'},
                    {'word': 'Nord', 'trans': 'Север', 'desc': 'Сторона света; nordir — северный'},
                    {'word': 'Jun', 'trans': 'Юг', 'desc': 'Сторона света; junir — южный'},
                    {'word': 'Zest', 'trans': 'Запад', 'desc': 'Сторона света; zestir — западный'},
                    {'word': 'Vost', 'trans': 'Восток', 'desc': 'Сторона света; vostir — восточный'},
                ]
            }
        },

        # ========== ЭЛОРА ==========
        'elora': {
            'name': 'Королевство Элора',
            'color': '#5DBCD2',
            'flag': '/static/images/flags/elora/elora_flag.jpg',
            'region_name': 'Регионы',
            'general_info': {
                'politics': 'Торговля, Дипломатия',
                'military': 'Миролюбивая (оборонительная)',
                'language': 'Русский (официальный)',
                'religion': 'Католичество',
                'income': 'Торговля: Доставка провизии, рыболовство, наёмничество',
                'ruling_house': 'Элорианы',
                'current_ruler': 'Элориан Фулми',
                'heir': 'Отсутствует',
                'fact': 'Народ, который на данный момент проживает в Королевстве Элора, пришёл с далёких южных земель с целью найти идеальное место для проживания. Также во всём мире (на данный момент) существует только одна гильдия наёмников. Эти наёмники обученные в лучших королевских академиях, потому за достойную плату они способны на многое.'
            },
            'regions': [
                {'name': 'Аурлин', 'flag': '/static/images/flags/elora/elora_aurlin.jpg', 'description': ''},
                {'name': 'Вальдрейн', 'flag': '/static/images/flags/elora/elora_valdrain.jpg', 'description': ''},
                {'name': 'Селестария', 'flag': '/static/images/flags/elora/elora_celestaria.jpg', 'description': ''},
                {'name': 'Мирвелл', 'flag': '/static/images/flags/elora/elora_mirvell.jpg', 'description': ''},
                {'name': 'Генерис', 'flag': '/static/images/flags/elora/elora_generis.jpg', 'description': ''},
            ],
        },

        # ========== СОЛЕНОР ==========
        'solennor': {
            'name': 'Королевство Соленор',
            'color': '#111111',
            'flag': '/static/images/flags/solennor/solennor_flag.jpg',
            'region_name': 'Регионы',
            'general_info': {
                'politics': 'Религия, торговля',
                'military': 'Нейтралитет (оборонительная)',
                'language': 'Английский (государственный); Эрридианский (международный)',
                'religion': 'Light Shrine (храм света)',
                'income': 'Клирикство: медицина, алхимия. Торговля: Продажа угля, лекарств.',
                'ruling_house': 'Soulid\'Un (Солидан)',
                'current_ruler': 'Годрик Солидан',
                'heir': 'Эррик Солидан; Годлинк Солидан',
                'fact': 'В стране идёт священная война с теневым подземным народом. Обеими сторонами было решено заморозить конфликт и изолироваться друг от друга.'
            },
            'regions': [
                {'name': 'Флэймхолд', 'flag': '/static/images/flags/solennor/solennor_flamehold.jpg', 'description': ''},
                {'name': 'Солерсэт', 'flag': '/static/images/flags/solennor/solennor_solersat.jpg', 'description': ''},
            ],
        },

        # ========== ВАЛКАРИОН ==========
        'valkarion': {
            'name': 'Валкарионская Империя',
            'color': '#6b6b6b',
            'flag': '/static/images/flags/valkarion/valkarion_flag.jpg',
            'region_name': 'Регионы',
            'general_info': {
                'politics': 'Торговля, гибкая дипломатия',
                'military': 'Оборона, мирный захват нейтральных земель',
                'language': 'Общий, альдреймарский',
                'religion': 'Крепь Начала',
                'income': 'Торговля, наёмные инженеры',
                'ruling_house': 'Вальденны',
                'current_ruler': 'Арден 3-й Вальденн',
                'heir': 'Верик 1-й Вальденн',
                'fact': 'Народ Валкариона пришёл с холодных северо-западных земель около 300 лет назад, ведомый вождем Альдреем Вальденном. Они обнаружили древний Замок, стоящий на скале над морем — сооружение, которое существовало до появления человечества. В 1282 году королевство Альдреймар было преобразовано в Валкарионскую Империю, столица перенесена в Валкарион.'
            },
            'religion_detail': {
                'name': 'Религия - Крепь Начала',
                'description': 'Первый Замок — это древнее и непостижимое строение, возникшее до появления человечества. Люди не построили его, он был всегда. Он стоит в мире или вне его, и служит опорой самой реальности. Верующие считают, что именно из Замка "вытек свет порядка", и мир начал строиться вокруг него — как город вокруг крепости. Замок не бог, но он — первая форма, из которой родился порядок.',
                'beliefs': 'Люди — задача мира. Лишь поздние гости в этом мире, и их цель — строить и беречь, как Замок берёг начало. Всё, что устойчиво, симметрично, выстроено, приближает к Замку. Крепь Начала не требует поклонения, но учит наблюдать, строить и понимать. Главное — передавать знание, строить города, укреплять стены (моральные, не только физические). Уважение к тишине, к симметрии, к мастерству — форма молитвы.'
            },
            'regions': [
                {'name': 'Мирелар', 'flag': '/static/images/flags/valkarion/valkarion_mirelar.jpg', 'description': ''},
                {'name': 'Варгхейм', 'flag': '/static/images/flags/valkarion/valkarion_vargheim.jpg', 'description': ''},
                {'name': 'Айрдола', 'flag': '/static/images/flags/valkarion/valkarion_airdola.jpg', 'description': ''},
                {'name': 'Гарнхольд', 'flag': '/static/images/flags/valkarion/valkarion_garnhold.jpg', 'description': ''},
                {'name': 'Ревенпорт', 'flag': '/static/images/flags/valkarion/valkarion_revenport.jpg', 'description': ''},
                {'name': 'Фальден', 'flag': '/static/images/flags/valkarion/valkarion_falden.jpg', 'description': ''},
                {'name': 'Клинмор', 'flag': '/static/images/flags/valkarion/valkarion_klinmor.jpg', 'description': ''},
                {'name': 'Валкарион', 'flag': '/static/images/flags/valkarion/valkarion_valkarion.jpg', 'description': ''},
                {'name': 'Варелон', 'flag': '/static/images/flags/valkarion/valkarion_varelon.jpg', 'description': ''},
                {'name': 'Тальверайн', 'flag': '/static/images/flags/valkarion/valkarion_talverayn.jpg', 'description': ''},
                {'name': 'Элкард', 'flag': '/static/images/flags/valkarion/valkarion_elcard.jpg', 'description': ''},
            ],
        },

        # ========== УДОВ (ПОЛНОСТЬЮ ЗАПОЛНЕНО) ==========
        'udov': {
            'name': 'Королевство Удов',
            'color': '#5EEAD4',
            'flag': '/static/images/flags/udov/udov_flag.jpg',
            'region_name': 'Уезды',
            'general_info': {
                'politics': 'Взаимопомощь и невмешательство',
                'military': 'Оборона',
                'language': '',
                'religion': '',
                'income': 'Аренда земли для порта ИВД (Империю Великих Домов) и продажа берёзы',
                'ruling_house': 'Неизвестен',
                'current_ruler': 'Король Батько-Зелëный',
                'heir': 'Неизвестен'
            },
            'regions': [
                {'name': 'Березовский уезд', 'flag': '/static/images/flags/udov/udov_berezovsky.jpg', 'description': ''},
                {'name': 'Златокаменский уезд', 'flag': '/static/images/flags/udov/udov_zlatokamensky.jpg', 'description': ''},
            ],
        },

        'alk-kadir': {
            'name': 'Альк Кадир',
            'color': '#D4AF37',
            'flag': '/static/images/flags/alk-kadir/alk-kadir_flag.jpg',
            'region_name': 'Регионы',
            'general_info': {
                'politics': 'Торговля, Дипломатия',
                'military': 'Миролюбивая (оборонительная)',
                'language': 'Русский (официальный)',
                'religion': 'Квадар',
                'income': 'Торговля: Доставка металла, инструментов, стройматериалов, драгоценных металлов и изделий из них.',
                'ruling_house': 'Лодгар',
                'current_ruler': 'Грун Лодгар',
                'heir': 'Отсутствует',
                'fact': 'Кадирцы заняли горы после долгих скитаний в надежде на спасение. Поначалу это должен был быть перевалочный пункт для продвижения в более пригодные для жизни места, но в итоге путь их был завершён, и они основали поселение Альк Кадир. С тех пор род Лодгаров правит в этих землях.'
            },
            'religion': {
                'name': 'Квадар',
                'description': 'Пантеон из 4-х богов, каждый из которых отвечает за свои аспекты бытия. Формально их можно разделить на 2-х "хороших" и 2-х "плохих". Каждому богу присвоен свой орден, а также возводятся здания для поклонения.',
                'example': 'Путеводный факел в честь бога солнца Эльдурина',
                'adopted_by': ['Королевство Эрридия', 'Королевство Соленор', 'Альк Кадир'],
                'gods': [
                    {'name': 'Хельгримнир', 'title': 'Бог войны, разрушения и зла',
                     'description': 'Покровительствует воинам, кровавым правителям и военному ремеслу. Его можно попросить об удаче в бою или проклятия для врага.'},
                    {'name': 'Готвальдр', 'title': 'Бог мира, добра и милосердия',
                     'description': 'Покровительствует правителям, дипломатам. Дает благословение от невзгод.'},
                    {'name': 'Миркарр', 'title': 'Бог луны, ночи и самой тьмы',
                     'description': 'Покровительствует убийцам, ворам, тем кто добивается цели не смотря на жертвы.'},
                    {'name': 'Эльдурин', 'title': 'Бог света, солнца и огня',
                     'description': 'Покровительствует мирным ремеслам, познанию нового и саморазвитию.'}
                ]
            },
            'regions': [
                {'name': 'Дурмак', 'flag': '/static/images/flags/alk-kadir/alk-kadir_durmak.jpg', 'description': ''},
                {'name': 'Громнигр', 'flag': '/static/images/flags/alk-kadir/alk-kadir_gromnigr.jpg',
                 'description': ''},
                {'name': 'Жуланбур', 'flag': '/static/images/flags/alk-kadir/alk-kadir_zhulanburg.jpg',
                 'description': ''},
                {'name': 'Нижний Нарклаг', 'flag': '/static/images/flags/alk-kadir/alk-kadir_nizhny_narklag.jpg',
                 'description': ''},
                {'name': 'Верхний Нарклаг', 'flag': '/static/images/flags/alk-kadir/alk-kadir_verhny_narklag.jpg',
                 'description': ''},
            ],
        },

        'great-houses': {
            'name': 'Империя Великих Домов',
            'color': '#1E3A8A',
            'flag': '/static/images/flags/great-houses/great-houses_flag.jpg',
            'region_name': 'Великие Дома',
            'general_info': {
                'politics': 'Распространение влияния, содействие ассоциации с федерацией',
                'military': 'Защита интересов государства, союзников и их оборона',
                'language': '',
                'religion': '',
                'income': 'Сбор податей, кузнечное дело',
                'ruling_house': 'Демидовы',
                'current_ruler': 'Михаил Демидов',
                'heir': '',
                'fact': 'Имеет федеративное устройство'
            },
            'regions': [
                {'name': 'Демидовы', 'flag': '/static/images/flags/great-houses/great-houses_demidov.png',
                 'description': ''},
                {'name': 'Бугарищевы', 'flag': '/static/images/flags/great-houses/great-houses_bugarishchev.png',
                 'description': ''},
                {'name': 'Гуляевы', 'flag': '/static/images/flags/great-houses/great-houses_gulyaev.png',
                 'description': ''},
                {'name': 'Крутовы', 'flag': '/static/images/flags/great-houses/great-houses_krutov.png',
                 'description': ''},
                {'name': 'Пугачи', 'flag': '/static/images/flags/great-houses/great-houses_pugachi.png',
                 'description': ''},
            ],
            # Уезды (отдельный список)
            'uezds': [
                'Туфский', 'Александрийский', 'Поляновский', 'Солнцегорский',
                'Гвоздевский', 'Гидицкий', 'Галицкий', 'Чорнопольский',
                'Высоколесский', 'Цареград', 'Великомуромский', 'Кайский',
                'Руницкий', 'Жигинский', 'Соколиный', 'Щукинский',
                'о. Тихий', 'Зелёноборский', 'Миценский', 'Ярский',
                'Рижский', 'Вежайский'
            ],
        },
        'aliola': {
            'name': 'Королевство Алиола',
            'color': '#8B5CF6',
            'flag': '/static/images/flags/aliola/aliola_flag.jpg',
            'region_name': 'Регионы',
            'general_info': {
                'politics': 'Взаимопомощь и невмешательство',
                'military': 'Оборона',
                'language': '',
                'religion': '',
                'income': 'Экспорт экзотических товаров в ИВД (Империю Великих Домов)',
                'ruling_house': 'Неизвестен',
                'current_ruler': 'Неизвестен',
                'heir': 'Неизвестен'
            },
            'regions': [
                {'name': 'Алион', 'flag': '/static/images/flags/aliola/aliola_alion.jpg', 'description': ''},
                {'name': 'Кеймур', 'flag': '/static/images/flags/aliola/aliola_keymour.jpg', 'description': ''},
                {'name': 'Вейласта', 'flag': '/static/images/flags/aliola/aliola_veilasta.jpg', 'description': ''},
            ],
        },
    }
    # Импорт данных
    for slug, data in countries_data.items():
        country, created = Country.objects.get_or_create(
            slug=slug,
            defaults={
                'name': data['name'],
                'color': data['color'],
                'flag': data.get('flag', ''),
                'region_name': data.get('region_name', 'Регионы'),
                'politics': data.get('politics', ''),
                'military': data.get('military', ''),
                'income': data.get('income', ''),
                'ruling_house': data.get('ruling_house', ''),
                'current_ruler': data.get('current_ruler', ''),
                'heir': data.get('heir', ''),
                'fact': data.get('fact', ''),
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'✓ Создана страна: {country.name}'))
        else:
            self.stdout.write(self.style.WARNING(f'~ Обновлена страна: {country.name}'))

        # Создаем регионы
        regions_data = data.get('regions', [])
        for region_data in regions_data:
            Region.objects.get_or_create(
                country=country,
                name=region_data['name'],
                defaults={
                    'flag': region_data.get('flag', ''),
                    'description': region_data.get('description', ''),
                }
            )

    self.stdout.write(self.style.SUCCESS('\n🎉 Импорт завершен успешно!'))
    self.stdout.write(self.style.SUCCESS(f'Всего стран: {Country.objects.count()}'))
    self.stdout.write(self.style.SUCCESS(f'Всего регионов: {Region.objects.count()}'))