# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, os, sys
import requests, json, urllib

reload(sys)
sys.setdefaultencoding('utf-8')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot_name = "@happy_mybot"

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello World! I'm a bot, please talk to me!")	

def echo(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def tangshi_songci(bot,update):
    cmd, text = parse_cmd_text(update.message.text)

    data = {}
    data["appkey"] = os.getenv('APPKEY')
    data["keyword"] = text
    data["pagesize"] = 1
    data["pagenum"] = 1

    url_values = urllib.urlencode(data)
    if(cmd == "/tangshi"):
        url = "http://api.jisuapi.com/tangshi/search" + "?" + url_values
    else:
        url = "http://api.jisuapi.com/songci/search" + "?" + url_values

    req = requests.get(url)
    html = unicode(req.text).encode('utf-8')
    jsonarr = json.loads(html.read())

    if jsonarr["status"] != u'0':
        bot.send_message(chat_id=update.message.chat_id, text=jsonarr["msg"])
        return

    result = jsonarr["result"]

    temp_text = result["list"][0]["title"] + "\n" + result["list"][0]["author"] + "\n" + result["list"][0]["content"]

    block_chars = '⓪①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳❶❷❸❹❺❻❼❽❾❿⑴⑵⑶⑷⑸⑹⑺⑻⑼⑽⑾⑿⒀⒁⒂⒃⒄⒅⒆⒇'
    temp = ''
    for c in temp_text:
        if not c in block_chars:
            temp += c

    send_text = temp.replace('&nbsp;', ' ').replace('<br />', '\n')

    bot.send_message(chat_id=update.message.chat_id, text=send_text)


def run():

    token = os.getenv('TELEGRAM_TOKEN')

    # create an Updater
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # register function in the dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('tangshi', tangshi_songci))
    dispatcher.add_handler(CommandHandler('songci', tangshi_songci))

    # echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dispatcher.add_error_handler(error)

    # start the bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()

def parse_cmd_text(text):
    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = text.encode('utf-8')
    cmd = None
    if '/' in text:
        try:
            index = text.index(' ')
        except ValueError as e:
            return (text, None)
        cmd = text[:index]
        text = text[index + 1:]
    if cmd != None and '@' in cmd:
        cmd = cmd.replace(bot_name, '')
    return (cmd, text)

if __name__ == '__main__':
    run()
