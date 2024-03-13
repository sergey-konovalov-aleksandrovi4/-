import telebot
import random

from telebot import types

bot = telebot.TeleBot('6702792076:AAFqh3Ld_eb4mtBRX8hihVfSO2U2KPJhR5Q')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item=types.InlineKeyboardButton('Start game',callback_data='start_game')
    markup.add(item)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. Этот бот был создан для игры "Правда или Действие". Приятной игры!',reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'start_game')
def callback(call):
    markup = types.InlineKeyboardMarkup()
    btn2 = types.InlineKeyboardButton('2', callback_data='2')
    btn3 = types.InlineKeyboardButton('3', callback_data='3')
    btn4 = types.InlineKeyboardButton('4', callback_data='4')
    btn5 = types.InlineKeyboardButton('5', callback_data='5')
    btn6 = types.InlineKeyboardButton('6', callback_data='6')
    btn7 = types.InlineKeyboardButton('7', callback_data='7')
    btn8 = types.InlineKeyboardButton('8', callback_data='8')
    markup.add(btn2, btn3, btn4)
    markup.add(btn5, btn6, btn7, btn8)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Выберите количество игроков', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data in ['2', '3', '4', '5', '6', '7', '8'])
def check_callback_message(callback):
    if callback.data in ['2', '3', '4', '5', '6', '7', '8']:
        markup = types.InlineKeyboardMarkup()
        btn_family = types.InlineKeyboardButton('Семейный', callback_data='family')
        btn_party = types.InlineKeyboardButton('Дикая вечеринка', callback_data='party')
        btn_dirty = types.InlineKeyboardButton('Пошлое', callback_data='dirty')
        markup.add(btn_family, btn_party, btn_dirty)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text='Выберите режим', reply_markup=markup)


questions_truth_family = [
    "Кто из играющих больше фоткается?",
    "Как Вы учились? (отличник, хорошист или есть тройки)",
    "Кто из играющих лучше поёт?",
    "Что тебе доводилось стащить из магазина?",
    "Ты готов взять собаку или кошку из приюта?",
    "Как ты разыгрывал друга в последний раз?",
    "Кого из этой комнаты ты бы поцеловал?"
]

questions_action_family = [
    "Изобрази балерину",
    "Изобрази какую-нибудь известную личность, и пусть остальные угадывают.",
    "Сесть на воздушный шарик так, чтобы он лопнул",
    "Быстро скажи любое слово!",
    "Крякай как уточка до следующего игрока.",
    "Набери в рот воды и попробуй просидеть так пять минут.",
    "Сделай 10 приседаний, каждый раз произнося название стран.",
    "Скажи комплимент каждому из присутствующих.",
    "Спародируй какую-нибудь звезду, чтобы мы ее угадали.",
    "Выбери игрока и выполни его просьбу.",
    "Опиши цвет глаз игрока у которого есть зеленый цвет на одежде"
]   

@bot.callback_query_handler(func=lambda callback: callback.data == 'family')
def check_callback_message(callback):
    global message_id  # Declare message_id as a global variable

    if callback.data in ['family']:
        markup = types.InlineKeyboardMarkup()
        btn_truth = types.InlineKeyboardButton('Правда', callback_data='truth_family')
        btn_action = types.InlineKeyboardButton('Действие', callback_data='action_family')
        markup.add(btn_truth, btn_action)
        message_id = callback.message.message_id  # Update message_id
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=message_id, text='Выбрать или правда или действие', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'truth_family')
def check_callback_message(callback):
    global message_id  # Declare message_id as a global variable

    if callback.data == 'truth_family':
        with open('family.py', 'r') as file:
            exec(file.read())
            message_id = callback.message.message_id  # Store the original message ID
            question = random.choice(questions_truth_family)
        markup = types.InlineKeyboardMarkup()
        btn_okay = types.InlineKeyboardButton('Выполнено', callback_data='okay_family_truth')
        btn_no = types.InlineKeyboardButton('Не выполнено', callback_data='no_family_truth')
        markup.add(btn_okay, btn_no)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=message_id, text=question, reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'action_family')
