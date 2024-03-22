from dotenv import load_dotenv
import ptbot
import os
from pytimeparse import parse


def wait(chat_id, text):
    time = parse(text)
    bot_message = bot.send_message(chat_id, f"Осталось cекунд: {time}")
    bot.create_countdown(time, notify_progress, chat_id=chat_id, message_id=bot_message, start_time=time)
    bot.create_timer(time, choose, chat_id=chat_id)


def notify_progress(secs_left, chat_id, message_id, start_time):
    progress_text = render_progressbar(start_time, start_time-secs_left)
    bot.update_message(
        chat_id,
        message_id,
        f"Осталось секунд: {secs_left}\n{progress_text}"
    )


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def choose(chat_id):
    message = 'Время вышло!'
    bot.send_message(chat_id, message)


if __name__ == '__main__':
    load_dotenv()
    TG_TOKEN = os.getenv('TG_TOKEN')
    TG_CHAT_ID = os.getenv('TG_CHAT_ID')
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(wait)
    bot.run_bot()
