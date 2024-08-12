import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from random import choice

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Наш сайт', url='http://usauniversities.tg.bot.tilda.ws', callback_data='site')
    button2 = types.InlineKeyboardButton(text='Почему США?', callback_data='question')
    button3 = types.InlineKeyboardButton(text='Список университетов', callback_data='listik')
    markup.add(button1, button2, button3)
    bot.send_photo(message.chat.id, photo=open('pereezd-v-ssha-na-pmzh-1500x1000.jpg', 'rb'), caption='Выберите опцию',  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'question')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Причина № 1', callback_data='reason')
    button2 = types.InlineKeyboardButton(text='Причина № 2', callback_data='reasonn')
    button3 = types.InlineKeyboardButton(text='Причина № 3', callback_data='reasonnn')
    button4 = types.InlineKeyboardButton(text='В главное меню', callback_data='farback')
    markup.add(button1, button2, button3, button4)
    bot.send_message(call.message.chat.id, "Выберите причину", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'reason')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Назад', callback_data='backr')
    markup.add(button1)
    bot.send_message(call.message.chat.id, '1. Америка является родиной многих ведущих университетов мира. Согласно мировому репутационному рейтингу журнала Times Higher Education за 2017, 41 американский университет входит в сотню лучших ВУЗов мира. Студенты, желающие обучаться в США, имеют возможность получить блестящее высшее образование.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'reasonn')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Назад', callback_data='backr')
    markup.add(button1)
    bot.send_message(call.message.chat.id,'2. Америка это весело! В США много интересных мест, таких как Гавайи, Аляска, Йеллоустонский национальный парк и Калифорния. Кроме того, со студенческой визой F-1, вы можете посетить Мексику без визы, хотя получить визу для стран Карибского бассейна и Канады довольно просто. Помимо путешествий, жизнь в городе никогда не бывает скучной независимо от того, является ли большим или маленьким город, где вы учитесь. Вы можете зайти на сайт MeetUp.com, чтобы найти друзей и единомышленников, посетить местный музей, стать волонтером. Американская жизнь прекрасна во всех ее проявлениях.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'reasonnn')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Назад', callback_data='backr')
    markup.add(button1)
    bot.send_message(call.message.chat.id, '3. Еще одна причина, почему стоит выбрать американский ВУЗ – это финансовая компенсация обучения. Несмотря на то, что по некоторым программам финансирование для иностранных студентов ограничено, университеты США могут быть достаточно щедрыми в предоставлении финансовой помощи, особенно для студентов STEM (science, technology, engineering, or mathematics). Кроме того, американские учебные заведения предоставляют множество возможностей для трудоустройства на кампусе, чтобы компенсировать затраты на обучение для иностранных студентов.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backr')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Причина № 1', callback_data='reason')
    button2 = types.InlineKeyboardButton(text='Причина № 2', callback_data='reasonn')
    button3 = types.InlineKeyboardButton(text='Причина № 3', callback_data='reasonnn')
    button4 = types.InlineKeyboardButton(text='В главное меню', callback_data='farback')
    markup.add(button1, button2, button3, button4)
    bot.send_message(call.message.chat.id, "Выберите причину", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'farback')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Наш сайт', url='http://usauniversities.tg.bot.tilda.ws', callback_data='site')
    button2 = types.InlineKeyboardButton(text='Почему США?', callback_data='question')
    button3 = types.InlineKeyboardButton(text='Список университетов', callback_data='listik')
    markup.add(button1, button2, button3)
    bot.send_photo(chat_id=call.message.chat.id, photo=open('pereezd-v-ssha-na-pmzh-1500x1000.jpg', 'rb'), caption='Выберите опцию',  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'listik')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Вашингтон', callback_data='washington')
    button2 = types.InlineKeyboardButton(text='Калифорния', callback_data='california')
    button3 = types.InlineKeyboardButton(text='Аризона', callback_data='arizona')
    button4 = types.InlineKeyboardButton(text='Вайоминг', callback_data='wyoming')
    button5 = types.InlineKeyboardButton(text='Колорадо', callback_data='colorado')
    button6 = types.InlineKeyboardButton(text='Миннесота', callback_data='minnesota')
    button7 = types.InlineKeyboardButton(text='Висконсин', callback_data='wisconsin')
    button8 = types.InlineKeyboardButton(text='Мичиган', callback_data='michigan')
    button9 = types.InlineKeyboardButton(text='Техас', callback_data='texas')
    button10 = types.InlineKeyboardButton(text='Нью-Йорк', callback_data='newyork')
    button11 = types.InlineKeyboardButton(text='В главное меню', callback_data='farback')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'425b2fea40c9c3e6a431eec5bc08b6c1.jpg', 'rb'), caption='Выберите штат', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'stateback')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Вашингтон', callback_data='washington')
    button2 = types.InlineKeyboardButton(text='Калифорния', callback_data='california')
    button3 = types.InlineKeyboardButton(text='Аризона', callback_data='arizona')
    button4 = types.InlineKeyboardButton(text='Вайоминг', callback_data='wyoming')
    button5 = types.InlineKeyboardButton(text='Колорадо', callback_data='colorado')
    button6 = types.InlineKeyboardButton(text='Миннесота', callback_data='minnesota')
    button7 = types.InlineKeyboardButton(text='Висконсин', callback_data='wisconsin')
    button8 = types.InlineKeyboardButton(text='Мичиган', callback_data='michigan')
    button9 = types.InlineKeyboardButton(text='Техас', callback_data='texas')
    button10 = types.InlineKeyboardButton(text='Нью-Йорк', callback_data='newyork')
    button11 = types.InlineKeyboardButton(text='В главное меню', callback_data='farback')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'425b2fea40c9c3e6a431eec5bc08b6c1.jpg', 'rb'),caption='Выберите штат', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'washington')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Washington', callback_data='uniwashington1')
    button2 = types.InlineKeyboardButton(text='Washington State University', callback_data='uniwashington2')
    button3 = types.InlineKeyboardButton(text='Western Washington University', callback_data='uniwashington3')
    button4 = types.InlineKeyboardButton(text='Gonzaga University', callback_data='uniwashington4')
    button5 = types.InlineKeyboardButton(text='Pacific Lutheran University', callback_data='uniwashington5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'washington-dc-gcffccf162_1920.jpg__0_0x0.jpg', 'rb'), caption='Штат Вашингтон находится на северо-востоке США на берегу Тихого океана, к югу от канадской провинции Британская Колумбия, к северу от штата Орегон и к западу от Айдахо. Его площадь составляет 184,8 км2, население — более 6 млн человек. Столица штата — город Олимпия, самые крупные города — Сиэтл, Спокан, Такома. Как добраться. Крупнейшие аэропорты штата Вашингтон находятся в 6 км от Олимпии, в Сиэтле и в Ситэке, между городами Сиэтл и Такома.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'california')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Stanford University', callback_data='unicalifornia1')
    button2 = types.InlineKeyboardButton(text='California Institute of Technology', callback_data='unicalifornia2')
    button3 = types.InlineKeyboardButton(text='University of Southern California', callback_data='unicalifornia3')
    button4 = types.InlineKeyboardButton(text='Pomona College', callback_data='unicalifornia4')
    button5 = types.InlineKeyboardButton(text='Claremont McKenna College', callback_data='unicalifornia5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'USA_Houses_Los_Angeles_California_Palms_599408_3840x2602.jpg', 'rb'), caption='Калифорния — самый населённый штат США (по результатам переписи населения США 2020 года) и 3-й по площади (после Аляски и Техаса). Столица — Сакраменто, крупнейший город — Лос-Анджелес. Другие крупные города: Сан-Франциско, Сан-Диего, Сан-Хосе. Штат известен своим разнообразным климатом, пёстрым составом населения. Калифорния занимает 1-е место среди штатов США по объёму ВВП.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'wyoming')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wyoming', callback_data='uniwyoming1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'37b3a423c55ff594f071f64fc69e2c13.jpg', 'rb'), caption='Штат Вайоминг находится на западе США и относится к группе Горных штатов в Скалистых горах системы Кордильер.Протяжённость штата с севера на юг составляет 450 км, а с запада на восток — 581 км. По площади он является 10-м штатом в США, занимая территорию 253 348 км².Столицей является самый крупный город штата — Шайенн.Вайоминг называют ковбойским штатом из-за того, что здесь издавна очень развито животноводство: разведение крупного рогатого скота и овечьи фермы.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'colorado')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Colorado Boulder', callback_data='unicolorado1')
    button2 = types.InlineKeyboardButton(text='Colorado State University-Fort Collins', callback_data='unicolorado2')
    button3 = types.InlineKeyboardButton(text='University of Denver', callback_data='unicolorado3')
    button4 = types.InlineKeyboardButton(text='University of Northern Colorado', callback_data='unicolorado4')
    button5 = types.InlineKeyboardButton(text='Colorado College', callback_data='unicolorado5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'412110_10151699817105123_357683390122_23835258_81151115_o-e1576488076879.jpg', 'rb'), caption='Колора́до — 38-й (по порядку) штат США. Это Горный штат. На севере Колорадо граничит с Вайомингом и Небраской, на востоке со штатом Канзас, на юге с Оклахомой, Нью-Мексикой и Аризоной, и с Ютой на западе. Это 8-ой по площади штат Америки. Площадь Колорадо составляет 269,8 км², 37 % которой занимают национальные парки. Население штата составляет более 4,5 млн человек. Столицей и самым крупным городом Колорадо является Денвер.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'minnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Minnesota-Twin Cities', callback_data='uniminnesota1')
    button2 = types.InlineKeyboardButton(text='Mayo Clinic College of Medicine and Science', callback_data='uniminnesota2')
    button3 = types.InlineKeyboardButton(text='Carleton College', callback_data='uniminnesota3')
    button4 = types.InlineKeyboardButton(text='University of St Thomas-Minnesota', callback_data='uniminnesota4')
    button5 = types.InlineKeyboardButton(text='Saint Cloud State University', callback_data='uniminnesota5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1670456913_priroda-club-p-shtat-minnesota-priroda-krasivo-foto-34.jpg', 'rb'), caption='Миннесота (/ˌmɪnəˈsoʊtə / ⓘ MIN-á-SOH-tə) - штат в регионе Верхнего Среднего Запада Соединенных Штатов. Это 12-й по величине штат США по площади и 22-й по численности населения, с населением более 5,75 миллиона человек. Миннесота известна как "Страна 10 000 озер" за наличие более 14 000 водоемов с пресной водой площадью не менее десяти акров каждый; примерно треть территории штата покрыта лесами; большая часть остальной территории - прерии и сельскохозяйственные угодья.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'wisconsin')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wisconsin-Madison', callback_data='uniwisconsin1')
    button2 = types.InlineKeyboardButton(text='University of Wisconsin-Milwaukee', callback_data='uniwisconsin2')
    button3 = types.InlineKeyboardButton(text='Marquette University', callback_data='uniwisconsin3')
    button4 = types.InlineKeyboardButton(text='University of Wisconsin-Eau Claire', callback_data='uniwisconsin4')
    button5 = types.InlineKeyboardButton(text='Lawrence University', callback_data='uniwisconsin5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1579665460_8-p-shtat-viskonsin-15.jpg', 'rb'), caption='Висконсин — это штат в США, расположенный южнее Мичигана. Его площадь составляет 169,7 тыс. кв. км.Висконсин отличается разнообразными природно-климатическими условиями. Смешанные леса покрывают возвышенные участки, между которыми раскинулась сеть ледниковых озёр и рек. Низменные приозерные районы и плодородная Центральная равнина покрыты разнотравьем и сельхозугодиями.В штате можно найти уникальные формирования песчаника, а районы Айрон-Маунтин изобилуют хвойными лесами, мини-каньонами и горными пустошами.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'michigan')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Michigan-Ann Arbor', callback_data='unimichigan1')
    button2 = types.InlineKeyboardButton(text='Michigan State University', callback_data='unimichigan2')
    button3 = types.InlineKeyboardButton(text='Wayne State University', callback_data='unimichigan3')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'db328ba494fc76f0c4927a106b86dab0.jpeg', 'rb'), caption='Штат Мичиган расположен на Среднем Западе США в районе Великих озёр.Озеро Мичиган является единственным из Великих озёр, находящимся полностью в Соединенных Штатах. Остальная территория граничит с четырьмя из пяти Великих озёр.Мичиган делится на верхний и нижний полуостров проливом Макино, который соединяет озера Мичиган и Гурон. Две части штата связаны мостом — одним из самых длинных подвесных мостов в мире.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'texas')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Texas at Austin', callback_data='unitexas1')
    button2 = types.InlineKeyboardButton(text='University of Houston', callback_data='unitexas2')
    button3 = types.InlineKeyboardButton(text='Rice University', callback_data='unitexas3')
    button4 = types.InlineKeyboardButton(text='Texas Tech University', callback_data='unitexas4')
    button5 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'capitol-building-aerial-skyline-sunset-austin-tx-texas-state-capital-501154548-58fd156b3df78ca159b45f04.jpg', 'rb'), caption='Техас — один из 50 штатов США. Был присоединен к стране указом президента 29 декабря 1845 года. Занимает второе место после Аляски по площади территории — 696 тысяч квадратных километров и второе место по численности населения после Калифорнии. По итогам переписи населения США 2020 года оно составило 29,1 миллиона человек.Столица штата — Остин, по административному делению состоит из 254 округов — это больше, чем у любого другого штата США.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'newyork')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Cornell University', callback_data='uninewyork1')
    button2 = types.InlineKeyboardButton(text='Columbia University', callback_data='uninewyork2')
    button3 = types.InlineKeyboardButton(text='New York University', callback_data='uninewyork3')
    button4 = types.InlineKeyboardButton(text='University at Buffalo', callback_data='uninewyork4')
    button5 = types.InlineKeyboardButton(text='Bard College', callback_data='uninewyork5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'united-states-of-america-nyu-iork-23130.jpg', 'rb'), caption='Штат Нью-Йорк (State of New York).В северо-восточной части США вдоль побережья Атлантики раскинулся штат Нью-Йорк. Главным городом штата является город Олбани.На северо-востоке протянулась граница с Канадой, юго-восточную часть занимает побережье Атлантики, западнее расположены озера – Онтарио и Эри, южнее находится остров Лонг-Айленд.Значительную часть территории штата занимают реки и озера. Другая часть покрыта горными хребтами Аппалачи.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'arizona')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Arizona', callback_data='uniarizona1')
    button2 = types.InlineKeyboardButton(text='Arizona State University-Tempe', callback_data='uniarizona2')
    button3 = types.InlineKeyboardButton(text='Northern Arizona University', callback_data='uniarizona3')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'midtown-phoenix-skyline-night-1.jpg', 'rb'), caption='Аризона (англ. Arizona) – штат, расположенный на юго-западе Соединенных Штатов Америки. На востоке граничит с Нью-Мексико, на западе – с Калифорнией, на южной стороне с Мексикой и на северо-восточной – с Колорадо.Площадь 295 254 км². Столицей штата является город Финикс. Крупные города: Меса и Тусон. В 2011 году население составляло 6 482 505 человек (16-е место по численности). Территория делится на 15 графств.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwashington1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.washington.edu/', callback_data='siteuniwashington1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'32155c917ef20f9879bd0da38cc84b20.jpg', 'rb'), caption='University of Washington (UW) — один из ведущих университетов США и мира. Расположен в самом сердце Северо-Западного побережья.Основан в 1861 году в Такоме, штат Вашингтон, как территориальный университет. В 1862 году переехал в Сиэтл и был переименован в Университет Вашингтона.Вуз славится своими исследовательскими программами и лабораториями, работающими в различных областях, включая медицину, технологии, науки о природе и многие другие.Университет постоянно расширяет число своих кампусов и модернизирует инфраструктуру, чтобы соответствовать потребностям студентов и исследовательским проектам.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwashington2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://wsu.edu/', callback_data='siteuniwashington2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'WSU-Spokane-scaled.jpg', 'rb'), caption='Университет штата Вашингтон — американский университет в городе Пулмен, штат Вашингтон.Он предлагает широкий спектр дисциплин, включая такие специализации, как инженерное дело, ветеринария, сельское хозяйство, медицина, естественные науки и многие другие.Университет является одним из ведущих государственных университетов Америки с высокой научно-исследовательской деятельностью по классификации Карнеги. Он был основан в 1890 году и является одним из старейших университетов на американском Западе.В настоящее время Университет штата Вашингтон имеет три филиала: WSU Spokane, WSU Tri-Cities и Washington State University Vancouver.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwashington3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.wwu.edu/', callback_data='siteuniwashington3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'c84750ff5b6ded030a08a0804b6f7e82.jpg', 'rb'), caption='Western Washington University – крупный американский университет в городе Беллингхем, штат Вашингтон. Существует с 1893 года. В Western учится 16 000 студентов. Они выбирают из 160 академических программ, среди которых антропология, математика, география, искусство, биология, история культуры, биохимия, медицина, юриспруденция, инженерия, кибербезопасность, танцы, философия или экономика.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwashington4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.gonzaga.edu/', callback_data='siteuniwashington4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'news4-1-5cf833947c545bdb.jpg', 'rb'), caption='Gonzaga University — это университет в США, основанный в 1887 году.Его гуманитарное наследие сосредоточено на обучении разума, тела и духа, а также на личном, академическом и профессиональном росте посредством критического мышления и творческих инноваций.В университете есть 92 направления и 26 программ магистратуры. Также есть программы подготовки к профессиональным школам в области бизнеса, образования, инженерии, стоматологии, богословия/теологии, права, медицины, сестринского дела и ветеринарии.Университет участвует в армейской программе ROTC, которая даёт возможность студентам после окончания учёбы стать офицерами.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwashington5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.plu.edu/', callback_data='siteuniwashington5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Screen-Shot-2016-12-14-at-5.12.21-PM.png', 'rb'), caption='Тихоокеанский лютеранский университет (PLU) - частный лютеранский университет в Паркленде, штат Вашингтон. Он был основан норвежскими лютеранскими иммигрантами в 1890 году. PLU спонсируется 580 конгрегациями региона I Евангелическо-лютеранской церкви в Америке. В плу обучается около 3100 студентов. По состоянию на 2017 год в школе работает около 220 штатных профессоров на территории лесного кампуса площадью 156 акров (63 га).', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backwashingtonuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Washington', callback_data='uniwashington1')
    button2 = types.InlineKeyboardButton(text='Washington State University', callback_data='uniwashington2')
    button3 = types.InlineKeyboardButton(text='Western Washington University', callback_data='uniwashington3')
    button4 = types.InlineKeyboardButton(text='Gonzaga University', callback_data='uniwashington4')
    button5 = types.InlineKeyboardButton(text='Pacific Lutheran University', callback_data='uniwashington5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'washington-dc-gcffccf162_1920.jpg__0_0x0.jpg', 'rb'), caption='Штат Вашингтон находится на северо-востоке США на берегу Тихого океана, к югу от канадской провинции Британская Колумбия, к северу от штата Орегон и к западу от Айдахо. Его площадь составляет 184,8 км2, население — более 6 млн человек. Столица штата — город Олимпия, самые крупные города — Сиэтл, Спокан, Такома. Как добраться. Крупнейшие аэропорты штата Вашингтон находятся в 6 км от Олимпии, в Сиэтле и в Ситэке, между городами Сиэтл и Такома.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicalifornia1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.stanford.edu/', callback_data='siteunicalifornia1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'scale_1200.jpeg', 'rb'), caption='Стэнфордский университет – огромный научно-исследовательский комплекс, объединяющий в себе 4 основных факультета: юридический, медицинский,экономический,технический. Здесь лучшие образовательные программы MBA в мире, десятки лабораторий, испытательных центров и, конечно, центр знаменитой Силиконовой долины. Таким образом, университет объединяет в себе две главнейших отрасли современного мира: крупный бизнес и высокие технологии.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicalifornia2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.caltech.edu/', callback_data='siteunicalifornia2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'scale_1200.png', 'rb'), caption='Калифорнийский технологический институт (Caltech) — частный исследовательский университет, расположенный в городе Пасадина в штате Калифорния.Это один из ведущих университетов США и один из двух самых важных, наряду с Массачусетским технологическим институтом, специализирующихся в точных науках и инженерии. Входит в десятку лучших университетов мира.Калтеху также принадлежит лаборатория реактивного движения, которая запускает большую часть автоматических космических аппаратов НАСА.В университете обучается около 1000 студентов и 1200 аспирантов.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicalifornia3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.usc.edu/', callback_data='siteunicalifornia3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'191112141459-01-university-of-southern-california-campus-file-scaled.jpg', 'rb'), caption='Университет Южной Калифорнии расположен в Лос-Анджелесе и является ведущим частным исследовательским университетом, глобальным центром искусства, технологий и международного бизнеса.В его состав входит до 21 академической школы и подразделения. В Медицинском кампусе находятся известные специализированные учреждения по лечению рака, изучению стволовых клеток и регенеративной медицины, ортопедии и спортивной медицине.Университет всегда занимает ведущие места в рейтингах частных университетов. Количество заявлений от первокурсников всегда очень высокое — более 64 000 заявок.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicalifornia4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.pomona.edu/', callback_data='siteunicalifornia4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'p2.jpg', 'rb'), caption='Помонский колледж — американский частный колледж свободных искусств в Клермонте (Калифорния).Основан 14 октября 1887 года группой христиан-конгрегационалистов, которые хотели воссоздать «типичный колледж Новой Англии» на территории Южной Калифорнии.Колледж предоставляет обучение по четырёхлетней программе бакалавриата. Около 1700 студентов обучаются 48 специальностям по гуманитарным дисциплинам и около 650 курсам. Также они имеют доступ к более чем 2000 дополнительным курсам в других колледжах Клермонта.Помонский колледж считается самым престижным гуманитарным колледжем на американском Западе и одним из самых престижных в стране.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicalifornia5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.cmc.edu/', callback_data='siteunicalifornia5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'claremont-mckenna-college-Victoire-Chalupy-wiki-58b5bdd63df78cdcd8b81643.jpg', 'rb'), caption='олледж Клермонт Маккенна (CMC) — частный гуманитарный колледж в Клермонте, Калифорния.В его учебной программе особое внимание уделяется государственному управлению, экономике, связям с общественностью, финансам и международным отношениям.Колледж был основан в 1946 году как мужской колледж, а в 1976 году стал совместным учебным заведением.В 2007 году он основал Школу экономики и финансов имени Роберта Дэя, которая предлагает магистерскую программу в области финансов.CMC известен консервативной политической ориентацией своего факультета по сравнению с аналогичными гуманитарными колледжами.По состоянию на 2019 год в университете насчитывалось 1338 студентов бакалавриата и аспирантуры.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backcaliforniauni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Stanford University', callback_data='unicalifornia1')
    button2 = types.InlineKeyboardButton(text='California Institute of Technology', callback_data='unicalifornia2')
    button3 = types.InlineKeyboardButton(text='University of Southern California', callback_data='unicalifornia3')
    button4 = types.InlineKeyboardButton(text='Pomona College', callback_data='unicalifornia4')
    button5 = types.InlineKeyboardButton(text='Claremont McKenna College', callback_data='unicalifornia5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'USA_Houses_Los_Angeles_California_Palms_599408_3840x2602.jpg', 'rb'),caption='Калифорния — самый населённый штат США (по результатам переписи населения США 2020 года) и 3-й по площади (после Аляски и Техаса). Столица — Сакраменто, крупнейший город — Лос-Анджелес. Другие крупные города: Сан-Франциско, Сан-Диего, Сан-Хосе. Штат известен своим разнообразным климатом, пёстрым составом населения. Калифорния занимает 1-е место среди штатов США по объёму ВВП.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwyoming1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.cmc.edu/', callback_data='siteuniuniwyoming15')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backwyominguni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'New_old_main_8d68026a-d9e5-4f61-bab1-70d1a903919b.jpg', 'rb'), caption='Университет Вайоминга — американский государственный университет, расположенный в Ларами, штат Вайоминг.Университет основан в сентябре 1886 года, то есть за четыре года до включения Вайоминга в состав США. Первых студентов университет принял в сентябре 1887 года.Вайомингский университет — национальный исследовательский центр, особенно в области защиты окружающей среды и природных ресурсов, со специализацией на агрокультуре, геологии и гидрологии.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backwyominguni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wyoming', callback_data='uniwyoming1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'37b3a423c55ff594f071f64fc69e2c13.jpg', 'rb'), caption='Штат Вайоминг находится на западе США и относится к группе Горных штатов в Скалистых горах системы Кордильер.Протяжённость штата с севера на юг составляет 450 км, а с запада на восток — 581 км. По площади он является 10-м штатом в США, занимая территорию 253 348 км².Столицей является самый крупный город штата — Шайенн.Вайоминг называют ковбойским штатом из-за того, что здесь издавна очень развито животноводство: разведение крупного рогатого скота и овечьи фермы.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicolorado1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.colorado.edu/https://www.colorado.edu/', callback_data='siteunicolorado1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'university-of-colorado-summer-14.jpg', 'rb'), caption='University of Colorado at Boulder (CU) — это университет государственного образца, функционирующий в лучших традициях обучения США.Преподавательский состав университета тщательно подбирается, благодаря чему он входит в список 200 лидеров в мире по качеству образования.CU известен своим активным участием в программе обмена студентами с другими университетами страны и за её пределами.Образовательная деятельность университета началась в 1876 году.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'unicolorado2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.colostate.edu/', callback_data='siteunicolorado2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1366_front.jpg', 'rb'), caption='Colorado State University находится в городе Форт-Коллинс, штат Колорадо, США.Он был основан в 1870 году как Сельскохозяйственный колледж Колорадо. В 1957 вуз был переименован в Государственный университет Колорадо.Colorado State реализует философию «земельных» колледжей: теоретические занятия в аудиториях здесь сочетаются с практикой в полевых и лабораторных условиях. Сегодня это один из ведущих научно-исследовательских институтов страны.Университет предлагает абитуриентам высшее образование мирового уровня: 65 программ бакалавриата, 55 — магистратуры, 40 — докторантуры, в том числе возможность получить степень доктора ветеринарной медицины.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicolorado3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.du.edu/', callback_data='siteunicolorado3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'e96b956b6b7b6f292f8acb15c9dd9d10.jpg', 'rb'), caption='Денверский университет (University of Denver) — частный исследовательский университет в городе Денвер, Колорадо, США.Аффилирован с Объединённой методистской церковью. Основан в 1864 году бывшим губернатором Колорадо Джоном Эвансом. Является старейшим частным университетом в регионе Скалистых гор.В университете обучается более 11 000 студентов. Кампус расположен в 11 км к югу от центра Денвера.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicolorado4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.unco.edu/', callback_data='siteunicolorado4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Wallpaper3.jpg', 'rb'), caption='Университет Северного Колорадо, основанный в 1889 году, находится в Грили, штат Колорадо. Вуз предлагает более 100 программ бакалавриата и более 100 программ магистратуры, обучая 13,035 студентов. Университет Северного Колорадо состоит из пяти колледжей педагогики и поведенческих наук, гуманитарных и социальных наук, естественных и медицинских наук, исполнительских и визуальных искусств и бизнеса.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unicolorado5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.coloradocollege.edu/', callback_data='siteunicolorado5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Colorado-College_Slocum-Hall_2012-Renovation-and-Addition_The-Treehouse.jpg', 'rb'), caption='Colorado College — это частный колледж в Колорадо, основанный в 1874 году Томасом Нельсоном Хаскеллом.Он известен своей уникальной системой «Block Plan», при которой студенты проходят один курс за раз в интенсивных 3,5-недельных блоках. Колледж расположен у подножия пика Пайкс, предлагая студентам уникальное сочетание городского и outdoor-experiences.В колледже предлагается более 40 специальностей и мини-специальностей, включая популярные программы в области экономики, экологии, политической науки, психологии и социологии.Студенты могут участвовать в более чем 100 студенческих клубах и организациях, а в колледже проводятся различные мероприятия в течение года, включая ежегодный летний музыкальный фестиваль Colorado College.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backunicolorado')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Colorado Boulder', callback_data='unicolorado1')
    button2 = types.InlineKeyboardButton(text='Colorado State University-Fort Collins', callback_data='unicolorado2')
    button3 = types.InlineKeyboardButton(text='University of Denver', callback_data='unicolorado3')
    button4 = types.InlineKeyboardButton(text='University of Northern Colorado', callback_data='unicolorado4')
    button5 = types.InlineKeyboardButton(text='Colorado College', callback_data='unicolorado5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'412110_10151699817105123_357683390122_23835258_81151115_o-e1576488076879.jpg', 'rb'),caption='Колора́до — 38-й (по порядку) штат США. Это Горный штат. На севере Колорадо граничит с Вайомингом и Небраской, на востоке со штатом Канзас, на юге с Оклахомой, Нью-Мексикой и Аризоной, и с Ютой на западе. Это 8-ой по площади штат Америки. Площадь Колорадо составляет 269,8 км², 37 % которой занимают национальные парки. Население штата составляет более 4,5 млн человек. Столицей и самым крупным городом Колорадо является Денвер.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniminnesota1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://twin-cities.umn.edu/', callback_data='siteuniminnesota1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'University-of-Minnesota-2.jpg', 'rb'), caption='Университет Миннесоты (UMN Twin Cities) — государственный исследовательский университет, предоставляющий земельные гранты в городах-побратимах Миннеаполисе и Сент-Поле, штат Миннесота, США.Кампус Twin Cities расположен в Миннеаполисе и Фалькон-Хайтс, пригороде Сент-Пола, примерно в 3 милях (4,8 км) друг от друга.Это ведущее учебное заведение системы Университета Миннесоты, состоящее из 19 колледжей, школ и других крупных академических подразделений.Университет предлагает 154 программы бакалавриата, 24 сертификата бакалавра, 307 программ магистратуры и 79 сертификатов выпускника.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniminnesota2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://college.mayo.edu/', callback_data='siteuniminnesota2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'173957-mayo-clinic-college-of-medicine-and-science.webp', 'rb'), caption='Медицинский и научный колледж клиники Майо (MCCMS) — это частный исследовательский университет, расположенный в Рочестере, штат Миннесота, США. Он готовит врачей, учёных и смежных медицинских работников.Колледж является частью академического медицинского центра клиники Майо и аккредитован Комиссией по высшему образованию (HLC).MCCMS состоит из пяти школ, которые предлагают доктора медицины, доктора философии и другие степени, а также медицинские ординатуры, стипендии и непрерывное медицинское образование (CME).Колледж базируется в Рочестере, штат Миннесота, с дополнительными кампусами в Финиксе и Скоттсдейле, штат Аризона, и Джексонвилле, штат Флорида.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniminnesota3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.carleton.edu/', callback_data='siteuniminnesota3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'carleton-college-2.jpg', 'rb'), caption='Карлтонский колледж (Carleton College) — частный гуманитарный колледж, расположенный в Нортфилде в Миннесоте.Он предлагает степень бакалавра, и в настоящее время в нём обучаются 2057 студентов.Карлтонский колледж часто входит в десятку лучших колледжей гуманитарных наук США. В 2015 году журнал US News & World Report поставил его на восьмое место по общему качеству и первое по качеству преподавания среди колледжей гуманитарных наук США.Среди выпускников Карлтонского колледжа были экономист Торстейн Веблен (1880), министр обороны 1969–1973 годов Мелвин Лэрд и генетик Мари-Клэр Кинг.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniminnesota4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.stthomas.edu/', callback_data='siteuniminnesota4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'7-5.jpg', 'rb'), caption='Частный католический исследовательский университет с кампусами в Сент-Поле и Миннеаполисе, штат Миннесота. Основанный в 1885 году как католическая семинария, он назван в честь Фомы Аквинского, средневекового католического богослова и философа, который является покровителем студентов. По состоянию на осень 2021 года в Сент-Томасе обучалось 9 347 студентов, что делает его крупнейшим частным некоммерческим университетом Миннесоты.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniminnesota5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.stcloudstate.edu/', callback_data='siteuniminnesota5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'636432483030335113-St.-Cloud-State-University1.webp', 'rb'), caption='Государственный университет Сент-Клауд (SCSU) — государственное некоммерческое учебное заведение, расположенное в городе Сен-Клу, США.SCSU является членом Minnesota State Colleges and Universities System и American Association of State Colleges and Universities (AASCU).Год основания университета — 1869.В вузе действует несколько программ финансовой поддержки, которые помогают учащимся покрывать часть расходов на обучение.Стоимость обучения для местных жителей начинается от 7 498 USD в год, для студентов из других стран — минимум 14 996 USD в год.У университета городской кампус, что открывает студентам много вариантов учебы и отдыха. В городе находятся крупные компании, которые предлагают стажировки. При учебном заведении есть библиотека.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backuniminnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Minnesota-Twin Cities', callback_data='uniminnesota1')
    button2 = types.InlineKeyboardButton(text='Mayo Clinic College of Medicine and Science',callback_data='uniminnesota2')
    button3 = types.InlineKeyboardButton(text='Carleton College', callback_data='uniminnesota3')
    button4 = types.InlineKeyboardButton(text='University of St Thomas-Minnesota', callback_data='uniminnesota4')
    button5 = types.InlineKeyboardButton(text='Saint Cloud State University', callback_data='uniminnesota5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'1670456913_priroda-club-p-shtat-minnesota-priroda-krasivo-foto-34.jpg', 'rb'),caption='Миннесота (/ˌmɪnəˈsoʊtə / ⓘ MIN-á-SOH-tə) - штат в регионе Верхнего Среднего Запада Соединенных Штатов. Это 12-й по величине штат США по площади и 22-й по численности населения, с населением более 5,75 миллиона человек. Миннесота известна как "Страна 10 000 озер" за наличие более 14 000 водоемов с пресной водой площадью не менее десяти акров каждый; примерно треть территории штата покрыта лесами; большая часть остальной территории - прерии и сельскохозяйственные угодья.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwisconsin1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.wisc.edu/', callback_data='siteuniwisconsin1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'social-card.jpg', 'rb'), caption='University of Wisconsin-Madison — это старейший и крупнейший вуз штата Висконсин, а также главный университет системы University of Wisconsin.Он был основан в 1848 году. В университете обучается почти 45 000 студентов, в том числе иностранные из 40 стран мира.Кампус университета находится в живописном месте между ботаническим садом и озёрами. На территории кампуса расположены 4 музея, спортивная арена, футбольный стадион, бассейны и спортивные центры.University of Wisconsin входит в число Public Ivy и занимает 13-е место среди американских государственных университетов. Он считается докторским университетом с очень высокой исследовательской активностью — на научные проекты тратится более 1,2 миллиарда долларов ежегодно.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwisconsin2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://uwm.edu/', callback_data='siteuniwisconsin2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'c7-4.jpg', 'rb'), caption='University of Wisconsin-Milwaukee — это общественный городской исследовательский университет, расположенный в городе Милуоки, штат Висконсин, США.Он был основан в 1956 году и предоставляет доступное образование мирового уровня для 27 000 студентов из 92 стран.В университете 15 школ и колледжей, включая единственные в Висконсине школы архитектуры, науки о пресной воде и здравоохранении. Он предлагает 195 академических программ бакалавриата, магистратуры, докторантуры, а также сертификатные и онлайн-курсы.Университет сотрудничает с ведущими компаниями в Висконсине и за его пределами. Он продвигает знания, выводит на рынок новые продукты, готовит студентов к работе на глобальном рынке труда.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwisconsin3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.marquette.edu/', callback_data='siteuniwisconsin3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'041815-marquette-lee-0179.jpg', 'rb'), caption='Marquette University — это приватный исследовательский университет, основанный в 1881 году. Он расположен в Милуоки, штат Висконсин, США.Университет предлагает широкий спектр программ обучения, включая бакалавриат, магистратуру и докторантуру. Студенты могут выбирать из более чем 80 специальностей и 80 миноров на уровне бакалавриата, а также из множества магистерских и докторских программ.Университет известен своими программами в области бизнеса, инженерии, коммуникаций, образования и права.Согласно международным экспертам, Marquette University занимает место в первых 5 процентах самых престижных учебных учреждений мира. При этом национальный академический рейтинг США относит его к 160 лучшим американским ВУЗам.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwisconsin4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.uwec.edu/', callback_data='siteuniwisconsin4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'20140911_CENTENNIAL_003.jpg', 'rb'), caption='Университет Висконсин–О–Клэр (UW-Eau Claire, UWEC или просто Eau Claire) — государственный университет в О–Клэр, штат Висконсин.Он является частью системы Висконсинского университета и предлагает степень бакалавра и магистра.Кампус состоит из 28 основных зданий, занимающих площадь 333 акра (135 га).Университет предлагает своим студентам возможность участвовать в национально признанной исследовательской программе через своё Управление исследований и спонсируемых программ (ORSP).', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniwisconsin5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.commonapp.org/explore/lawrence-university/', callback_data='siteuniwisconsin5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Main_Hall_at_Lawrence_University.jpg', 'rb'), caption='Lawrence University - это ведущий частный жилой гуманитарный колледж и музыкальная консерватория, специализирующаяся исключительно на бакалавриате. Сообщество Лоуренса, расположенное в гостеприимном Среднем Западе, штат Висконсин, с 15% его 1500 студентов из более чем 50 стран за пределами США, является одним из самых интернациональных в стране.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backuniminnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wisconsin-Madison', callback_data='uniwisconsin1')
    button2 = types.InlineKeyboardButton(text='University of Wisconsin-Milwaukee', callback_data='uniwisconsin2')
    button3 = types.InlineKeyboardButton(text='Marquette University', callback_data='uniwisconsin3')
    button4 = types.InlineKeyboardButton(text='University of Wisconsin-Eau Claire', callback_data='uniwisconsin4')
    button5 = types.InlineKeyboardButton(text='Lawrence University', callback_data='uniwisconsin5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1579665460_8-p-shtat-viskonsin-15.jpg', 'rb'), caption='Висконсин — это штат в США, расположенный южнее Мичигана. Его площадь составляет 169,7 тыс. кв. км.Висконсин отличается разнообразными природно-климатическими условиями. Смешанные леса покрывают возвышенные участки, между которыми раскинулась сеть ледниковых озёр и рек. Низменные приозерные районы и плодородная Центральная равнина покрыты разнотравьем и сельхозугодиями.В штате можно найти уникальные формирования песчаника, а районы Айрон-Маунтин изобилуют хвойными лесами, мини-каньонами и горными пустошами.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unimichigan1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='', callback_data='siteunimichigan1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunimichigan')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'caption.jpg', 'rb'), caption='Мичиганский университет — государственный исследовательский университет в Анн-Арборе, штат Мичиган. Основан в 1817 году, это старейшее высшее учебное заведение штата.Мичиганский университет является одним из первых американских исследовательских университетов и членом-основателем Ассоциации американских университетов.Он состоит из девятнадцати колледжей и предлагает 250 дипломных программ на уровне бакалавриата и магистратуры по различным гуманитарным и STEM-дисциплинам.Университет аккредитован Комиссией по высшему образованию. В 2021 году он занял третье место среди американских университетов по расходам на исследования по данным Национального научного фонда.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unimichigan1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='', callback_data='siteunimichigan1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunimichigan')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'', 'rb'), caption='', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unimichigan1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='', callback_data='siteunimichigan1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backunimichigan')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'', 'rb'), caption='', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backunimichigan')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Michigan-Ann Arbor', callback_data='unimichigan1')
    button2 = types.InlineKeyboardButton(text='Michigan State University', callback_data='unimichigan2')
    button3 = types.InlineKeyboardButton(text='Wayne State University', callback_data='unimichigan3')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'db328ba494fc76f0c4927a106b86dab0.jpeg', 'rb'),caption='Штат Мичиган расположен на Среднем Западе США в районе Великих озёр.Озеро Мичиган является единственным из Великих озёр, находящимся полностью в Соединенных Штатах. Остальная территория граничит с четырьмя из пяти Великих озёр.Мичиган делится на верхний и нижний полуостров проливом Макино, который соединяет озера Мичиган и Гурон. Две части штата связаны мостом — одним из самых длинных подвесных мостов в мире.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniarizona1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.arizona.edu/', callback_data='siteuniarizona1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'734f715a9479442c44f75452ba10e45b.jpg', 'rb'), caption='University of Arizona (UA) – государственный исследовательский университет, расположенный в Тусоне, штат Аризона. Преподавательский состав является сильнейшим в регионе, где также работают лауреаты Нобелевской премии. The University Arizona работает с многочисленными предприятиями и даёт возможность как проводить исследования, так и проходить различные стажровки, что позволяет студентам достичь больших высот в своей области.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniarizona2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.asu.edu/academics/colleges-schools/tempe', callback_data='siteuniarizona2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Arizona_State_University,_Tempe_Main_Campus,_Tempe,_AZ_-_panoramio_(61).jpg', 'rb'), caption='Tempe — это кампус Arizona State University (ASU).Он предлагает студентам и выпускникам возможность заниматься многодисциплинарными исследованиями и исследованиями в первоклассных лабораториях и помещениях.На кампусе расположены:колледж Liberal Arts and Sciences;Herberger Institute for Design and the Arts;School for the Future of Innovation in Society;School of Sustainability.Также на кампусе находятся:Ira A. Fulton Schools of Engineering;Mary Lou Fulton Teachers College;W. P. Carey School of Business;University College;Barrett, The Honors College.Кампус Tempe отличается высокой экологичностью и предлагает лёгкий доступ ко всей столице Phoenix через общественный транспорт, включая лёгкую железную дорогу.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uniarizona3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://nau.edu/', callback_data='siteuniarizona3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'northern-arizona-university-twitter.webp', 'rb'), caption='Northern Arizona University (NAU) является публичным исследовательским университетом, расположенным в городе Флагстафф, штат Аризона. Основанный в 1899 году, NAU предлагает широкий спектр программ бакалавриата, магистратуры и докторантуры через свои колледжи и школы, включая Колледж искусств и письма, Колледж образования, Колледж инженерии, информатики и прикладных наук, Колледж здоровья и гуманитарных наук, The W. A. Franke College of Business и многие другие.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backarizonauni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Arizona', callback_data='uniarizona1')
    button2 = types.InlineKeyboardButton(text='Arizona State University-Tempe', callback_data='uniarizona2')
    button3 = types.InlineKeyboardButton(text='Northern Arizona University', callback_data='uniarizona3')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'midtown-phoenix-skyline-night-1.jpg', 'rb'),caption='Аризона (англ. Arizona) – штат, расположенный на юго-западе Соединенных Штатов Америки. На востоке граничит с Нью-Мексико, на западе – с Калифорнией, на южной стороне с Мексикой и на северо-восточной – с Колорадо.Площадь 295 254 км². Столицей штата является город Финикс. Крупные города: Меса и Тусон. В 2011 году население составляло 6 482 505 человек (16-е место по численности). Территория делится на 15 графств.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uninewyork1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.cornell.edu/', callback_data='siteuninewyork1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backnewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Campus image for fb.jpg', 'rb'), caption='Cornell University – частный исследовательский университет, основанный в 1865 году. Это единственный университет Лиги плюща, основанный после американской Войны за независимость. В Корнелле обучается 24,000 студентов. Корнеллский университет располагается в небольшом тихом городке Итака в Новой Англии, в четырех часах езды от Нью-Йорка.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uninewyork2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.columbia.edu/', callback_data='siteuninewyork2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backnewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'97281_original.png', 'rb'), caption='Columbia University — один из самых престижных и старейших частных университетов Америки. Расположен в районе Манхеттен в Нью-Йорке.Был основан в середине 18 века как Королевский колледж. Входит в «Лигу плюща» — образовательную элиту США.Среди выпускников и преподавателей Колумбийского университета несколько президентов Америки, главы других государств, лауреаты премии «Оскар» и Нобелевской премии.Главный кампус расположен в сердце Нью-Йорка, на Манхеттене. Он занимает 13 гектаров земли. На кампусах университета есть всё для жизни и учебы: библиотеки, лаборатории, инфраструктура для занятий спортом, медицинский центр.Для студентов работают более 500 организаций и кружков по интересам.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uninewyork3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.nyu.edu/', callback_data='siteuninewyork3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backnewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'nyu-stern.webp', 'rb'), caption='Нью-Йоркский университет — частный исследовательский университет США, расположенный в Нью-Йорке. Один из наиболее известных и престижных высших учебных заведений мира.В 2020 году Нью-Йоркский университет занял 11 место среди лучших университетов США и 35 место среди лучших университетов мира в рейтинге Quacquarelli Symonds (QS).Университет является самым крупным научно-исследовательским частным университетом Соединённых Штатов. В нём обучаются более 51 тысячи студентов.Нью-Йоркский университет состоит из 16 школ, институтов и колледжей. Главный корпус университета располагается в Гринвич-Виллидж в Манхеттене.Университет является членом Ассоциации американских университетов, объединяющей с 1900 года ведущие научно-исследовательские университеты Северной Америки.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uninewyork4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.buffalo.edu/', callback_data='siteuninewyork4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backnewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'buffalo-state.jpg', 'rb'), caption='Университет в Буффало (UB) — государственный исследовательский университет с кампусами в Буффало и Амхерсте, штат Нью-Йорк, США.Университет был основан в 1846 году как частный медицинский колледж, а в 1962 году объединился с системой Государственного университета Нью-Йорка.По состоянию на 2022 год это одно из двух ведущих учебных заведений системы SUNY.Университет предлагает степени бакалавра по более чем 140 областям обучения, а также более 220 магистерских программ и более 95 докторских программ.В 1989 году UB был избран в Ассоциацию американских университетов.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uninewyork5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.commonapp.org/explore/bard-college/', callback_data='siteuninewyork5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backnewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'bard-college-campus_1130x500_acf_cropped.jpg', 'rb'), caption='Бард-колледж (англ. Bard College, сокращённо Бард) — престижный частный гуманитарный университет свободных искусств и наук, расположенный в Аннандейл-на-Гудзоне, округ Датчесс, штат Нью-Йорк. Является Национальным историческим памятником США.В состав учреждения входит одна из самых молодых и прогрессивных консерваторий Америки.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'uninewyork5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Cornell University', callback_data='uninewyork1')
    button2 = types.InlineKeyboardButton(text='Columbia University', callback_data='uninewyork2')
    button3 = types.InlineKeyboardButton(text='New York University', callback_data='uninewyork3')
    button4 = types.InlineKeyboardButton(text='University at Buffalo', callback_data='uninewyork4')
    button5 = types.InlineKeyboardButton(text='Bard College', callback_data='uninewyork5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'united-states-of-america-nyu-iork-23130.jpg', 'rb'),caption='Штат Нью-Йорк (State of New York).В северо-восточной части США вдоль побережья Атлантики раскинулся штат Нью-Йорк. Главным городом штата является город Олбани.На северо-востоке протянулась граница с Канадой, юго-восточную часть занимает побережье Атлантики, западнее расположены озера – Онтарио и Эри, южнее находится остров Лонг-Айленд.Значительную часть территории штата занимают реки и озера. Другая часть покрыта горными хребтами Аппалачи.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unitexas1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.utexas.edu/', callback_data='siteunitexas1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backntexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'BostonEntrance_10rs.jpg', 'rb'), caption='University of Texas at Austin — государственный университет в Остине, штат Техас, США.Он был основан в 1883 году и является одним из самых крупных в стране и самым большим в Техасе.Университет активно занимается исследованиями, значимыми для общества, привлекая студентов и преподавателей к решению задач и вызовов науки. Сумма финансирования научных исследований на базе вуза составляет более 400 миллионов долларов.Университет предлагает широкий выбор специальностей — гуманитарных, технических, классических и узкого профиля.Он расположен в центре Остина, кампус городского типа площадью 437 акров. В состав кампуса входит 9 академических университетов и 6 государственных медицинских учреждений.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unitexas2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://uh.edu/', callback_data='siteunitexas2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backtexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'825_585_uh.jpg', 'rb'), caption='Хью́стонский университет (англ. University of Houston) — общественный исследовательский университет в США, расположенный в Хьюстоне, штат Техас. Крупнейший и главный кампус в cистеме Хьюстонского университета (UHS), а также 3-й по величине университет в штате. Изданием The Princeton Review был причислен к одному из лучших университетов США, а также входит в число первых 300 университетов в Академическом рейтинге университетов мира.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unitexas3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.rice.edu/', callback_data='siteunitexas3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backtexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'lovettbirdseye.jpg', 'rb'), caption='Rice University (полное название — Университет Уильяма Марша Райса) — это престижный частный университет, расположенный в городе Хьюстон, штат Техас.Он был основан в 1891 году бизнесменом Уильямом Маршем Райсом, который оставил большую часть своего состояния на создание учебного заведения.Сегодня вуз входит в число лучших заведений США, стабильно находится в топ-20. Ежегодно на исследования выделяются огромные средства, работает множество профессиональных исследовательских центров и групп (более 100).В Rice University действуют отделения бакалавриата, магистратуры и докторантуры, есть возможность проходить краткосрочные и дополнительные курсы.Выпускники с дипломами Rice University ценятся как прекрасные специалисты в своих областях.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'unitexas4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.ttu.edu/', callback_data='siteunitexas4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='backtexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'texas-tech-university-health-sciences-center-2.jpg', 'rb'), caption='Техасский технологический университет, основанный в 1923 году в Лаббоке, штат Техас, также известен как Техасский технологический колледж. В данный момент в вузе учится 28,422 студента. Университет предлагает академические программы на базе колледжей и школ сельскохозяйственных наук и природных ресурсов, инженерии, искусств и наук, массовых коммуникаций, визуальных и исполнительских искусств, общественных услуг, архитектуры, бизнеса, педагогики и права.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backtexasuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Texas at Austin', callback_data='uniexas1')
    button2 = types.InlineKeyboardButton(text='University of Houston', callback_data='unitexas2')
    button3 = types.InlineKeyboardButton(text='Rice University', callback_data='unitexas3')
    button4 = types.InlineKeyboardButton(text='Texas Tech University', callback_data='unitexas4')
    button5 = types.InlineKeyboardButton(text='Назад', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'capitol-building-aerial-skyline-sunset-austin-tx-texas-state-capital-501154548-58fd156b3df78ca159b45f04.jpg','rb'),caption='Техас — один из 50 штатов США. Был присоединен к стране указом президента 29 декабря 1845 года. Занимает второе место после Аляски по площади территории — 696 тысяч квадратных километров и второе место по численности населения после Калифорнии. По итогам переписи населения США 2020 года оно составило 29,1 миллиона человек.Столица штата — Остин, по административному делению состоит из 254 округов — это больше, чем у любого другого штата США.',reply_markup=markup)




bot.polling(none_stop=True)






