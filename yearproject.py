import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
from random import choice
import logging


bot = telebot.TeleBot('6727085832:AAGFeJytLGc8DV6W9jlHC33Na-nosVWuSWk')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Русский', callback_data='ruchange')
    button2 = types.InlineKeyboardButton(text='English', callback_data='engchange')
    markup.add(button1, button2)
    bot.send_message(message.chat.id, '⚙️Выберите язык: \n'
'     Select a language:', parse_mode='MarkdownV2', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruchange')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Продолжить/Continue', callback_data='mainrumenu')
    button2 = types.InlineKeyboardButton(text='Назад/Back', callback_data='backlanguagestart')
    markup.add(button1, button2)
    bot.send_message(call.message.chat.id, '⚙️Вы уверенны, что хотите выбрать русский язык? \n'
'||     Are you sure you want to choose Russian?||' , parse_mode='MarkdownV2', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engchange')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Продолжить/Continue', callback_data='mainengmenu')
    button2 = types.InlineKeyboardButton(text='Назад/Back', callback_data='backlanguagestart')
    markup.add(button1, button2)
    bot.send_message(call.message.chat.id,'⚙️Are you sure you want to choose English? \n'
'||     Вы уверенны, что хотите выбрать английский язык?||', parse_mode='MarkdownV2', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'backlanguagestart')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Русский', callback_data='ruchange')
    button2 = types.InlineKeyboardButton(text='English', callback_data='engchange')
    markup.add(button1, button2)
    bot.send_message(call.message.chat.id, '⚙️Выберите язык: \n'
'||     Select a language:||', parse_mode='MarkdownV2', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'mainrumenu')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Наш сайт', url='http://usauniversities.tg.bot.ru.tilda.ws/', callback_data='site')
    button2 = types.InlineKeyboardButton(text='Почему США?', callback_data='ruquestion')
    button3 = types.InlineKeyboardButton(text='Список университетов', callback_data='rulistik')
    button4 = types.InlineKeyboardButton(text='⚙️Сменить язык', callback_data='rulanguagechange')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open('pereezd-v-ssha-na-pmzh-1500x1000.jpg', 'rb'), caption='Выберите опцию:',  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'mainengmenu')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Our website', url='http://usauniversities.tg.bot.eng.tilda.ws/', callback_data='site')
    button2 = types.InlineKeyboardButton(text='Why the USA?', callback_data='engquestion')
    button3 = types.InlineKeyboardButton(text='List of universities', callback_data='englistik')
    button4 = types.InlineKeyboardButton(text='⚙️Change the language', callback_data='englanguagechange')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open('pereezd-v-ssha-na-pmzh-1500x1000.jpg', 'rb'), caption='Select an option:',  reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rulanguagechange')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Русский', callback_data='ruchange')
    button2 = types.InlineKeyboardButton(text='English', callback_data='engchange')
    button3 = types.InlineKeyboardButton(text='Назад/Back', callback_data='mainrumenu')
    markup.add(button1, button2, button3)
    bot.send_message(call.message.chat.id, '⚙️Выберите язык: \n'
'||     Select a language:||', parse_mode='MarkdownV2', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'englanguagechange')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Русский', callback_data='ruchange')
    button2 = types.InlineKeyboardButton(text='English', callback_data='engchange')
    button3 = types.InlineKeyboardButton(text='Back/Назад', callback_data='mainengmenu')
    markup.add(button1, button2, button3)
    bot.send_message(call.message.chat.id, '⚙️Select a language: \n'
'||     Выберите язык:||', parse_mode='MarkdownV2', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruquestion')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Причина № 1', callback_data='rureason')
    button2 = types.InlineKeyboardButton(text='Причина № 2', callback_data='rureasonn')
    button3 = types.InlineKeyboardButton(text='Причина № 3', callback_data='rureasonnn')
    button4 = types.InlineKeyboardButton(text='В главное меню', callback_data='mainrumenu')
    markup.add(button1, button2, button3, button4)
    bot.send_message(call.message.chat.id, "Выберите причину", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rureason')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Назад', callback_data='rubackr')
    markup.add(button1)
    bot.send_message(call.message.chat.id, '1. Америка является родиной многих ведущих университетов мира. Согласно мировому репутационному рейтингу журнала Times Higher Education за 2017, 41 американский университет входит в сотню лучших ВУЗов мира. Студенты, желающие обучаться в США, имеют возможность получить блестящее высшее образование.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'rureasonn')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Назад', callback_data='rubackr')
    markup.add(button1)
    bot.send_message(call.message.chat.id,'2. Америка это весело! В США много интересных мест, таких как Гавайи, Аляска, Йеллоустонский национальный парк и Калифорния. Кроме того, со студенческой визой F-1, вы можете посетить Мексику без визы, хотя получить визу для стран Карибского бассейна и Канады довольно просто. Помимо путешествий, жизнь в городе никогда не бывает скучной независимо от того, является ли большим или маленьким город, где вы учитесь. Вы можете зайти на сайт MeetUp.com, чтобы найти друзей и единомышленников, посетить местный музей, стать волонтером. Американская жизнь прекрасна во всех ее проявлениях.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'rureasonnn')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Назад', callback_data='rubackr')
    markup.add(button1)
    bot.send_message(call.message.chat.id, '3. Еще одна причина, почему стоит выбрать американский ВУЗ – это финансовая компенсация обучения. Несмотря на то, что по некоторым программам финансирование для иностранных студентов ограничено, университеты США могут быть достаточно щедрыми в предоставлении финансовой помощи, особенно для студентов STEM (science, technology, engineering, or mathematics). Кроме того, американские учебные заведения предоставляют множество возможностей для трудоустройства на кампусе, чтобы компенсировать затраты на обучение для иностранных студентов.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackr')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Причина № 1', callback_data='rureason')
    button2 = types.InlineKeyboardButton(text='Причина № 2', callback_data='rureasonn')
    button3 = types.InlineKeyboardButton(text='Причина № 3', callback_data='rureasonnn')
    button4 = types.InlineKeyboardButton(text='В главное меню', callback_data='mainrumenu')
    markup.add(button1, button2, button3, button4)
    bot.send_message(call.message.chat.id, "Выберите причину", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engquestion')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Reason #1', callback_data='engreason')
    button2 = types.InlineKeyboardButton(text='Reason #2', callback_data='engreasonn')
    button3 = types.InlineKeyboardButton(text='Reason #3', callback_data='engreasonnn')
    button4 = types.InlineKeyboardButton(text='To the main menu', callback_data='mainengmenu')
    markup.add(button1, button2, button3, button4)
    bot.send_message(call.message.chat.id, "Choose a reason", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engreason')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Back', callback_data='engbackr')
    markup.add(button1)
    bot.send_message(call.message.chat.id, '1. America is home to many of the worlds leading universities. According to the Times Higher Education magazines global reputation rating for 2017, 41 American universities are among the top hundred universities in the world. Students who want to study in the USA have the opportunity to receive a brilliant higher education.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'engreasonn')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Back', callback_data='engbackr')
    markup.add(button1)
    bot.send_message(call.message.chat.id,'2. America is fun! There are many interesting places in the USA, such as Hawaii, Alaska, Yellowstone National Park and California. In addition, with an F-1 student visa, you can visit Mexico without a visa, although it is quite easy to get a visa for the Caribbean and Canada. Apart from traveling, life in the city is never boring, regardless of whether the city where you study is big or small. You can go to the website MeetUp.com to find friends and like-minded people, visit a local museum, become a volunteer. American life is beautiful in all its forms.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'engreasonnn')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Back', callback_data='engbackr')
    markup.add(button1)
    bot.send_message(call.message.chat.id, '3. Another reason why you should choose an American university is financial compensation for tuition. Despite the fact that funding for international students is limited for some programs, US universities can be quite generous in providing financial assistance, especially for STEM (science, technology, engineering, or mathematics) students. In addition, American educational institutions provide many on-campus job opportunities to offset tuition costs for international students.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackr')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Reason #1', callback_data='engreason')
    button2 = types.InlineKeyboardButton(text='Reason #2', callback_data='engreasonn')
    button3 = types.InlineKeyboardButton(text='Reason #3', callback_data='engreasonnn')
    button4 = types.InlineKeyboardButton(text='To the main menu', callback_data='mainengmenu')
    markup.add(button1, button2, button3, button4)
    bot.send_message(call.message.chat.id, "Choose a reason", reply_markup=markup)