def check_callback_message(callback):
    global message_id  # Declare message_id as a global variable
    if callback.data == 'action_family':
        with open('family.py', 'r') as file:
            exec(file.read())
            message_id = callback.message.message_id  # Store the original message ID
            question = random.choice(questions_action_family)
        markup = types.InlineKeyboardMarkup()
        btn_okay = types.InlineKeyboardButton('Выполнено', callback_data='okay_family_action')
        btn_no = types.InlineKeyboardButton('Не выполнено', callback_data='no_family_action')
        markup.add(btn_okay, btn_no)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=message_id, text=question, reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data in ['okay_family_truth','no_family_truth','okay_family_action', 'no_family_action'])
def check_callback_message(callback):
    if callback.data in ['okay_family_truth','no_family_truth','okay_family_action', 'no_family_action']:
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=False)
        markup = types.InlineKeyboardMarkup()
        btn_truth = types.InlineKeyboardButton('Правда', callback_data='truth_family')
        btn_action = types.InlineKeyboardButton('Действие', callback_data='action_family')
        markup.add(btn_truth, btn_action)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Выберите правда или действие", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'party')
def check_callback_message(callback):
    global message_id  # Declare message_id as a global variable
    if callback.data in ['party']:
        message_id = callback.message.message_id  # Store the original message ID
        markup = types.InlineKeyboardMarkup()
        btn_truth = types.InlineKeyboardButton('Правда', callback_data='truth_party')
        btn_action = types.InlineKeyboardButton('Действие', callback_data='action_party')
        markup.add(btn_truth, btn_action)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=message_id, text='Выбрать или правда или действие', reply_markup=markup)

questions_truth_party = [
    "Просыпали ли Вы на утро с незнакомым человеком?",
    "Пропусти ход",
    "Вы когда-нибудь фантазировали о человеке напротив?",
    "Вы когда-нибудь писали в бассейне?",
    "О чем ты думаешь, когда сидишь на унитазе?",
    "У тебя был воображаемый друг в детстве?",
    "Какая твоя самая плохая привычка?"
]

questions_action_party = [
    "Повернись спиной к другим игрокам, тебе скажут, когда можно будет повернуться!",
    "Взять игрока слева на колени на 2 раунда",
    "Вы должны рассказать (желательно в форме веселой истории), как выкрутишься из предложенной ситуации: тебя случайно заперли на работепоздно вечером. Ты работаешь в бюро похоронных услуг «Солнышко»",
    "Помирись со своей рукой.",
    "Позволь кому-то уложить твои волосы и ходи с этой прической до конца дня.",
    "Притворись будто плачешь.",
    "Поспорь со стеной."
]   

@bot.callback_query_handler(func=lambda callback: callback.data == 'truth_party')
def check_callback_message(callback):
    global message_id  # Declare message_id as a global variable

    if callback.data == 'truth_party':
        with open('family.py', 'r') as file:
            exec(file.read())
            message_id = callback.message.message_id  # Store the original message ID
            question = random.choice(questions_truth_party)
        markup = types.InlineKeyboardMarkup()
        btn_okay = types.InlineKeyboardButton('Выполнено', callback_data='okay_party_truth')
        btn_no = types.InlineKeyboardButton('Не выполнено', callback_data='no_party_truth')
        markup.add(btn_okay, btn_no)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=message_id, text=question, reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'action_party')
def check_callback_message(callback):
    global message_id  # Declare message_id as a global variable
    if callback.data == 'action_party':
        with open('family.py', 'r') as file:
            exec(file.read())
            message_id = callback.message.message_id  # Store the original message ID
            question = random.choice(questions_action_party)
        markup = types.InlineKeyboardMarkup()
        btn_okay = types.InlineKeyboardButton('Выполнено', callback_data='okay_party_action')
        btn_no = types.InlineKeyboardButton('Не выполнено', callback_data='no_party_action')
        markup.add(btn_okay, btn_no)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=message_id, text=question, reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data in ['okay_party_truth','no_party_truth','okay_party_action', 'no_party_action'])
