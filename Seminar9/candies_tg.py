import telebot
from random import randint

# создаем бот-клиента
bot = telebot.TeleBot("5811949740:AAHxJNNbvFBpUV1gsXrivHqbmQ09KKEs6f0")   # вставьте сюда токен для бота
# переменные
names = []
candies = 50
max_stake = 28
prev_stake = 0
stake = 0

def restart():
    global candies
    global prev_stake
    candies = 50
    prev_stake = 0

def get_player_names(message):   
    global names
    names = [message.from_user.first_name, 'Бот']

# жеребьевка
def coin_toss():
    global switch
    global names
    switch = randint(0, 1)

def switch_turn():
    global switch
    if switch == 1:
        switch = 0
    else:
        switch = 1

def player_move(message):
    global stake
    global prev_stake
    global candies
    if message.text.isdigit() and 0 < int(message.text) <= max_stake:
        stake = int(message.text)
        bot.send_message(message.chat.id, f'Игрок берет {stake} конфет')
        candies -= stake
        prev_stake = stake
        switch_turn()
    else:
        bot.send_message(message.chat.id, f'Можно брать от 1 до {max_stake} конфет!')    
    game(message)

def bot_move(message):
    global prev_stake
    global stake
    global candies
    # умный бот
    # если первый ход и конфеты не делятся на ставку+1 без остатка,
    # то берем n%(stake_limit+1) конфет
    if candies % (max_stake + 1) > 0:
        stake = candies % (max_stake + 1)
    # и после дополняем ход противника до (его ставка+1)
    else:
        if prev_stake > 0:
            stake = max_stake + 1 - prev_stake
        # если же ходим вторым, то делаем случайные ходы в надежде на ошибку противника
        else:
            stake = randint(1, max_stake)
    # если ходим вторым и конфеты делятся на ставку+1 без остатка
    if prev_stake > 0 and candies % (max_stake + 1) == 0:
        stake = max_stake + 1 - prev_stake
    bot.send_message(message.chat.id, f'Бот берет {stake} конфет')
    candies -= stake
    prev_stake = stake
    switch_turn()
    game(message)


def game(message):
    if candies > 0:
        bot.send_message(message.chat.id, f'На кону {candies} конфет')
        if switch == 0:
            bot.send_message(message.chat.id, f'Ваш ход. Сколько конфет возьмете (1 - {max_stake}?')
            bot.register_next_step_handler(message, player_move)
        else:
            bot_move(message)
    else:
        bot.send_message(message.chat.id, f'Осталось {candies} конфет')
        switch_turn()
        bot.send_message(message.chat.id, f'Выиграл {names[switch]}!')

def option(message):
    if message.text.lower() == 'yes':  
        get_player_names(message)
        coin_toss()
        restart()
        bot.send_message(message.chat.id, f'Первым ходит {names[switch]}')
        game(message)
    elif message.text.lower() == 'no':
        bot.send_message(message.chat.id, f'Скучаем...')
    else:
        bot.send_message(message.chat.id, f'Я не понимаю тебя. Давай снова.')

def play_game():
    @bot.message_handler(content_types = ["text"]) # вызов функции если тип сообщения - текст
    def controller(message):
        if message.text.lower() == 'play':
            bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, сыграем в конфеты (yes/no)?')
            bot.register_next_step_handler(message, option)
        else:
            bot.send_message(message.chat.id, f'Напиши play') 
    bot.infinity_polling()

play_game()