@bot.callback_query_handler(func=lambda call: call.data == 'rulistik')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Вашингтон', callback_data='ruwashington')
    button2 = types.InlineKeyboardButton(text='Калифорния', callback_data='rucalifornia')
    button3 = types.InlineKeyboardButton(text='Аризона', callback_data='ruarizona')
    button4 = types.InlineKeyboardButton(text='Вайоминг', callback_data='ruwyoming')
    button5 = types.InlineKeyboardButton(text='Колорадо', callback_data='rucolorado')
    button6 = types.InlineKeyboardButton(text='Миннесота', callback_data='ruminnesota')
    button7 = types.InlineKeyboardButton(text='Висконсин', callback_data='ruwisconsin')
    button8 = types.InlineKeyboardButton(text='Мичиган', callback_data='rumichigan')
    button9 = types.InlineKeyboardButton(text='Техас', callback_data='rutexas')
    button10 = types.InlineKeyboardButton(text='Нью-Йорк', callback_data='runewyork')
    button11 = types.InlineKeyboardButton(text='В главное меню', callback_data='mainrumenu')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'425b2fea40c9c3e6a431eec5bc08b6c1.jpg', 'rb'), caption='Выберите штат', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'englistik')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Washington', callback_data='engwashington')
    button2 = types.InlineKeyboardButton(text='California', callback_data='engcalifornia')
    button3 = types.InlineKeyboardButton(text='Arizona', callback_data='engarizona')
    button4 = types.InlineKeyboardButton(text='Wyoming', callback_data='engwyoming')
    button5 = types.InlineKeyboardButton(text='Colorado', callback_data='engcolorado')
    button6 = types.InlineKeyboardButton(text='Minnesota', callback_data='engminnesota')
    button7 = types.InlineKeyboardButton(text='Wisconsin', callback_data='engwisconsin')
    button8 = types.InlineKeyboardButton(text='Michigan', callback_data='engmichigan')
    button9 = types.InlineKeyboardButton(text='Texas', callback_data='engtexas')
    button10 = types.InlineKeyboardButton(text='New-York', callback_data='engnewyork')
    button11 = types.InlineKeyboardButton(text='To the main menu', callback_data='mainengmenu')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'425b2fea40c9c3e6a431eec5bc08b6c1.jpg', 'rb'), caption='Select a state', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rustateback')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Вашингтон', callback_data='ruwashington')
    button2 = types.InlineKeyboardButton(text='Калифорния', callback_data='rucalifornia')
    button3 = types.InlineKeyboardButton(text='Аризона', callback_data='ruarizona')
    button4 = types.InlineKeyboardButton(text='Вайоминг', callback_data='ruwyoming')
    button5 = types.InlineKeyboardButton(text='Колорадо', callback_data='rucolorado')
    button6 = types.InlineKeyboardButton(text='Миннесота', callback_data='ruminnesota')
    button7 = types.InlineKeyboardButton(text='Висконсин', callback_data='ruwisconsin')
    button8 = types.InlineKeyboardButton(text='Мичиган', callback_data='rumichigan')
    button9 = types.InlineKeyboardButton(text='Техас', callback_data='rutexas')
    button10 = types.InlineKeyboardButton(text='Нью-Йорк', callback_data='runewyork')
    button11 = types.InlineKeyboardButton(text='В главное меню', callback_data='mainrumenu')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'425b2fea40c9c3e6a431eec5bc08b6c1.jpg', 'rb'),caption='Выберите штат', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engstateback')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text='Washington', callback_data='engwashington')
    button2 = types.InlineKeyboardButton(text='California', callback_data='engcalifornia')
    button3 = types.InlineKeyboardButton(text='Arizona', callback_data='engarizona')
    button4 = types.InlineKeyboardButton(text='Wyoming', callback_data='engwyoming')
    button5 = types.InlineKeyboardButton(text='Colorado', callback_data='engcolorado')
    button6 = types.InlineKeyboardButton(text='Minnesota', callback_data='engminnesota')
    button7 = types.InlineKeyboardButton(text='Wisconsin', callback_data='engwisconsin')
    button8 = types.InlineKeyboardButton(text='Michigan', callback_data='engmichigan')
    button9 = types.InlineKeyboardButton(text='Texas', callback_data='engtexas')
    button10 = types.InlineKeyboardButton(text='New-York', callback_data='engnewyork')
    button11 = types.InlineKeyboardButton(text='To the main menu', callback_data='mainengmenu')
    markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'425b2fea40c9c3e6a431eec5bc08b6c1.jpg', 'rb'),caption='Select a state', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruwashington')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Washington', callback_data='ruuniwashington1')
    button2 = types.InlineKeyboardButton(text='Washington State University', callback_data='ruuniwashington2')
    button3 = types.InlineKeyboardButton(text='Western Washington University', callback_data='ruuniwashington3')
    button4 = types.InlineKeyboardButton(text='Gonzaga University', callback_data='ruuniwashington4')
    button5 = types.InlineKeyboardButton(text='Pacific Lutheran University', callback_data='ruuniwashington5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'washington-dc-gcffccf162_1920.jpg__0_0x0.jpg', 'rb'), caption='Штат Вашингтон находится на северо-востоке США на берегу Тихого океана, к югу от канадской провинции Британская Колумбия, к северу от штата Орегон и к западу от Айдахо. Его площадь составляет 184,8 км2, население — более 6 млн человек. Столица штата — город Олимпия, самые крупные города — Сиэтл, Спокан, Такома. Как добраться. Крупнейшие аэропорты штата Вашингтон находятся в 6 км от Олимпии, в Сиэтле и в Ситэке, между городами Сиэтл и Такома.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rucalifornia')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Stanford University', callback_data='ruunicalifornia1')
    button2 = types.InlineKeyboardButton(text='California Institute of Technology', callback_data='ruunicalifornia2')
    button3 = types.InlineKeyboardButton(text='University of Southern California', callback_data='ruunicalifornia3')
    button4 = types.InlineKeyboardButton(text='Pomona College', callback_data='ruunicalifornia4')
    button5 = types.InlineKeyboardButton(text='Claremont McKenna College', callback_data='ruunicalifornia5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'USA_Houses_Los_Angeles_California_Palms_599408_3840x2602.jpg', 'rb'), caption='Калифорния — самый населённый штат США (по результатам переписи населения США 2020 года) и 3-й по площади (после Аляски и Техаса). Столица — Сакраменто, крупнейший город — Лос-Анджелес. Другие крупные города: Сан-Франциско, Сан-Диего, Сан-Хосе. Штат известен своим разнообразным климатом, пёстрым составом населения. Калифорния занимает 1-е место среди штатов США по объёму ВВП.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruwyoming')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wyoming', callback_data='ruuniwyoming1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'37b3a423c55ff594f071f64fc69e2c13.jpg', 'rb'), caption='Штат Вайоминг находится на западе США и относится к группе Горных штатов в Скалистых горах системы Кордильер.Протяжённость штата с севера на юг составляет 450 км, а с запада на восток — 581 км. По площади он является 10-м штатом в США, занимая территорию 253 348 км².Столицей является самый крупный город штата — Шайенн.Вайоминг называют ковбойским штатом из-за того, что здесь издавна очень развито животноводство: разведение крупного рогатого скота и овечьи фермы.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rucolorado')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Colorado Boulder', callback_data='ruunicolorado1')
    button2 = types.InlineKeyboardButton(text='Colorado State University-Fort Collins', callback_data='ruunicolorado2')
    button3 = types.InlineKeyboardButton(text='University of Denver', callback_data='ruunicolorado3')
    button4 = types.InlineKeyboardButton(text='University of Northern Colorado', callback_data='ruunicolorado4')
    button5 = types.InlineKeyboardButton(text='Colorado College', callback_data='ruunicolorado5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'412110_10151699817105123_357683390122_23835258_81151115_o-e1576488076879.jpg', 'rb'), caption='Колора́до — 38-й (по порядку) штат США. Это Горный штат. На севере Колорадо граничит с Вайомингом и Небраской, на востоке со штатом Канзас, на юге с Оклахомой, Нью-Мексикой и Аризоной, и с Ютой на западе. Это 8-ой по площади штат Америки. Площадь Колорадо составляет 269,8 км², 37 % которой занимают национальные парки. Население штата составляет более 4,5 млн человек. Столицей и самым крупным городом Колорадо является Денвер.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruminnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Minnesota-Twin Cities', callback_data='ruuniminnesota1')
    button2 = types.InlineKeyboardButton(text='Mayo Clinic College of Medicine and Science', callback_data='ruuniminnesota2')
    button3 = types.InlineKeyboardButton(text='Carleton College', callback_data='ruuniminnesota3')
    button4 = types.InlineKeyboardButton(text='University of St Thomas-Minnesota', callback_data='ruuniminnesota4')
    button5 = types.InlineKeyboardButton(text='Saint Cloud State University', callback_data='ruuniminnesota5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1670456913_priroda-club-p-shtat-minnesota-priroda-krasivo-foto-34.jpg', 'rb'), caption='Миннесота (/ˌmɪnəˈsoʊtə / ⓘ MIN-á-SOH-tə) - штат в регионе Верхнего Среднего Запада Соединенных Штатов. Это 12-й по величине штат США по площади и 22-й по численности населения, с населением более 5,75 миллиона человек. Миннесота известна как "Страна 10 000 озер" за наличие более 14 000 водоемов с пресной водой площадью не менее десяти акров каждый; примерно треть территории штата покрыта лесами; большая часть остальной территории - прерии и сельскохозяйственные угодья.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruwisconsin')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wisconsin-Madison', callback_data='ruuniwisconsin1')
    button2 = types.InlineKeyboardButton(text='University of Wisconsin-Milwaukee', callback_data='ruuniwisconsin2')
    button3 = types.InlineKeyboardButton(text='Marquette University', callback_data='ruuniwisconsin3')
    button4 = types.InlineKeyboardButton(text='University of Wisconsin-Eau Claire', callback_data='ruuniwisconsin4')
    button5 = types.InlineKeyboardButton(text='Lawrence University', callback_data='ruuniwisconsin5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1579665460_8-p-shtat-viskonsin-15.jpg', 'rb'), caption='Висконсин — это штат в США, расположенный южнее Мичигана. Его площадь составляет 169,7 тыс. кв. км.Висконсин отличается разнообразными природно-климатическими условиями. Смешанные леса покрывают возвышенные участки, между которыми раскинулась сеть ледниковых озёр и рек. Низменные приозерные районы и плодородная Центральная равнина покрыты разнотравьем и сельхозугодиями.В штате можно найти уникальные формирования песчаника, а районы Айрон-Маунтин изобилуют хвойными лесами, мини-каньонами и горными пустошами.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rumichigan')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Michigan-Ann Arbor', callback_data='ruunimichigan1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'db328ba494fc76f0c4927a106b86dab0.jpeg', 'rb'), caption='Штат Мичиган расположен на Среднем Западе США в районе Великих озёр.Озеро Мичиган является единственным из Великих озёр, находящимся полностью в Соединенных Штатах. Остальная территория граничит с четырьмя из пяти Великих озёр.Мичиган делится на верхний и нижний полуостров проливом Макино, который соединяет озера Мичиган и Гурон. Две части штата связаны мостом — одним из самых длинных подвесных мостов в мире.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rutexas')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Texas at Austin', callback_data='ruunitexas1')
    button2 = types.InlineKeyboardButton(text='University of Houston', callback_data='ruunitexas2')
    button3 = types.InlineKeyboardButton(text='Rice University', callback_data='ruunitexas3')
    button4 = types.InlineKeyboardButton(text='Texas Tech University', callback_data='ruunitexas4')
    button5 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'capitol-building-aerial-skyline-sunset-austin-tx-texas-state-capital-501154548-58fd156b3df78ca159b45f04.jpg', 'rb'), caption='Техас — один из 50 штатов США. Был присоединен к стране указом президента 29 декабря 1845 года. Занимает второе место после Аляски по площади территории — 696 тысяч квадратных километров и второе место по численности населения после Калифорнии. По итогам переписи населения США 2020 года оно составило 29,1 миллиона человек.Столица штата — Остин, по административному делению состоит из 254 округов — это больше, чем у любого другого штата США.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'runewyork')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Cornell University', callback_data='ruuninewyork1')
    button2 = types.InlineKeyboardButton(text='Columbia University', callback_data='ruuninewyork2')
    button3 = types.InlineKeyboardButton(text='New York University', callback_data='ruuninewyork3')
    button4 = types.InlineKeyboardButton(text='University at Buffalo', callback_data='ruuninewyork4')
    button5 = types.InlineKeyboardButton(text='Bard College', callback_data='ruuninewyork5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'united-states-of-america-nyu-iork-23130.jpg', 'rb'), caption='Штат Нью-Йорк (State of New York).В северо-восточной части США вдоль побережья Атлантики раскинулся штат Нью-Йорк. Главным городом штата является город Олбани.На северо-востоке протянулась граница с Канадой, юго-восточную часть занимает побережье Атлантики, западнее расположены озера – Онтарио и Эри, южнее находится остров Лонг-Айленд.Значительную часть территории штата занимают реки и озера. Другая часть покрыта горными хребтами Аппалачи.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruarizona')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Arizona', callback_data='ruuniarizona1')
    button2 = types.InlineKeyboardButton(text='Arizona State University-Tempe', callback_data='ruuniarizona2')
    button3 = types.InlineKeyboardButton(text='Northern Arizona University', callback_data='ruuniarizona3')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'midtown-phoenix-skyline-night-1.jpg', 'rb'), caption='Аризона (англ. Arizona) – штат, расположенный на юго-западе Соединенных Штатов Америки. На востоке граничит с Нью-Мексико, на западе – с Калифорнией, на южной стороне с Мексикой и на северо-восточной – с Колорадо.Площадь 295 254 км². Столицей штата является город Финикс. Крупные города: Меса и Тусон. В 2011 году население составляло 6 482 505 человек (16-е место по численности). Территория делится на 15 графств.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engwashington')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Washington', callback_data='enguniwashington1')
    button2 = types.InlineKeyboardButton(text='Washington State University', callback_data='enguniwashington2')
    button3 = types.InlineKeyboardButton(text='Western Washington University', callback_data='enguniwashington3')
    button4 = types.InlineKeyboardButton(text='Gonzaga University', callback_data='enguniwashington4')
    button5 = types.InlineKeyboardButton(text='Pacific Lutheran University', callback_data='enguniwashington5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'washington-dc-gcffccf162_1920.jpg__0_0x0.jpg', 'rb'), caption='Washington State is located in the northeastern United States on the Pacific Ocean, south of the Canadian province of British Columbia, north of Oregon and west of Idaho. Its area is 184.8 km2, and its population is more than 6 million people. The capital of the state is the city of Olympia, the largest cities are Seattle, Spokane, Tacoma. How to get. The largest airports in Washington State are located 6 km from Olympia, in Seattle and in Sitek, between the cities of Seattle and Tacoma.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engcalifornia')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Stanford University', callback_data='engunicalifornia1')
    button2 = types.InlineKeyboardButton(text='California Institute of Technology', callback_data='engunicalifornia2')
    button3 = types.InlineKeyboardButton(text='University of Southern California', callback_data='engunicalifornia3')
    button4 = types.InlineKeyboardButton(text='Pomona College', callback_data='engunicalifornia4')
    button5 = types.InlineKeyboardButton(text='Claremont McKenna College', callback_data='engunicalifornia5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'USA_Houses_Los_Angeles_California_Palms_599408_3840x2602.jpg', 'rb'), caption='California is the most populous state in the United States (according to the results of the 2020 U.S. Census) and the 3rd largest by area (after Alaska and Texas). The capital is Sacramento, the largest city is Los Angeles. Other major cities: San Francisco, San Diego, San Jose. The state is known for its diverse climate and diverse population. California ranks 1st among the US states in terms of GDP.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engwyoming')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wyoming', callback_data='enguniwyoming1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'37b3a423c55ff594f071f64fc69e2c13.jpg', 'rb'), caption='Wyoming is located in the western United States and belongs to a group of Mountainous states in the Rocky Mountains of the Cordillera system.The length of the state from north to south is 450 km, and from west to east — 581 km. By area, it is the 10th state in the United States, covering an area of 253,348 km2.The capital is the largest city in the state — Cheyenne.Wyoming is called the cowboy state due to the fact that animal husbandry has long been very developed here: cattle breeding and sheep farms.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engcolorado')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Colorado Boulder', callback_data='engunicolorado1')
    button2 = types.InlineKeyboardButton(text='Colorado State University-Fort Collins', callback_data='engunicolorado2')
    button3 = types.InlineKeyboardButton(text='University of Denver', callback_data='engunicolorado3')
    button4 = types.InlineKeyboardButton(text='University of Northern Colorado', callback_data='engunicolorado4')
    button5 = types.InlineKeyboardButton(text='Colorado College', callback_data='engunicolorado5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'412110_10151699817105123_357683390122_23835258_81151115_o-e1576488076879.jpg', 'rb'), caption='Colorado is the 38th (in order) U.S. state. This is a Mountainous state. Colorado is bordered by Wyoming and Nebraska to the north, Kansas to the east, Oklahoma, New Mexico and Arizona to the south, and Utah to the west. It is the 8th largest state in America. The area of Colorado is 269.8 km2, 37% of which is occupied by national parks. The population of the state is more than 4.5 million people. The capital and largest city of Colorado is Denver.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engminnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Minnesota-Twin Cities', callback_data='enguniminnesota1')
    button2 = types.InlineKeyboardButton(text='Mayo Clinic College of Medicine and Science', callback_data='enguniminnesota2')
    button3 = types.InlineKeyboardButton(text='Carleton College', callback_data='uniminnesota3')
    button4 = types.InlineKeyboardButton(text='University of St Thomas-Minnesota', callback_data='enguniminnesota4')
    button5 = types.InlineKeyboardButton(text='Saint Cloud State University', callback_data='enguniminnesota5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1670456913_priroda-club-p-shtat-minnesota-priroda-krasivo-foto-34.jpg', 'rb'), caption='Minnesota (/ˌmɪnəˈsoʊtə / ⓘ MIN-á-SOH-tə) is a state in the Upper Midwest region of the United States. It is the 12th largest U.S. state by area and the 22nd largest by population, with a population of over 5.75 million people. Minnesota is known as the "Land of 10,000 Lakes" for having more than 14,000 freshwater reservoirs with an area of at least ten acres each; about a third of the state is covered with forests; most of the rest is prairie and farmland.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engwisconsin')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wisconsin-Madison', callback_data='enguniwisconsin1')
    button2 = types.InlineKeyboardButton(text='University of Wisconsin-Milwaukee', callback_data='enguniwisconsin2')
    button3 = types.InlineKeyboardButton(text='Marquette University', callback_data='enguniwisconsin3')
    button4 = types.InlineKeyboardButton(text='University of Wisconsin-Eau Claire', callback_data='enguniwisconsin4')
    button5 = types.InlineKeyboardButton(text='Lawrence University', callback_data='enguniwisconsin5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1579665460_8-p-shtat-viskonsin-15.jpg', 'rb'), caption='Wisconsin is a state in the United States located south of Michigan. Its area is 169.7 thousand square kilometers. Wisconsin is characterized by a variety of natural and climatic conditions. Mixed forests cover elevated areas, between which a network of glacial lakes and rivers stretches. The low-lying lake districts and the fertile Central Plain are covered with various grasses and farmlands.Unique sandstone formations can be found in the state, and the Iron Mountain areas are replete with coniferous forests, mini-canyons and mountain wastelands.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engmichigan')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Michigan-Ann Arbor', callback_data='engunimichigan1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'db328ba494fc76f0c4927a106b86dab0.jpeg', 'rb'), caption='The state of Michigan is located in the Midwestern United States in the Great Lakes region.Lake Michigan is the only one of the Great Lakes located entirely in the United States. The rest of the territory borders four of the five Great Lakes.Michigan is divided into the upper and lower peninsulas by the Strait of Mackinac, which connects Lakes Michigan and Huron. The two parts of the state are connected by a bridge — one of the longest suspension bridges in the world.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engtexas')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Texas at Austin', callback_data='engunitexas1')
    button2 = types.InlineKeyboardButton(text='University of Houston', callback_data='engunitexas2')
    button3 = types.InlineKeyboardButton(text='Rice University', callback_data='engunitexas3')
    button4 = types.InlineKeyboardButton(text='Texas Tech University', callback_data='engunitexas4')
    button5 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'capitol-building-aerial-skyline-sunset-austin-tx-texas-state-capital-501154548-58fd156b3df78ca159b45f04.jpg', 'rb'), caption='Texas is one of the 50 US states. It was annexed to the country by presidential decree on December 29, 1845. It occupies the second place after Alaska in terms of territory area — 696 thousand square kilometers and the second place in terms of population after California. According to the results of the 2020 U.S. census, it amounted to 29.1 million people.The capital of the state is Austin, which is administratively divided into 254 counties — this is more than any other US state.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engnewyork')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Cornell University', callback_data='enguninewyork1')
    button2 = types.InlineKeyboardButton(text='Columbia University', callback_data='enguninewyork2')
    button3 = types.InlineKeyboardButton(text='New York University', callback_data='enguninewyork3')
    button4 = types.InlineKeyboardButton(text='University at Buffalo', callback_data='enguninewyork4')
    button5 = types.InlineKeyboardButton(text='Bard College', callback_data='enguninewyork5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'united-states-of-america-nyu-iork-23130.jpg', 'rb'), caption='The State of New York.In the northeastern part of the United States, the state of New York stretches along the Atlantic coast. The main city of the state is the city of Albany.The border with Canada stretches to the northeast, the southeastern part is occupied by the Atlantic coast, lakes Ontario and Erie are located to the west, and Long Island is located to the south.A significant part of the states territory is occupied by rivers and lakes. The other part is covered by the Appalachian mountain ranges.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engarizona')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Arizona', callback_data='enguniarizona1')
    button2 = types.InlineKeyboardButton(text='Arizona State University-Tempe', callback_data='enguniarizona2')
    button3 = types.InlineKeyboardButton(text='Northern Arizona University', callback_data='enguniarizona3')
    button4 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'midtown-phoenix-skyline-night-1.jpg', 'rb'), caption='Arizona is a state located in the southwestern United States of America. It borders New Mexico to the east, California to the west, Mexico to the south, and Colorado to the northeast.The area is 295,254 km2. The capital of the state is the city of Phoenix. Major cities: Mesa and Tucson. In 2011, the population was 6,482,505 (16th largest). The territory is divided into 15 counties.', reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwashington1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.washington.edu/', callback_data='rusiteuniwashington1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'32155c917ef20f9879bd0da38cc84b20.jpg', 'rb'), caption='University of Washington (UW) — один из ведущих университетов США и мира. Расположен в самом сердце Северо-Западного побережья.Основан в 1861 году в Такоме, штат Вашингтон, как территориальный университет. В 1862 году переехал в Сиэтл и был переименован в Университет Вашингтона.Вуз славится своими исследовательскими программами и лабораториями, работающими в различных областях, включая медицину, технологии, науки о природе и многие другие.Университет постоянно расширяет число своих кампусов и модернизирует инфраструктуру, чтобы соответствовать потребностям студентов и исследовательским проектам.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwashington2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://wsu.edu/', callback_data='rusiteuniwashington2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'WSU-Spokane-scaled.jpg', 'rb'), caption='Университет штата Вашингтон — американский университет в городе Пулмен, штат Вашингтон.Он предлагает широкий спектр дисциплин, включая такие специализации, как инженерное дело, ветеринария, сельское хозяйство, медицина, естественные науки и многие другие.Университет является одним из ведущих государственных университетов Америки с высокой научно-исследовательской деятельностью по классификации Карнеги. Он был основан в 1890 году и является одним из старейших университетов на американском Западе.В настоящее время Университет штата Вашингтон имеет три филиала: WSU Spokane, WSU Tri-Cities и Washington State University Vancouver.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwashington3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.wwu.edu/', callback_data='siteuniwashington3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'c84750ff5b6ded030a08a0804b6f7e82.jpg', 'rb'), caption='Western Washington University – крупный американский университет в городе Беллингхем, штат Вашингтон. Существует с 1893 года. В Western учится 16 000 студентов. Они выбирают из 160 академических программ, среди которых антропология, математика, география, искусство, биология, история культуры, биохимия, медицина, юриспруденция, инженерия, кибербезопасность, танцы, философия или экономика.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwashington4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.gonzaga.edu/', callback_data='rusiteuniwashington4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'news4-1-5cf833947c545bdb.jpg', 'rb'), caption='Gonzaga University — это университет в США, основанный в 1887 году.Его гуманитарное наследие сосредоточено на обучении разума, тела и духа, а также на личном, академическом и профессиональном росте посредством критического мышления и творческих инноваций.В университете есть 92 направления и 26 программ магистратуры. Также есть программы подготовки к профессиональным школам в области бизнеса, образования, инженерии, стоматологии, богословия/теологии, права, медицины, сестринского дела и ветеринарии.Университет участвует в армейской программе ROTC, которая даёт возможность студентам после окончания учёбы стать офицерами.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwashington5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.plu.edu/', callback_data='rusiteuniwashington5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Screen-Shot-2016-12-14-at-5.12.21-PM.png', 'rb'), caption='Тихоокеанский лютеранский университет (PLU) - частный лютеранский университет в Паркленде, штат Вашингтон. Он был основан норвежскими лютеранскими иммигрантами в 1890 году. PLU спонсируется 580 конгрегациями региона I Евангелическо-лютеранской церкви в Америке. В плу обучается около 3100 студентов. По состоянию на 2017 год в школе работает около 220 штатных профессоров на территории лесного кампуса площадью 156 акров (63 га).', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackwashingtonuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Washington', callback_data='ruuniwashington1')
    button2 = types.InlineKeyboardButton(text='Washington State University', callback_data='ruuniwashington2')
    button3 = types.InlineKeyboardButton(text='Western Washington University', callback_data='ruuniwashington3')
    button4 = types.InlineKeyboardButton(text='Gonzaga University', callback_data='ruuniwashington4')
    button5 = types.InlineKeyboardButton(text='Pacific Lutheran University', callback_data='ruuniwashington5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'washington-dc-gcffccf162_1920.jpg__0_0x0.jpg', 'rb'), caption='Штат Вашингтон находится на северо-востоке США на берегу Тихого океана, к югу от канадской провинции Британская Колумбия, к северу от штата Орегон и к западу от Айдахо. Его площадь составляет 184,8 км2, население — более 6 млн человек. Столица штата — город Олимпия, самые крупные города — Сиэтл, Спокан, Такома. Как добраться. Крупнейшие аэропорты штата Вашингтон находятся в 6 км от Олимпии, в Сиэтле и в Ситэке, между городами Сиэтл и Такома.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicalifornia1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.stanford.edu/', callback_data='rusiteunicalifornia1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'scale_1200.jpeg', 'rb'), caption='Стэнфордский университет – огромный научно-исследовательский комплекс, объединяющий в себе 4 основных факультета: юридический, медицинский,экономический,технический. Здесь лучшие образовательные программы MBA в мире, десятки лабораторий, испытательных центров и, конечно, центр знаменитой Силиконовой долины. Таким образом, университет объединяет в себе две главнейших отрасли современного мира: крупный бизнес и высокие технологии.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicalifornia2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.caltech.edu/', callback_data='rusiteunicalifornia2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'scale_1200.png', 'rb'), caption='Калифорнийский технологический институт (Caltech) — частный исследовательский университет, расположенный в городе Пасадина в штате Калифорния.Это один из ведущих университетов США и один из двух самых важных, наряду с Массачусетским технологическим институтом, специализирующихся в точных науках и инженерии. Входит в десятку лучших университетов мира.Калтеху также принадлежит лаборатория реактивного движения, которая запускает большую часть автоматических космических аппаратов НАСА.В университете обучается около 1000 студентов и 1200 аспирантов.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicalifornia3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.usc.edu/', callback_data='rusiteunicalifornia3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'191112141459-01-university-of-southern-california-campus-file-scaled.jpg', 'rb'), caption='Университет Южной Калифорнии расположен в Лос-Анджелесе и является ведущим частным исследовательским университетом, глобальным центром искусства, технологий и международного бизнеса.В его состав входит до 21 академической школы и подразделения. В Медицинском кампусе находятся известные специализированные учреждения по лечению рака, изучению стволовых клеток и регенеративной медицины, ортопедии и спортивной медицине.Университет всегда занимает ведущие места в рейтингах частных университетов. Количество заявлений от первокурсников всегда очень высокое — более 64 000 заявок.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicalifornia4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.pomona.edu/', callback_data='rusiteunicalifornia4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'p2.jpg', 'rb'), caption='Помонский колледж — американский частный колледж свободных искусств в Клермонте (Калифорния).Основан 14 октября 1887 года группой христиан-конгрегационалистов, которые хотели воссоздать «типичный колледж Новой Англии» на территории Южной Калифорнии.Колледж предоставляет обучение по четырёхлетней программе бакалавриата. Около 1700 студентов обучаются 48 специальностям по гуманитарным дисциплинам и около 650 курсам. Также они имеют доступ к более чем 2000 дополнительным курсам в других колледжах Клермонта.Помонский колледж считается самым престижным гуманитарным колледжем на американском Западе и одним из самых престижных в стране.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicalifornia5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.cmc.edu/', callback_data='rusiteunicalifornia5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'claremont-mckenna-college-Victoire-Chalupy-wiki-58b5bdd63df78cdcd8b81643.jpg', 'rb'), caption='олледж Клермонт Маккенна (CMC) — частный гуманитарный колледж в Клермонте, Калифорния.В его учебной программе особое внимание уделяется государственному управлению, экономике, связям с общественностью, финансам и международным отношениям.Колледж был основан в 1946 году как мужской колледж, а в 1976 году стал совместным учебным заведением.В 2007 году он основал Школу экономики и финансов имени Роберта Дэя, которая предлагает магистерскую программу в области финансов.CMC известен консервативной политической ориентацией своего факультета по сравнению с аналогичными гуманитарными колледжами.По состоянию на 2019 год в университете насчитывалось 1338 студентов бакалавриата и аспирантуры.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackcaliforniauni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Stanford University', callback_data='ruunicalifornia1')
    button2 = types.InlineKeyboardButton(text='California Institute of Technology', callback_data='ruunicalifornia2')
    button3 = types.InlineKeyboardButton(text='University of Southern California', callback_data='ruunicalifornia3')
    button4 = types.InlineKeyboardButton(text='Pomona College', callback_data='unicalifornia4')
    button5 = types.InlineKeyboardButton(text='Claremont McKenna College', callback_data='ruunicalifornia5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'USA_Houses_Los_Angeles_California_Palms_599408_3840x2602.jpg', 'rb'),caption='Калифорния — самый населённый штат США (по результатам переписи населения США 2020 года) и 3-й по площади (после Аляски и Техаса). Столица — Сакраменто, крупнейший город — Лос-Анджелес. Другие крупные города: Сан-Франциско, Сан-Диего, Сан-Хосе. Штат известен своим разнообразным климатом, пёстрым составом населения. Калифорния занимает 1-е место среди штатов США по объёму ВВП.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwyoming1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.cmc.edu/', callback_data='rusiteuniuniwyoming15')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackwyominguni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'New_old_main_8d68026a-d9e5-4f61-bab1-70d1a903919b.jpg', 'rb'), caption='Университет Вайоминга — американский государственный университет, расположенный в Ларами, штат Вайоминг.Университет основан в сентябре 1886 года, то есть за четыре года до включения Вайоминга в состав США. Первых студентов университет принял в сентябре 1887 года.Вайомингский университет — национальный исследовательский центр, особенно в области защиты окружающей среды и природных ресурсов, со специализацией на агрокультуре, геологии и гидрологии.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackwyominguni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wyoming', callback_data='ruuniwyoming1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'37b3a423c55ff594f071f64fc69e2c13.jpg', 'rb'), caption='Штат Вайоминг находится на западе США и относится к группе Горных штатов в Скалистых горах системы Кордильер.Протяжённость штата с севера на юг составляет 450 км, а с запада на восток — 581 км. По площади он является 10-м штатом в США, занимая территорию 253 348 км².Столицей является самый крупный город штата — Шайенн.Вайоминг называют ковбойским штатом из-за того, что здесь издавна очень развито животноводство: разведение крупного рогатого скота и овечьи фермы.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicolorado1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.colorado.edu/https://www.colorado.edu/', callback_data='rusiteunicolorado1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'university-of-colorado-summer-14.jpg', 'rb'), caption='University of Colorado at Boulder (CU) — это университет государственного образца, функционирующий в лучших традициях обучения США.Преподавательский состав университета тщательно подбирается, благодаря чему он входит в список 200 лидеров в мире по качеству образования.CU известен своим активным участием в программе обмена студентами с другими университетами страны и за её пределами.Образовательная деятельность университета началась в 1876 году.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'ruunicolorado2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.colostate.edu/', callback_data='rusiteunicolorado2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1366_front.jpg', 'rb'), caption='Colorado State University находится в городе Форт-Коллинс, штат Колорадо, США.Он был основан в 1870 году как Сельскохозяйственный колледж Колорадо. В 1957 вуз был переименован в Государственный университет Колорадо.Colorado State реализует философию «земельных» колледжей: теоретические занятия в аудиториях здесь сочетаются с практикой в полевых и лабораторных условиях. Сегодня это один из ведущих научно-исследовательских институтов страны.Университет предлагает абитуриентам высшее образование мирового уровня: 65 программ бакалавриата, 55 — магистратуры, 40 — докторантуры, в том числе возможность получить степень доктора ветеринарной медицины.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicolorado3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.du.edu/', callback_data='rusiteunicolorado3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'e96b956b6b7b6f292f8acb15c9dd9d10.jpg', 'rb'), caption='Денверский университет (University of Denver) — частный исследовательский университет в городе Денвер, Колорадо, США.Аффилирован с Объединённой методистской церковью. Основан в 1864 году бывшим губернатором Колорадо Джоном Эвансом. Является старейшим частным университетом в регионе Скалистых гор.В университете обучается более 11 000 студентов. Кампус расположен в 11 км к югу от центра Денвера.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicolorado4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.unco.edu/', callback_data='rusiteunicolorado4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Wallpaper3.jpg', 'rb'), caption='Университет Северного Колорадо, основанный в 1889 году, находится в Грили, штат Колорадо. Вуз предлагает более 100 программ бакалавриата и более 100 программ магистратуры, обучая 13,035 студентов. Университет Северного Колорадо состоит из пяти колледжей педагогики и поведенческих наук, гуманитарных и социальных наук, естественных и медицинских наук, исполнительских и визуальных искусств и бизнеса.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunicolorado5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.coloradocollege.edu/', callback_data='rusiteunicolorado5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Colorado-College_Slocum-Hall_2012-Renovation-and-Addition_The-Treehouse.jpg', 'rb'), caption='Colorado College — это частный колледж в Колорадо, основанный в 1874 году Томасом Нельсоном Хаскеллом.Он известен своей уникальной системой «Block Plan», при которой студенты проходят один курс за раз в интенсивных 3,5-недельных блоках. Колледж расположен у подножия пика Пайкс, предлагая студентам уникальное сочетание городского и outdoor-experiences.В колледже предлагается более 40 специальностей и мини-специальностей, включая популярные программы в области экономики, экологии, политической науки, психологии и социологии.Студенты могут участвовать в более чем 100 студенческих клубах и организациях, а в колледже проводятся различные мероприятия в течение года, включая ежегодный летний музыкальный фестиваль Colorado College.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackunicolorado')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Colorado Boulder', callback_data='ruunicolorado1')
    button2 = types.InlineKeyboardButton(text='Colorado State University-Fort Collins', callback_data='ruunicolorado2')
    button3 = types.InlineKeyboardButton(text='University of Denver', callback_data='ruunicolorado3')
    button4 = types.InlineKeyboardButton(text='University of Northern Colorado', callback_data='ruunicolorado4')
    button5 = types.InlineKeyboardButton(text='Colorado College', callback_data='ruunicolorado5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'412110_10151699817105123_357683390122_23835258_81151115_o-e1576488076879.jpg', 'rb'),caption='Колора́до — 38-й (по порядку) штат США. Это Горный штат. На севере Колорадо граничит с Вайомингом и Небраской, на востоке со штатом Канзас, на юге с Оклахомой, Нью-Мексикой и Аризоной, и с Ютой на западе. Это 8-ой по площади штат Америки. Площадь Колорадо составляет 269,8 км², 37 % которой занимают национальные парки. Население штата составляет более 4,5 млн человек. Столицей и самым крупным городом Колорадо является Денвер.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniminnesota1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://twin-cities.umn.edu/', callback_data='rusiteuniminnesota1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'University-of-Minnesota-2.jpg', 'rb'), caption='Университет Миннесоты (UMN Twin Cities) — государственный исследовательский университет, предоставляющий земельные гранты в городах-побратимах Миннеаполисе и Сент-Поле, штат Миннесота, США.Кампус Twin Cities расположен в Миннеаполисе и Фалькон-Хайтс, пригороде Сент-Пола, примерно в 3 милях (4,8 км) друг от друга.Это ведущее учебное заведение системы Университета Миннесоты, состоящее из 19 колледжей, школ и других крупных академических подразделений.Университет предлагает 154 программы бакалавриата, 24 сертификата бакалавра, 307 программ магистратуры и 79 сертификатов выпускника.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniminnesota2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://college.mayo.edu/', callback_data='rusiteuniminnesota2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'173957-mayo-clinic-college-of-medicine-and-science.webp', 'rb'), caption='Медицинский и научный колледж клиники Майо (MCCMS) — это частный исследовательский университет, расположенный в Рочестере, штат Миннесота, США. Он готовит врачей, учёных и смежных медицинских работников.Колледж является частью академического медицинского центра клиники Майо и аккредитован Комиссией по высшему образованию (HLC).MCCMS состоит из пяти школ, которые предлагают доктора медицины, доктора философии и другие степени, а также медицинские ординатуры, стипендии и непрерывное медицинское образование (CME).Колледж базируется в Рочестере, штат Миннесота, с дополнительными кампусами в Финиксе и Скоттсдейле, штат Аризона, и Джексонвилле, штат Флорида.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniminnesota3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.carleton.edu/', callback_data='rusiteuniminnesota3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'carleton-college-2.jpg', 'rb'), caption='Карлтонский колледж (Carleton College) — частный гуманитарный колледж, расположенный в Нортфилде в Миннесоте.Он предлагает степень бакалавра, и в настоящее время в нём обучаются 2057 студентов.Карлтонский колледж часто входит в десятку лучших колледжей гуманитарных наук США. В 2015 году журнал US News & World Report поставил его на восьмое место по общему качеству и первое по качеству преподавания среди колледжей гуманитарных наук США.Среди выпускников Карлтонского колледжа были экономист Торстейн Веблен (1880), министр обороны 1969–1973 годов Мелвин Лэрд и генетик Мари-Клэр Кинг.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniminnesota4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.stthomas.edu/', callback_data='rusiteuniminnesota4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'7-5.jpg', 'rb'), caption='Частный католический исследовательский университет с кампусами в Сент-Поле и Миннеаполисе, штат Миннесота. Основанный в 1885 году как католическая семинария, он назван в честь Фомы Аквинского, средневекового католического богослова и философа, который является покровителем студентов. По состоянию на осень 2021 года в Сент-Томасе обучалось 9 347 студентов, что делает его крупнейшим частным некоммерческим университетом Миннесоты.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniminnesota5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.stcloudstate.edu/', callback_data='rusiteuniminnesota5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'636432483030335113-St.-Cloud-State-University1.webp', 'rb'), caption='Государственный университет Сент-Клауд (SCSU) — государственное некоммерческое учебное заведение, расположенное в городе Сен-Клу, США.SCSU является членом Minnesota State Colleges and Universities System и American Association of State Colleges and Universities (AASCU).Год основания университета — 1869.В вузе действует несколько программ финансовой поддержки, которые помогают учащимся покрывать часть расходов на обучение.Стоимость обучения для местных жителей начинается от 7 498 USD в год, для студентов из других стран — минимум 14 996 USD в год.У университета городской кампус, что открывает студентам много вариантов учебы и отдыха. В городе находятся крупные компании, которые предлагают стажировки. При учебном заведении есть библиотека.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackuniminnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Minnesota-Twin Cities', callback_data='ruuniminnesota1')
    button2 = types.InlineKeyboardButton(text='Mayo Clinic College of Medicine and Science',callback_data='ruuniminnesota2')
    button3 = types.InlineKeyboardButton(text='Carleton College', callback_data='ruuniminnesota3')
    button4 = types.InlineKeyboardButton(text='University of St Thomas-Minnesota', callback_data='ruuniminnesota4')
    button5 = types.InlineKeyboardButton(text='Saint Cloud State University', callback_data='ruuniminnesota5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'1670456913_priroda-club-p-shtat-minnesota-priroda-krasivo-foto-34.jpg', 'rb'),caption='Миннесота (/ˌmɪnəˈsoʊtə / ⓘ MIN-á-SOH-tə) - штат в регионе Верхнего Среднего Запада Соединенных Штатов. Это 12-й по величине штат США по площади и 22-й по численности населения, с населением более 5,75 миллиона человек. Миннесота известна как "Страна 10 000 озер" за наличие более 14 000 водоемов с пресной водой площадью не менее десяти акров каждый; примерно треть территории штата покрыта лесами; большая часть остальной территории - прерии и сельскохозяйственные угодья.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwisconsin1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.wisc.edu/', callback_data='rusiteuniwisconsin1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'social-card.jpg', 'rb'), caption='University of Wisconsin-Madison — это старейший и крупнейший вуз штата Висконсин, а также главный университет системы University of Wisconsin.Он был основан в 1848 году. В университете обучается почти 45 000 студентов, в том числе иностранные из 40 стран мира.Кампус университета находится в живописном месте между ботаническим садом и озёрами. На территории кампуса расположены 4 музея, спортивная арена, футбольный стадион, бассейны и спортивные центры.University of Wisconsin входит в число Public Ivy и занимает 13-е место среди американских государственных университетов. Он считается докторским университетом с очень высокой исследовательской активностью — на научные проекты тратится более 1,2 миллиарда долларов ежегодно.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwisconsin2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://uwm.edu/', callback_data='rusiteuniwisconsin2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'c7-4.jpg', 'rb'), caption='University of Wisconsin-Milwaukee — это общественный городской исследовательский университет, расположенный в городе Милуоки, штат Висконсин, США.Он был основан в 1956 году и предоставляет доступное образование мирового уровня для 27 000 студентов из 92 стран.В университете 15 школ и колледжей, включая единственные в Висконсине школы архитектуры, науки о пресной воде и здравоохранении. Он предлагает 195 академических программ бакалавриата, магистратуры, докторантуры, а также сертификатные и онлайн-курсы.Университет сотрудничает с ведущими компаниями в Висконсине и за его пределами. Он продвигает знания, выводит на рынок новые продукты, готовит студентов к работе на глобальном рынке труда.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwisconsin3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.marquette.edu/', callback_data='rusiteuniwisconsin3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'041815-marquette-lee-0179.jpg', 'rb'), caption='Marquette University — это приватный исследовательский университет, основанный в 1881 году. Он расположен в Милуоки, штат Висконсин, США.Университет предлагает широкий спектр программ обучения, включая бакалавриат, магистратуру и докторантуру. Студенты могут выбирать из более чем 80 специальностей и 80 миноров на уровне бакалавриата, а также из множества магистерских и докторских программ.Университет известен своими программами в области бизнеса, инженерии, коммуникаций, образования и права.Согласно международным экспертам, Marquette University занимает место в первых 5 процентах самых престижных учебных учреждений мира. При этом национальный академический рейтинг США относит его к 160 лучшим американским ВУЗам.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwisconsin4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.uwec.edu/', callback_data='rusiteuniwisconsin4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'20140911_CENTENNIAL_003.jpg', 'rb'), caption='Университет Висконсин–О–Клэр (UW-Eau Claire, UWEC или просто Eau Claire) — государственный университет в О–Клэр, штат Висконсин.Он является частью системы Висконсинского университета и предлагает степень бакалавра и магистра.Кампус состоит из 28 основных зданий, занимающих площадь 333 акра (135 га).Университет предлагает своим студентам возможность участвовать в национально признанной исследовательской программе через своё Управление исследований и спонсируемых программ (ORSP).', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniwisconsin5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.commonapp.org/explore/lawrence-university/', callback_data='rusiteuniwisconsin5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Main_Hall_at_Lawrence_University.jpg', 'rb'), caption='Lawrence University - это ведущий частный жилой гуманитарный колледж и музыкальная консерватория, специализирующаяся исключительно на бакалавриате. Сообщество Лоуренса, расположенное в гостеприимном Среднем Западе, штат Висконсин, с 15% его 1500 студентов из более чем 50 стран за пределами США, является одним из самых интернациональных в стране.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackuniwisconsin')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wisconsin-Madison', callback_data='ruuniwisconsin1')
    button2 = types.InlineKeyboardButton(text='University of Wisconsin-Milwaukee', callback_data='ruuniwisconsin2')
    button3 = types.InlineKeyboardButton(text='Marquette University', callback_data='ruuniwisconsin3')
    button4 = types.InlineKeyboardButton(text='University of Wisconsin-Eau Claire', callback_data='ruuniwisconsin4')
    button5 = types.InlineKeyboardButton(text='Lawrence University', callback_data='ruuniwisconsin5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1579665460_8-p-shtat-viskonsin-15.jpg', 'rb'), caption='Висконсин — это штат в США, расположенный южнее Мичигана. Его площадь составляет 169,7 тыс. кв. км.Висконсин отличается разнообразными природно-климатическими условиями. Смешанные леса покрывают возвышенные участки, между которыми раскинулась сеть ледниковых озёр и рек. Низменные приозерные районы и плодородная Центральная равнина покрыты разнотравьем и сельхозугодиями.В штате можно найти уникальные формирования песчаника, а районы Айрон-Маунтин изобилуют хвойными лесами, мини-каньонами и горными пустошами.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunimichigan1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='', callback_data='rusiteunimichigan1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackunimichigan')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'caption.jpg', 'rb'), caption='Мичиганский университет — государственный исследовательский университет в Анн-Арборе, штат Мичиган. Основан в 1817 году, это старейшее высшее учебное заведение штата.Мичиганский университет является одним из первых американских исследовательских университетов и членом-основателем Ассоциации американских университетов.Он состоит из девятнадцати колледжей и предлагает 250 дипломных программ на уровне бакалавриата и магистратуры по различным гуманитарным и STEM-дисциплинам.Университет аккредитован Комиссией по высшему образованию. В 2021 году он занял третье место среди американских университетов по расходам на исследования по данным Национального научного фонда.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackunimichigan')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Michigan-Ann Arbor', callback_data='ruunimichigan1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'db328ba494fc76f0c4927a106b86dab0.jpeg', 'rb'),caption='Штат Мичиган расположен на Среднем Западе США в районе Великих озёр.Озеро Мичиган является единственным из Великих озёр, находящимся полностью в Соединенных Штатах. Остальная территория граничит с четырьмя из пяти Великих озёр.Мичиган делится на верхний и нижний полуостров проливом Макино, который соединяет озера Мичиган и Гурон. Две части штата связаны мостом — одним из самых длинных подвесных мостов в мире.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniarizona1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.arizona.edu/', callback_data='rusiteuniarizona1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'734f715a9479442c44f75452ba10e45b.jpg', 'rb'), caption='University of Arizona (UA) – государственный исследовательский университет, расположенный в Тусоне, штат Аризона. Преподавательский состав является сильнейшим в регионе, где также работают лауреаты Нобелевской премии. The University Arizona работает с многочисленными предприятиями и даёт возможность как проводить исследования, так и проходить различные стажровки, что позволяет студентам достичь больших высот в своей области.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniarizona2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.asu.edu/academics/colleges-schools/tempe', callback_data='rusiteuniarizona2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Arizona_State_University,_Tempe_Main_Campus,_Tempe,_AZ_-_panoramio_(61).jpg', 'rb'), caption='Tempe — это кампус Arizona State University (ASU).Он предлагает студентам и выпускникам возможность заниматься многодисциплинарными исследованиями и исследованиями в первоклассных лабораториях и помещениях.На кампусе расположены:колледж Liberal Arts and Sciences;Herberger Institute for Design and the Arts;School for the Future of Innovation in Society;School of Sustainability.Также на кампусе находятся:Ira A. Fulton Schools of Engineering;Mary Lou Fulton Teachers College;W. P. Carey School of Business;University College;Barrett, The Honors College.Кампус Tempe отличается высокой экологичностью и предлагает лёгкий доступ ко всей столице Phoenix через общественный транспорт, включая лёгкую железную дорогу.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuniarizona3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://nau.edu/', callback_data='rusiteuniarizona3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'northern-arizona-university-twitter.webp', 'rb'), caption='Northern Arizona University (NAU) является публичным исследовательским университетом, расположенным в городе Флагстафф, штат Аризона. Основанный в 1899 году, NAU предлагает широкий спектр программ бакалавриата, магистратуры и докторантуры через свои колледжи и школы, включая Колледж искусств и письма, Колледж образования, Колледж инженерии, информатики и прикладных наук, Колледж здоровья и гуманитарных наук, The W. A. Franke College of Business и многие другие.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubackarizonauni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Arizona', callback_data='ruuniarizona1')
    button2 = types.InlineKeyboardButton(text='Arizona State University-Tempe', callback_data='ruuniarizona2')
    button3 = types.InlineKeyboardButton(text='Northern Arizona University', callback_data='ruuniarizona3')
    button4 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'midtown-phoenix-skyline-night-1.jpg', 'rb'),caption='Аризона (англ. Arizona) – штат, расположенный на юго-западе Соединенных Штатов Америки. На востоке граничит с Нью-Мексико, на западе – с Калифорнией, на южной стороне с Мексикой и на северо-восточной – с Колорадо.Площадь 295 254 км². Столицей штата является город Финикс. Крупные города: Меса и Тусон. В 2011 году население составляло 6 482 505 человек (16-е место по численности). Территория делится на 15 графств.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuninewyork1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.cornell.edu/', callback_data='rusiteuninewyork1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Campus image for fb.jpg', 'rb'), caption='Cornell University – частный исследовательский университет, основанный в 1865 году. Это единственный университет Лиги плюща, основанный после американской Войны за независимость. В Корнелле обучается 24,000 студентов. Корнеллский университет располагается в небольшом тихом городке Итака в Новой Англии, в четырех часах езды от Нью-Йорка.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuninewyork2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.columbia.edu/', callback_data='rusiteuninewyork2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'97281_original.png', 'rb'), caption='Columbia University — один из самых престижных и старейших частных университетов Америки. Расположен в районе Манхеттен в Нью-Йорке.Был основан в середине 18 века как Королевский колледж. Входит в «Лигу плюща» — образовательную элиту США.Среди выпускников и преподавателей Колумбийского университета несколько президентов Америки, главы других государств, лауреаты премии «Оскар» и Нобелевской премии.Главный кампус расположен в сердце Нью-Йорка, на Манхеттене. Он занимает 13 гектаров земли. На кампусах университета есть всё для жизни и учебы: библиотеки, лаборатории, инфраструктура для занятий спортом, медицинский центр.Для студентов работают более 500 организаций и кружков по интересам.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuninewyork3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.nyu.edu/', callback_data='rusiteuninewyork3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'nyu-stern.webp', 'rb'), caption='Нью-Йоркский университет — частный исследовательский университет США, расположенный в Нью-Йорке. Один из наиболее известных и престижных высших учебных заведений мира.В 2020 году Нью-Йоркский университет занял 11 место среди лучших университетов США и 35 место среди лучших университетов мира в рейтинге Quacquarelli Symonds (QS).Университет является самым крупным научно-исследовательским частным университетом Соединённых Штатов. В нём обучаются более 51 тысячи студентов.Нью-Йоркский университет состоит из 16 школ, институтов и колледжей. Главный корпус университета располагается в Гринвич-Виллидж в Манхеттене.Университет является членом Ассоциации американских университетов, объединяющей с 1900 года ведущие научно-исследовательские университеты Северной Америки.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuninewyork4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.buffalo.edu/', callback_data='rusiteuninewyork4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'buffalo-state.jpg', 'rb'), caption='Университет в Буффало (UB) — государственный исследовательский университет с кампусами в Буффало и Амхерсте, штат Нью-Йорк, США.Университет был основан в 1846 году как частный медицинский колледж, а в 1962 году объединился с системой Государственного университета Нью-Йорка.По состоянию на 2022 год это одно из двух ведущих учебных заведений системы SUNY.Университет предлагает степени бакалавра по более чем 140 областям обучения, а также более 220 магистерских программ и более 95 докторских программ.В 1989 году UB был избран в Ассоциацию американских университетов.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruuninewyork5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.commonapp.org/explore/bard-college/', callback_data='rusiteuninewyork5')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'bard-college-campus_1130x500_acf_cropped.jpg', 'rb'), caption='Бард-колледж (англ. Bard College, сокращённо Бард) — престижный частный гуманитарный университет свободных искусств и наук, расположенный в Аннандейл-на-Гудзоне, округ Датчесс, штат Нью-Йорк. Является Национальным историческим памятником США.В состав учреждения входит одна из самых молодых и прогрессивных консерваторий Америки.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubacknewyorkuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Cornell University', callback_data='ruuninewyork1')
    button2 = types.InlineKeyboardButton(text='Columbia University', callback_data='ruuninewyork2')
    button3 = types.InlineKeyboardButton(text='New York University', callback_data='ruuninewyork3')
    button4 = types.InlineKeyboardButton(text='University at Buffalo', callback_data='ruuninewyork4')
    button5 = types.InlineKeyboardButton(text='Bard College', callback_data='ruuninewyork5')
    button6 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'united-states-of-america-nyu-iork-23130.jpg', 'rb'),caption='Штат Нью-Йорк (State of New York).В северо-восточной части США вдоль побережья Атлантики раскинулся штат Нью-Йорк. Главным городом штата является город Олбани.На северо-востоке протянулась граница с Канадой, юго-восточную часть занимает побережье Атлантики, западнее расположены озера – Онтарио и Эри, южнее находится остров Лонг-Айленд.Значительную часть территории штата занимают реки и озера. Другая часть покрыта горными хребтами Аппалачи.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunitexas1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.utexas.edu/', callback_data='rusiteunitexas1')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubackntexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'BostonEntrance_10rs.jpg', 'rb'), caption='University of Texas at Austin — государственный университет в Остине, штат Техас, США.Он был основан в 1883 году и является одним из самых крупных в стране и самым большим в Техасе.Университет активно занимается исследованиями, значимыми для общества, привлекая студентов и преподавателей к решению задач и вызовов науки. Сумма финансирования научных исследований на базе вуза составляет более 400 миллионов долларов.Университет предлагает широкий выбор специальностей — гуманитарных, технических, классических и узкого профиля.Он расположен в центре Остина, кампус городского типа площадью 437 акров. В состав кампуса входит 9 академических университетов и 6 государственных медицинских учреждений.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunitexas2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://uh.edu/', callback_data='rusiteunitexas2')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacktexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'825_585_uh.jpg', 'rb'), caption='Хью́стонский университет (англ. University of Houston) — общественный исследовательский университет в США, расположенный в Хьюстоне, штат Техас. Крупнейший и главный кампус в cистеме Хьюстонского университета (UHS), а также 3-й по величине университет в штате. Изданием The Princeton Review был причислен к одному из лучших университетов США, а также входит в число первых 300 университетов в Академическом рейтинге университетов мира.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunitexas3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.rice.edu/', callback_data='rusiteunitexas3')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacktexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'lovettbirdseye.jpg', 'rb'), caption='Rice University (полное название — Университет Уильяма Марша Райса) — это престижный частный университет, расположенный в городе Хьюстон, штат Техас.Он был основан в 1891 году бизнесменом Уильямом Маршем Райсом, который оставил большую часть своего состояния на создание учебного заведения.Сегодня вуз входит в число лучших заведений США, стабильно находится в топ-20. Ежегодно на исследования выделяются огромные средства, работает множество профессиональных исследовательских центров и групп (более 100).В Rice University действуют отделения бакалавриата, магистратуры и докторантуры, есть возможность проходить краткосрочные и дополнительные курсы.Выпускники с дипломами Rice University ценятся как прекрасные специалисты в своих областях.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'ruunitexas4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Сайт', url='https://www.ttu.edu/', callback_data='rusiteunitexas4')
    button2 = types.InlineKeyboardButton(text='Назад', callback_data='rubacktexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'texas-tech-university-health-sciences-center-2.jpg', 'rb'), caption='Техасский технологический университет, основанный в 1923 году в Лаббоке, штат Техас, также известен как Техасский технологический колледж. В данный момент в вузе учится 28,422 студента. Университет предлагает академические программы на базе колледжей и школ сельскохозяйственных наук и природных ресурсов, инженерии, искусств и наук, массовых коммуникаций, визуальных и исполнительских искусств, общественных услуг, архитектуры, бизнеса, педагогики и права.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'rubacktexasuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Texas at Austin', callback_data='ruuniexas1')
    button2 = types.InlineKeyboardButton(text='University of Houston', callback_data='ruunitexas2')
    button3 = types.InlineKeyboardButton(text='Rice University', callback_data='ruunitexas3')
    button4 = types.InlineKeyboardButton(text='Texas Tech University', callback_data='ruunitexas4')
    button5 = types.InlineKeyboardButton(text='Назад', callback_data='rustateback')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'capitol-building-aerial-skyline-sunset-austin-tx-texas-state-capital-501154548-58fd156b3df78ca159b45f04.jpg','rb'),caption='Техас — один из 50 штатов США. Был присоединен к стране указом президента 29 декабря 1845 года. Занимает второе место после Аляски по площади территории — 696 тысяч квадратных километров и второе место по численности населения после Калифорнии. По итогам переписи населения США 2020 года оно составило 29,1 миллиона человек.Столица штата — Остин, по административному делению состоит из 254 округов — это больше, чем у любого другого штата США.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwashington1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.washington.edu/', callback_data='engsiteuniwashington1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'32155c917ef20f9879bd0da38cc84b20.jpg', 'rb'), caption='The University of Washington (UW) is one of the leading universities in the USA and the world. Located in the heart of the Northwest Coast.It was founded in 1861 in Tacoma, Washington, as a territorial university. In 1862, he moved to Seattle and was renamed the University of Washington.The university is famous for its research programs and laboratories working in various fields, including medicine, technology, natural sciences and many others.The University is constantly expanding the number of its campuses and modernizing its infrastructure to meet the needs of students and research projects.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwashington2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://wsu.edu/', callback_data='engsiteuniwashington2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'WSU-Spokane-scaled.jpg', 'rb'), caption='Washington State University is an American university in Pullman, Washington.It offers a wide range of disciplines, including specializations such as engineering, veterinary medicine, agriculture, medicine, natural sciences and many others.The University is one of the leading public universities in America with high research activity according to the Carnegie classification. It was founded in 1890 and is one of the oldest universities in the American West.Washington State University currently has three branches: WSU Spokane, WSU Tri-Cities and Washington State University Vancouver.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwashington3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.wwu.edu/', callback_data='engsiteuniwashington3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'c84750ff5b6ded030a08a0804b6f7e82.jpg', 'rb'), caption='Western Washington University is a major American university in Bellingham, Washington. It has been in existence since 1893. There are 16,000 students studying at Western. They choose from 160 academic programs, including anthropology, mathematics, geography, art, biology, cultural history, biochemistry, medicine, law, engineering, cybersecurity, dance, philosophy or economics.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwashington4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.gonzaga.edu/', callback_data='engsiteuniwashington4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'news4-1-5cf833947c545bdb.jpg', 'rb'), caption='Gonzaga University is a university in the United States, founded in 1887.His humanitarian legacy focuses on the training of the mind, body and spirit, as well as personal, academic and professional growth through critical thinking and creative innovation.The university has 92 courses and 26 masters degree programs. There are also training programs for professional schools in the fields of business, education, engineering, dentistry, theology/theology, law, medicine, nursing and veterinary medicine.The university participates in the Army ROTC program, which gives students the opportunity to become officers after graduation.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwashington5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.plu.edu/', callback_data='engsiteuniwashington5')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackwashingtonuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Screen-Shot-2016-12-14-at-5.12.21-PM.png', 'rb'), caption='Pacific Lutheran University (PLU) is a private Lutheran university in Parkland, Washington. It was founded by Norwegian Lutheran immigrants in 1890. PLU is sponsored by 580 congregations of the Region I Evangelical Lutheran Church in America. About 3,100 students study at PLU. As of 2017, the school has about 220 full-time professors on a 156-acre (63 ha) forest campus.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackwashingtonuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Washington', callback_data='enguniwashington1')
    button2 = types.InlineKeyboardButton(text='Washington State University', callback_data='enguniwashington2')
    button3 = types.InlineKeyboardButton(text='Western Washington University', callback_data='enguniwashington3')
    button4 = types.InlineKeyboardButton(text='Gonzaga University', callback_data='enguniwashington4')
    button5 = types.InlineKeyboardButton(text='Pacific Lutheran University', callback_data='enguniwashington5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'washington-dc-gcffccf162_1920.jpg__0_0x0.jpg', 'rb'), caption='Washington State is located in the northeastern United States on the Pacific Ocean, south of the Canadian province of British Columbia, north of Oregon and west of Idaho. Its area is 184.8 km2, and its population is more than 6 million people. The capital of the state is the city of Olympia, the largest cities are Seattle, Spokane, Tacoma. How to get. The largest airports in Washington State are located 6 km from Olympia, in Seattle and in Sitek, between the cities of Seattle and Tacoma.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicalifornia1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.stanford.edu/', callback_data='engsiteunicalifornia1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'scale_1200.jpeg', 'rb'), caption='Stanford University is a huge research complex that combines 4 main faculties: law, medicine, economics, and technology. It has the best MBA educational programs in the world, dozens of laboratories, testing centers and, of course, the center of the famous Silicon Valley. Thus, the university combines two of the most important branches of the modern world: big business and high technology.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicalifornia2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.caltech.edu/', callback_data='engsiteunicalifornia2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'scale_1200.png', 'rb'), caption='The California Institute of Technology (Caltech) is a private research university located in Pasadena, California.It is one of the leading universities in the United States and one of the two most important, along with the Massachusetts Institute of Technology, specializing in exact sciences and engineering. It is one of the top ten universities in the world.Caltech also owns the Jet Propulsion Laboratory, which launches most of NASAs automated spacecraft.The university has about 1,000 students and 1,200 graduate students.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicalifornia3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.usc.edu/', callback_data='engsiteunicalifornia3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'191112141459-01-university-of-southern-california-campus-file-scaled.jpg', 'rb'), caption='The University of Southern California is located in Los Angeles and is a leading private research university, a global center for art, technology and international business.It includes up to 21 academic schools and divisions. The Medical Campus houses well-known specialized institutions for cancer treatment, stem cell research and regenerative medicine, orthopedics and sports medicine.The university always occupies leading positions in the rankings of private universities. The number of applications from freshmen is always very high — more than 64,000 applications.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicalifornia4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.pomona.edu/', callback_data='engsiteunicalifornia4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'p2.jpg', 'rb'), caption='Pomona College is an American private liberal arts college in Claremont, California.It was founded on October 14, 1887 by a group of congregationalist Christians who wanted to recreate a "typical New England college" in Southern California.The college provides training in a four-year bachelors degree program. About 1,700 students study 48 specialties in the humanities and about 650 courses. They also have access to more than 2,000 additional courses at other Claremont colleges.Pomona College is considered the most prestigious liberal arts college in the American West and one of the most prestigious in the country.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicalifornia5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.cmc.edu/', callback_data='engsiteunicalifornia5')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackcaliforniauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'claremont-mckenna-college-Victoire-Chalupy-wiki-58b5bdd63df78cdcd8b81643.jpg', 'rb'), caption='Claremont McKenna College (CMC) is a private liberal arts college in Claremont, California.His curriculum focuses on public administration, economics, public relations, finance and international relations.The college was founded in 1946 as a mens college, and became a co-educational institution in 1976.In 2007, he founded the Robert Day School of Economics and Finance, which offers a masters degree program in finance.CMC is known for the conservative political orientation of its faculty compared to similar liberal arts colleges.As of 2019, there were 1,338 undergraduate and postgraduate students at the university.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackcaliforniauni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Stanford University', callback_data='engunicalifornia1')
    button2 = types.InlineKeyboardButton(text='California Institute of Technology', callback_data='engunicalifornia2')
    button3 = types.InlineKeyboardButton(text='University of Southern California', callback_data='engunicalifornia3')
    button4 = types.InlineKeyboardButton(text='Pomona College', callback_data='engunicalifornia4')
    button5 = types.InlineKeyboardButton(text='Claremont McKenna College', callback_data='engunicalifornia5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'USA_Houses_Los_Angeles_California_Palms_599408_3840x2602.jpg', 'rb'),caption='California is the most populous state in the United States (according to the results of the 2020 U.S. Census) and the 3rd largest by area (after Alaska and Texas). The capital is Sacramento, the largest city is Los Angeles. Other major cities: San Francisco, San Diego, San Jose. The state is known for its diverse climate and diverse population. California ranks 1st among the US states in terms of GDP.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwyoming1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.cmc.edu/', callback_data='engsiteuniuniwyoming15')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackwyominguni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'New_old_main_8d68026a-d9e5-4f61-bab1-70d1a903919b.jpg', 'rb'), caption='The University of Wyoming is an American public university located in Laramie, Wyoming.The university was founded in September 1886, that is, four years before Wyoming was incorporated into the United States. The university accepted its first students in September 1887.The University of Wyoming is a national research center, especially in the field of environmental protection and natural resources, with a specialization in agriculture, geology and hydrology.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackwyominguni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wyoming', callback_data='enguniwyoming1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'37b3a423c55ff594f071f64fc69e2c13.jpg', 'rb'), caption='Wyoming is located in the western United States and belongs to a group of Mountainous states in the Rocky Mountains of the Cordillera system.The length of the state from north to south is 450 km, and from west to east — 581 km. By area, it is the 10th state in the United States, covering an area of 253,348 km2.The capital is the largest city in the state — Cheyenne.Wyoming is called the cowboy state due to the fact that animal husbandry has long been very developed here: cattle breeding and sheep farms.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicolorado1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.colorado.edu/https://www.colorado.edu/', callback_data='engsiteunicolorado1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'university-of-colorado-summer-14.jpg', 'rb'), caption='The University of Colorado at Boulder (CU) is a state—owned university operating in the best traditions of U.S. education.The teaching staff of the university is carefully selected, which makes it one of the 200 leaders in the world in terms of education quality.CU is known for its active participation in the student exchange program with other universities in the country and abroad.The educational activity of the university began in 1876.', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'engunicolorado2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.colostate.edu/', callback_data='engsiteunicolorado2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1366_front.jpg', 'rb'), caption='Colorado State University is located in Fort Collins, Colorado, USA.It was founded in 1870 as the Colorado Agricultural College. In 1957, the university was renamed Colorado State University.Colorado State implements the philosophy of "land-based" colleges: theoretical classes in classrooms are combined with practice in the field and laboratory conditions. Today it is one of the leading research institutes in the country.The University offers applicants a world—class higher education: 65 bachelors degree programs, 55 masters degree programs, 40 doctoral programs, including the opportunity to obtain a doctor of veterinary medicine degree.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicolorado3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.du.edu/', callback_data='engsiteunicolorado3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'e96b956b6b7b6f292f8acb15c9dd9d10.jpg', 'rb'), caption='The University of Denver is a private research university in Denver, Colorado, USA.Affiliated with the United Methodist Church. It was founded in 1864 by former Colorado Governor John Evans. It is the oldest private university in the Rocky Mountain region.The university has more than 11,000 students. The campus is located 11 km south of downtown Denver.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicolorado4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.unco.edu/', callback_data='engsiteunicolorado4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Wallpaper3.jpg', 'rb'), caption='The University of Northern Colorado, founded in 1889, is located in Greeley, Colorado. The university offers more than 100 bachelors degree programs and more than 100 masters degree programs, educating 13,035 students. The University of Northern Colorado consists of five colleges of education and behavioral sciences, humanities and Social Sciences, natural and medical sciences, performing and Visual Arts, and Business.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunicolorado5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.coloradocollege.edu/', callback_data='engsiteunicolorado5')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackunicolorado')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Colorado-College_Slocum-Hall_2012-Renovation-and-Addition_The-Treehouse.jpg', 'rb'), caption='Colorado College is a private college in Colorado founded in 1874 by Thomas Nelson Haskell.It is known for its unique "Block Plan" system, in which students take one course at a time in intensive 3.5-week blocks. The college is located at the foot of Pikes Peak, offering students a unique mix of urban and outdoor experiences.The college offers more than 40 majors and mini-majors, including popular programs in economics, ecology, political science, psychology and sociology.Students can participate in over 100 student clubs and organizations, and the college hosts various events throughout the year, including the annual Colorado College Summer Music Festival.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackunicolorado')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Colorado Boulder', callback_data='engunicolorado1')
    button2 = types.InlineKeyboardButton(text='Colorado State University-Fort Collins', callback_data='engunicolorado2')
    button3 = types.InlineKeyboardButton(text='University of Denver', callback_data='engunicolorado3')
    button4 = types.InlineKeyboardButton(text='University of Northern Colorado', callback_data='engunicolorado4')
    button5 = types.InlineKeyboardButton(text='Colorado College', callback_data='engunicolorado5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'412110_10151699817105123_357683390122_23835258_81151115_o-e1576488076879.jpg', 'rb'),caption='Colorado is the 38th (in order) U.S. state. This is a Mountainous state. Colorado is bordered by Wyoming and Nebraska to the north, Kansas to the east, Oklahoma, New Mexico and Arizona to the south, and Utah to the west. It is the 8th largest state in America. The area of Colorado is 269.8 km2, 37% of which is occupied by national parks. The population of the state is more than 4.5 million people. The capital and largest city of Colorado is Denver.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniminnesota1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://twin-cities.umn.edu/', callback_data='engsiteuniminnesota1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'University-of-Minnesota-2.jpg', 'rb'), caption='The University of Minnesota (UMN Twin Cities) is a public research university providing land grants in the twin cities of Minneapolis and St. Paul, Minnesota, USA.The Twin Cities campus is located in Minneapolis and Falcon Heights, a suburb of St. Paul, about 3 miles (4.8 km) apart.It is the leading educational institution of the University of Minnesota system, consisting of 19 colleges, schools and other large academic units.The University offers 154 bachelors degree programs, 24 bachelors certificates, 307 Masters degree programs and 79 graduate certificates.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniminnesota2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://college.mayo.edu/', callback_data='engsiteuniminnesota2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'173957-mayo-clinic-college-of-medicine-and-science.webp', 'rb'), caption='The Mayo Clinic College of Medicine and Science (MCCMS) is a private research university located in Rochester, Minnesota, USA. It trains doctors, scientists and related medical professionals.The college is part of the Mayo Clinic Academic Medical Center and is accredited by the Commission on Higher Education (HLC).MCCMS consists of five schools that offer M.D., Ph.D., and other degrees, as well as medical residency, scholarships, and Continuing Medical Education (CME).The college is based in Rochester, Minnesota, with additional campuses in Phoenix and Scottsdale, Arizona, and Jacksonville, Florida.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniminnesota3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.carleton.edu/', callback_data='engsiteuniminnesota3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'carleton-college-2.jpg', 'rb'), caption='Carleton College is a private liberal arts college located in Northfield, Minnesota.It offers a bachelors degree and currently has 2,057 students enrolled.Carleton College is often ranked among the top ten liberal arts colleges in the United States. In 2015, US News & World Report magazine ranked it eighth in overall quality and first in teaching quality among US liberal arts colleges.Among the graduates of Carleton College were economist Thorstein Veblen (1880), Secretary of Defense 1969-1973 Melvin Laird and geneticist Marie-Claire King.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniminnesota4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.stthomas.edu/', callback_data='engsiteuniminnesota4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'7-5.jpg', 'rb'), caption='A private Catholic research university with campuses in St. Paul and Minneapolis, Minnesota. Founded in 1885 as a Catholic seminary, it is named after Thomas Aquinas, a medieval Catholic theologian and philosopher who is the patron saint of students. As of fall 2021, St. Thomas had 9,347 students enrolled, making it the largest private, non-profit university in Minnesota.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniminnesota5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.stcloudstate.edu/', callback_data='engsiteuniminnesota5')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniminnesota')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'636432483030335113-St.-Cloud-State-University1.webp', 'rb'), caption='St. Cloud State University (SCSU) is a public, non—profit educational institution located in Saint Cloud, USA.SCSU is a member of the Minnesota State Colleges and Universities System and the American Association of State Colleges and Universities (AASCU).The year of foundation of the university is 1869.The university has several financial support programs that help students cover part of their tuition costs.Tuition for local residents starts from 7,498 USD per year, for students from other countries — at least 14,996 USD per year.The university has an urban campus, which opens up many options for students to study and relax. There are large companies in the city that offer internships. There is a library attached to the educational institution.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackuniminnesota')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Minnesota-Twin Cities', callback_data='enguniminnesota1')
    button2 = types.InlineKeyboardButton(text='Mayo Clinic College of Medicine and Science',callback_data='enguniminnesota2')
    button3 = types.InlineKeyboardButton(text='Carleton College', callback_data='enguniminnesota3')
    button4 = types.InlineKeyboardButton(text='University of St Thomas-Minnesota', callback_data='enguniminnesota4')
    button5 = types.InlineKeyboardButton(text='Saint Cloud State University', callback_data='enguniminnesota5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id,photo=open(r'1670456913_priroda-club-p-shtat-minnesota-priroda-krasivo-foto-34.jpg', 'rb'),caption='Minnesota (/ˌmɪnəˈsoʊtə / ⓘ MIN-á-SOH-tə) is a state in the Upper Midwest region of the United States. It is the 12th largest U.S. state by area and the 22nd largest by population, with a population of over 5.75 million people. Minnesota is known as the "Land of 10,000 Lakes" for having more than 14,000 freshwater reservoirs with an area of at least ten acres each; about a third of the state is covered with forests; most of the rest is prairie and farmland.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwisconsin1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.wisc.edu/', callback_data='engsiteuniwisconsin1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'social-card.jpg', 'rb'), caption='The University of Wisconsin-Madison is the oldest and largest university in the state of Wisconsin, as well as the main university of the University of Wisconsin system.It was founded in 1848. The university has almost 45,000 students, including foreign students from 40 countries around the world.The university campus is located in a picturesque location between the botanical garden and the lakes. There are 4 museums, a sports arena, a football stadium, swimming pools and sports centers on the campus.The University of Wisconsin is among the Public Ivy and ranks 13th among American public universities. It is considered a doctoral university with a very high research activity — more than $ 1.2 billion is spent on research projects annually.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwisconsin2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://uwm.edu/', callback_data='engsiteuniwisconsin2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'c7-4.jpg', 'rb'), caption='The University of Wisconsin-Milwaukee is a public urban research university located in Milwaukee, Wisconsin, USA.It was founded in 1956 and provides world-class affordable education to 27,000 students from 92 countries.The university has 15 schools and colleges, including Wisconsins only schools of architecture, freshwater science, and healthcare. It offers 195 academic bachelors, masters, and doctoral degree programs, as well as certificate and online courses.The University cooperates with leading companies in Wisconsin and beyond. It promotes knowledge, introduces new products to the market, and prepares students to work in the global labor market.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwisconsin3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.marquette.edu/', callback_data='engsiteuniwisconsin3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'041815-marquette-lee-0179.jpg', 'rb'), caption='Marquette University is a private research university founded in 1881. It is located in Milwaukee, Wisconsin, USA.The University offers a wide range of study programs, including bachelors, masters and doctoral degrees. Students can choose from over 80 majors and 80 minors at the undergraduate level, as well as from a variety of masters and doctoral programs.The University is known for its programs in business, engineering, communications, education and law.According to international experts, Marquette University ranks in the top 5 percent of the most prestigious educational institutions in the world. At the same time, the US national academic ranking ranks it among the 160 best American universities.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwisconsin4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.uwec.edu/', callback_data='engsiteuniwisconsin4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'20140911_CENTENNIAL_003.jpg', 'rb'), caption='The University of Wisconsin–Eau Claire (UW-Eau Claire, UWEC or simply Eau Claire) is a public university in Eau Claire, Wisconsin.It is part of the University of Wisconsin system and offers bachelors and masters degrees.The campus consists of 28 main buildings covering an area of 333 acres (135 ha).The University offers its students the opportunity to participate in a nationally recognized research program through its Office of Research and Sponsored Programs (ORSP).', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniwisconsin5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.commonapp.org/explore/lawrence-university/', callback_data='engsiteuniwisconsin5')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackuniwisconsin')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Main_Hall_at_Lawrence_University.jpg', 'rb'), caption='Lawrence University is a leading private residential liberal arts college and music conservatory specializing exclusively in undergraduate studies. The Lawrence community, located in the welcoming Midwest, Wisconsin, with 15% of its 1,500 students from more than 50 countries outside the United States, is one of the most international in the country.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackuniwisconsin')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Wisconsin-Madison', callback_data='enguniwisconsin1')
    button2 = types.InlineKeyboardButton(text='University of Wisconsin-Milwaukee', callback_data='enguniwisconsin2')
    button3 = types.InlineKeyboardButton(text='Marquette University', callback_data='enguniwisconsin3')
    button4 = types.InlineKeyboardButton(text='University of Wisconsin-Eau Claire', callback_data='enguniwisconsin4')
    button5 = types.InlineKeyboardButton(text='Lawrence University', callback_data='enguniwisconsin5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='stateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'1579665460_8-p-shtat-viskonsin-15.jpg', 'rb'), caption='Wisconsin is a state in the United States located south of Michigan. Its area is 169.7 thousand square kilometers. Wisconsin is characterized by a variety of natural and climatic conditions. Mixed forests cover elevated areas, between which a network of glacial lakes and rivers stretches. The low-lying lake districts and the fertile Central Plain are covered with various grasses and farmlands.Unique sandstone formations can be found in the state, and the Iron Mountain areas are replete with coniferous forests, mini-canyons and mountain wastelands.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunimichigan1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='', callback_data='engsiteunimichigan1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackunimichigan')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'caption.jpg', 'rb'), caption='The University of Michigan is a public research university in Ann Arbor, Michigan. Founded in 1817, it is the oldest institution of higher education in the state.The University of Michigan is one of the first American research universities and a founding member of the Association of American Universities.It consists of nineteen colleges and offers 250 bachelors and masters degree programs in various humanities and STEM disciplines.The University is accredited by the Commission on Higher Education. In 2021, it ranked third among American universities in research spending according to the National Science Foundation.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackunimichigan')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Michigan-Ann Arbor', callback_data='engunimichigan1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'db328ba494fc76f0c4927a106b86dab0.jpeg', 'rb'),caption='The state of Michigan is located in the Midwestern United States in the Great Lakes region.Lake Michigan is the only one of the Great Lakes located entirely in the United States. The rest of the territory borders four of the five Great Lakes.Michigan is divided into the upper and lower peninsulas by the Strait of Mackinac, which connects Lakes Michigan and Huron. The two parts of the state are connected by a bridge — one of the longest suspension bridges in the world.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniarizona1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.arizona.edu/', callback_data='engsiteuniarizona1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'734f715a9479442c44f75452ba10e45b.jpg', 'rb'), caption='The University of Arizona (UA) is a public research university located in Tucson, Arizona. The teaching staff is the strongest in the region, where Nobel Prize laureates also work. The University of Arizona works with numerous enterprises and provides the opportunity to both conduct research and undergo various internships, which allows students to reach great heights in their field.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniarizona2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.asu.edu/academics/colleges-schools/tempe', callback_data='engsiteuniarizona2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Arizona_State_University,_Tempe_Main_Campus,_Tempe,_AZ_-_panoramio_(61).jpg', 'rb'), caption='Tempe is the campus of Arizona State University (ASU).It offers students and graduates the opportunity to engage in multidisciplinary research and research in first-class laboratories and facilities.There are located on the campus:Liberal Arts and Sciences College;Herberger Institute for Design and the Arts;School for the Future of Innovation in Society;School of Sustainability.Also on the campus are:Ira A. Fulton Schools of Engineering;Mary Lou Fulton Teachers College;W. P. Carey School of Business;University College;Barrett, The Honors College.The Tempe campus is highly environmentally friendly and offers easy access to the entire Phoenix capital via public transportation, including light rail.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguniarizona3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://nau.edu/', callback_data='engsiteuniarizona3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackarizonauni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'northern-arizona-university-twitter.webp', 'rb'), caption='Northern Arizona University (NAU) is a public research university located in Flagstaff, Arizona. Founded in 1899, NAU offers a wide range of undergraduate, graduate, and doctoral programs through its colleges and schools, including the College of Arts and Letters, College of Education, College of Engineering, Computer Science, and Applied Sciences, College of Health and Humanities, The W. A. Franke College of Business, and many others.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbackarizonauni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Arizona', callback_data='enguniarizona1')
    button2 = types.InlineKeyboardButton(text='Arizona State University-Tempe', callback_data='enguniarizona2')
    button3 = types.InlineKeyboardButton(text='Northern Arizona University', callback_data='enguniarizona3')
    button4 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'midtown-phoenix-skyline-night-1.jpg', 'rb'),caption='Arizona is a state located in the southwestern United States of America. It borders New Mexico to the east, California to the west, Mexico to the south, and Colorado to the northeast.The area is 295,254 km2. The capital of the state is the city of Phoenix. Major cities: Mesa and Tucson. In 2011, the population was 6,482,505 (16th largest). The territory is divided into 15 counties.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguninewyork1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.cornell.edu/', callback_data='engsiteuninewyork1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'Campus image for fb.jpg', 'rb'), caption='Cornell University is a private research university founded in 1865. It is the only Ivy League university founded after the American Revolutionary War. There are 24,000 students enrolled at Cornell. Cornell University is located in the small, quiet town of Ithaca in New England, a four-hour drive from New York City.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguninewyork2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.columbia.edu/', callback_data='engsiteuninewyork2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'97281_original.png', 'rb'), caption='Columbia University is one of the most prestigious and oldest private universities in America. It is located in the Manhattan neighborhood of New York City.It was founded in the middle of the 18th century as the Royal College. He is a member of the Ivy League, the educational elite of the United States.Among the graduates and teachers of Columbia University are several presidents of America, heads of other states, winners of the Oscar and Nobel Prizes.The main campus is located in the heart of New York City, in Manhattan. It occupies 13 hectares of land. The university campuses have everything for living and studying: libraries, laboratories, sports facilities, a medical center.There are more than 500 organizations and interest groups for students.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguninewyork3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.nyu.edu/', callback_data='engsiteuninewyork3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'nyu-stern.webp', 'rb'), caption='New York University is a private research university in the United States, located in New York City. One of the most famous and prestigious higher education institutions in the world.In 2020, New York University was ranked 11th among the best universities in the United States and 35th among the best universities in the world in the Quacquarelli Symonds (QS) ranking.The University is the largest private research university in the United States. It has more than 51 thousand students.New York University consists of 16 schools, institutes and colleges. The main building of the university is located in Greenwich Village in Manhattan.The University is a member of the Association of American Universities, which has been uniting leading research universities in North America since 1900.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguninewyork4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.buffalo.edu/', callback_data='engsiteuninewyork4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'buffalo-state.jpg', 'rb'), caption='The University at Buffalo (UB) is a public research university with campuses in Buffalo and Amherst, New York, USA.The university was founded in 1846 as a private medical college, and merged with the State University of New York system in 1962.As of 2022, it is one of the two leading educational institutions in the SUNY system.The University offers bachelors degrees in more than 140 fields of study, as well as more than 220 masters degree programs and more than 95 doctoral programs.In 1989, UB was elected to the Association of American Universities.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'enguninewyork5')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.commonapp.org/explore/bard-college/', callback_data='engsiteuninewyork5')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacknewyorkuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'bard-college-campus_1130x500_acf_cropped.jpg', 'rb'), caption='Bard College (English Bard College, abbreviated Bard) is a prestigious private liberal arts and sciences university located in Annandale-on-Hudson, Dutchess County, New York. It is a National Historic Landmark of the United States.The institution includes one of the youngest and most progressive conservatories in America.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbacknewyorkuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Cornell University', callback_data='enguninewyork1')
    button2 = types.InlineKeyboardButton(text='Columbia University', callback_data='enguninewyork2')
    button3 = types.InlineKeyboardButton(text='New York University', callback_data='enguninewyork3')
    button4 = types.InlineKeyboardButton(text='University at Buffalo', callback_data='enguninewyork4')
    button5 = types.InlineKeyboardButton(text='Bard College', callback_data='enguninewyork5')
    button6 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'united-states-of-america-nyu-iork-23130.jpg', 'rb'),caption='The State of New York.In the northeastern part of the United States, the state of New York stretches along the Atlantic coast. The main city of the state is the city of Albany.The border with Canada stretches to the northeast, the southeastern part is occupied by the Atlantic coast, lakes Ontario and Erie are located to the west, and Long Island is located to the south.A significant part of the states territory is occupied by rivers and lakes. The other part is covered by the Appalachian mountain ranges.',reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunitexas1')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.utexas.edu/', callback_data='engsiteunitexas1')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbackntexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'BostonEntrance_10rs.jpg', 'rb'), caption='The University of Texas at Austin is a public university in Austin, Texas, USA.It was founded in 1883 and is one of the largest in the country and the largest in Texas.The University is actively engaged in research that is significant for society, involving students and teachers in solving problems and challenges of science. The amount of funding for scientific research at the university is more than $ 400 million.The University offers a wide range of specialties — humanities, technical, classical and narrow profile.It is located in downtown Austin, a 437-acre urban campus. The campus includes 9 academic universities and 6 public medical institutions.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunitexas2')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://uh.edu/', callback_data='engsiteunitexas2')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacktexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'825_585_uh.jpg', 'rb'), caption='The University of Houston is a public research university in the United States, located in Houston, Texas. The largest and main campus in the University of Houston (UHS) system, as well as the 3rd largest university in the state. The Princeton Review ranked him one of the best universities in the United States, and is also among the top 300 universities in the Academic Ranking of universities in the world.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunitexas3')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.rice.edu/', callback_data='engsiteunitexas3')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacktexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'lovettbirdseye.jpg', 'rb'), caption='Rice University (full name — William Marsh Rice University) is a prestigious private university located in Houston, Texas.It was founded in 1891 by businessman William Marsh Rice, who left most of his fortune to establish an educational institution.Today, the university is among the best institutions in the United States, and it is consistently in the top 20. Huge funds are allocated for research every year, and many professional research centers and groups (more than 100) work.Rice University has bachelors, masters and doctoral departments, and it is possible to take short-term and additional courses.Graduates with Rice University diplomas are appreciated as excellent specialists in their fields.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engunitexas4')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='Website', url='https://www.ttu.edu/', callback_data='engsiteunitexas4')
    button2 = types.InlineKeyboardButton(text='Back', callback_data='engbacktexasuni')
    markup.add(button1, button2)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'texas-tech-university-health-sciences-center-2.jpg', 'rb'), caption='Texas Tech University, founded in 1923 in Lubbock, Texas, is also known as Texas Tech College. Currently, 28,422 students study at the university. The University offers academic programs based on colleges and schools of agricultural sciences and natural resources, engineering, arts and sciences, mass communications, visual and performing arts, public services, architecture, business, pedagogy and law.', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'engbacktexasuni')
def like_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text='University of Texas at Austin', callback_data='enguniexas1')
    button2 = types.InlineKeyboardButton(text='University of Houston', callback_data='engunitexas2')
    button3 = types.InlineKeyboardButton(text='Rice University', callback_data='engunitexas3')
    button4 = types.InlineKeyboardButton(text='Texas Tech University', callback_data='engunitexas4')
    button5 = types.InlineKeyboardButton(text='Back', callback_data='engstateback')
    markup.add(button1, button2, button3, button4, button5)
    bot.send_photo(chat_id=call.message.chat.id, photo=open(r'capitol-building-aerial-skyline-sunset-austin-tx-texas-state-capital-501154548-58fd156b3df78ca159b45f04.jpg','rb'),caption='Texas is one of the 50 US states. It was annexed to the country by presidential decree on December 29, 1845. It occupies the second place after Alaska in terms of territory area — 696 thousand square kilometers and the second place in terms of population after California. According to the results of the 2020 U.S. census, it amounted to 29.1 million people.The capital of the state is Austin, which is administratively divided into 254 counties — this is more than any other US state.',reply_markup=markup)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as ex:
            telebot.logger.error(ex)






