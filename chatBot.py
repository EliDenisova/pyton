from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}\n\n/hello\n/help\n/sum\n/time\n/new_year\n/calc')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split()  # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/help\n/sum\n/time\n/new_year\n/calc')


async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    expression = msg.split()
    x = expression[1]
    await update.message.reply_text(eval(x))


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.today()
    NY = datetime.datetime(2024, 1, 1)
    d = NY - now  # str(d)  '83 days, 2:43:10.517807'
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    await update.message.reply_text('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))


app = ApplicationBuilder().token('5985922059:AAFFRn4QkzALuhZWvfdhttqdp0ngL8nZYTw').build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("new_year", new_year_command))

app.run_polling()
