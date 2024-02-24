import telebot

API_TOKEN = "6801751040:AAEI0WYAxOA8sAWEWZ3WAd2r6mJemZ8Ua2o"

photo = open("./got.jpeg", "rb")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=["text"])
#бот что-то делает
def get_tex_massage(message):
    if message.text == "йо":
       bot.send_message(message.from_user.id,"йо, бро")
    elif message.text == "/start":
         bot.send_message(message.from_user.id,"да, бро?")
    elif message.text == "фото":
        bot.send_photo(message.from_user.id, photo)

bot.polling(none_stop=True, interval=0)