def check_callback_message(callback):
    if callback.data in ['okay_party_truth','no_party_truth','okay_party_action', 'no_party_action']:
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=False)
        markup = types.InlineKeyboardMarkup()
        btn_truth = types.InlineKeyboardButton('Правда', callback_data='truth_party')
        btn_action = types.InlineKeyboardButton('Действие', callback_data='action_party')
        markup.add(btn_truth, btn_action)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Выберите правда или действие", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data == 'dirty')
def check_callback_message(callback):
    if callback.data in ['dirty']:
        markup = types.InlineKeyboardMarkup()
        btn_truth = types.InlineKeyboardButton('Правда', callback_data='truth_dirty')
        btn_action = types.InlineKeyboardButton('Действие', callback_data='action_dirty')
        markup.add(btn_truth, btn_action)
        bot.edit_message_text(chat_id=callback.message.chat.id,
                               message_id=callback.message.message_id,
                               text='Выбрать или правда или действие',
                               reply_markup=markup)

questions_truth_dirty = [
    "Что Вас возбуждает в Вашем партнере?",
    "Расскажи, во всех подробностях, какое нижнее белье на тебе сейчас надето",
    "Что выберешь: виртуальный секс с любимым или реальный секс с обычной симпатией",
    "Сколько вам было лет, когда вы впервые занялись сексом?",
    "Как часто вы мастурбируете?",
    "Какая самая неловкая вещь, которая когда-либо случалась с вами во время секса?",
    "Что тебя больше всего заводит?"
]

questions_action_dirty = [
    "Ты начинаешь! Игроки по очереди должны называть фильмы, которые сняты по книгам. Отшлепай игрока, который не сможет ответить или повторится",
    "Станцуй тверк",
    "Потрогай все попы и скажи, у кого самая аппетитная",
    "Сделайте ближйшему игроку противоположного пола справа одноминутный массаж ягодиц.",
    "Зажмите кубик льда в зубах и проведите им по груди самого старшего по возрасту игрока",
    "Станцуй приватный танец для любого из присутствующих.",
    "Сними с любого из присутствующих в комнате одежду, не используя рук."    
]   


@bot.callback_query_handler(func=lambda callback: callback.data == 'truth_dirty')
def check_callback_message(callback):
    if callback.data == 'truth_dirty':
        with open('family.py', 'r') as file:
            exec(file.read())
            question = random.choice(questions_truth_dirty)
        markup = types.InlineKeyboardMarkup()
        btn_okay = types.InlineKeyboardButton('Выполнено', callback_data='okay_dirty_truth')
        btn_no = types.InlineKeyboardButton('Не выполнено', callback_data='no_dirty_truth')
        markup.add(btn_okay, btn_no)
        bot.edit_message_text(chat_id=callback.message.chat.id,
                               message_id=callback.message.message_id,
                               text=question,
                               reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data == 'action_dirty')
def check_callback_message(callback):
    if callback.data == 'action_dirty':
        with open('family.py', 'r') as file:
            exec(file.read())
            question = random.choice(questions_action_dirty)
        markup = types.InlineKeyboardMarkup()
        btn_okay = types.InlineKeyboardButton('Выполнено', callback_data='okay_dirty_action')
        btn_no = types.InlineKeyboardButton('Не выполнено', callback_data='no_dirty_action')
        markup.add(btn_okay, btn_no)
        bot.edit_message_text(chat_id=callback.message.chat.id,
                               message_id=callback.message.message_id,
                               text=question,
                               reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: callback.data in ['okay_dirty_truth','no_dirty_truth','okay_dirty_action', 'no_dirty_action'])
def check_callback_message(callback):
    if callback.data in ['okay_dirty_truth','no_dirty_truth','okay_dirty_action', 'no_dirty_action']:
        bot.answer_callback_query(callback_query_id=callback.id, show_alert=False)
        markup = types.InlineKeyboardMarkup()
        btn_truth = types.InlineKeyboardButton('Правда', callback_data='truth_dirty')
        btn_action = types.InlineKeyboardButton('Действие', callback_data='action_dirty')
        markup.add(btn_truth, btn_action)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text="Выберите правда или действие", reply_markup=markup)    

bot.polling()
