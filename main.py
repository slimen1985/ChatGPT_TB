import telebot
import openai

openai.api_key = ''
bot = telebot.TeleBot("")


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling()