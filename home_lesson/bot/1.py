import logging
import random
from telegram.ext import Updater 
from telegram.ext import CommandHandler 
from telegram.ext import MessageHandler,Filters
from setting import api_key

logging.basicConfig(filename='bot.log', level=logging.INFO)



def greet_user(update, context):

    update.message.reply_text(f'''              ");"   Привет !!
    давай сыграем с тобой в игру  конфетки
    ''')


# def talk_to_me(update, context):

#     text = update.message.text
#     print(text)
#     update.message.reply_text(f'{text} ты балбес')

def help_user(update, context):
      
    update.message.reply_text(f"""\nНапоминаем правила игры -нужно брать конфеты,
    В за один ход можно забрать не более чем 28 конфет.
    Все конфеты оппонента достаются сделавшему последний ход""")

def bot_motion(candy_qu):
    if candy_qu > 80:
        res = random.randint(1, 29)   # до 80 бот берет рандомно
        return res
    elif candy_qu <= 28:
        res = candy_qu
        return res
    else:
        atemp = candy_qu // 28
        if atemp == 1:
            f = candy_qu  # если  остается 1 попытка это от конфеты 55 до 27 и бот пытается оставить 29 конфет, и это хорошо  у него получается :)
            temp = f
            while f >= 29:
                res = temp - 29
                f -= 1
                if res == 0:   # если получается 0 бот проигрывает берем 1 конфету
                    res += 1
            return res

        res = candy_qu - (atemp) * 28 + 1  # грубо пытается оставить всегда 29
    return res

def input_num_candy(update,candy_qu):

    num = update.message.text
    
    if num.isdigit():
        num = int(num)
        if num > candy_qu:
            update.message.reply_text(f"нельзя взять конфет больше 28 и  больще чем осталось, всего осталось {candy_qu} конфет")  #
            return input_num_candy(update,candy_qu)
        elif num > 28:
            update.message.reply_text("Вы взяли  больше 28 конфет, так нельзя, возмите заново")
            return input_num_candy(update,candy_qu)
        elif num == 0:
            update.message.reply_text("Ну возмите хоть оду конфетку")
            return input_num_candy(update,candy_qu)
        else:
            return num
    else:
        update.message.reply_text("нужно ввести целое число, половинки  тоже не даем !! ;)")
        return input_num_candy(update,candy_qu)


def main_game(update,context):  #(update.message.text   .message.reply_text

    update.message.reply_text("Доброго дня Начинаем игру с конфетами  \nДавайте представимся,Введите имя первого игрока:")

    Name_player1 = update.message.text
    Name_player2 = "Bot"
    update.message.reply_text(f'\nиграет игрок №1 {Name_player1} против игрока №2 {Name_player2}')
    update.message.reply_text(f"\nНапоминаем правила игры -нужно брать конфеты, за один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход")
    one_player = ''
    two_player = ''
    update.message.reply_text(f"\nтеперь определим кто ходит первым")
    i = random.randint(1, 2)
    if i == 1:
        one_player, two_player = Name_player1, Name_player2
    else:
        one_player, two_player = Name_player2, Name_player1

    update.message.reply_text(f'\nПо результам жеребьевки первым ходит игрок {one_player}')

    # число конфет
    candy_quant = 120
    allcandy_first = 0
    allcandy_second = 0
    # запись последнего хода
    last_player1 = 0

    update.message.reply_text(f'Всего конфет {candy_quant}')
    
    while candy_quant > 0:

        update.message.reply_text(f'ходит игрок {one_player} ')
        if one_player == "Bot":
            first = int(bot_motion(candy_quant))
        else:
            first = int(input_num_candy(update,candy_quant))
        allcandy_first += first
        candy_quant -= first
        last_player1 = 1
        update.message.reply_text(f'осталось {candy_quant}')
        if candy_quant > 0:
            if two_player == "Bot":
                second = int(bot_motion(candy_quant))

            else:
                second = int(input_num_candy(update,candy_quant))
            update.message.reply_text(f'ходит игрок {two_player} и взял  {second} конфет')
            candy_quant -= second
            allcandy_second += second
            last_player1 = 0
        update.message.reply_text(f'осталось {candy_quant}')

    update.message.reply_text(
        f'В итоге : конфет у {one_player}  {allcandy_first}  конфет у {two_player}   {allcandy_second}')
    if last_player1 == 1:
        update.message.reply_text(
            f'Так как последним забрал конфеты игрок  по имени {one_player}, то он  Выиграл и забрал все конфеты')
    else:
        update.message.reply_text(
            f'Так как последним забрал конфеты игрок по имени {two_player}, то он  Выиграл и забрал все конфеты')




# # число конфет
# candy_quant = 120
# allcandy_first = 0
# allcandy_second = 0
# # запись последнего хода
# last_player1 = 0







def main():

    mybot = Updater(api_key, use_context=True)
    db = mybot.dispatcher
    db.add_handler(CommandHandler("start", greet_user))
    db.add_handler(CommandHandler("help", help_user))
    logging.info('start bot')
    db.add_handler(MessageHandler(Filters.text,main_game))

    mybot.start_polling()
    mybot.idle()



# if __name__ == '_main_':
    
#     main()


main()