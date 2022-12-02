"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import ephem
import logging
import datetime
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

def greet_user(update, context):
    logger.debug('Вызван /start')
    update.message.reply_text("Введи: /planet и название планеты на английском языке!")



def talk_to_me(update, context):
    text = update.message.text
    logger.debug(text)
    update.message.reply_text(text)



def get_constellation(update, bot):
    planets = {'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto'}
    logger.debug('Вызван /planet')
    msg = update.message

    planet_name = (msg.text.split(' ')[1]).capitalize()

    if planet_name in planets:
        planet = getattr(ephem, planet_name)
        time_planet = planet(datetime.datetime.now())
        planet_constellation = ephem.constellation(time_planet)
        logger.debug(planet_constellation)

        msg.reply_text(f'{planet_name}: {planet_constellation}')
    else:
        msg.reply_text('Ошибка ввода имени планеты: "' + planet_name + '". После /planet введи имя планеты на английском языке.')
        logger.debug('Ошибка ввода имени планеты')


def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_constellation))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
