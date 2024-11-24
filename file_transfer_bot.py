import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Read the token from an environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError("No TELEGRAM_BOT_TOKEN found in environment variables")

received_messages = []
counting = False

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Please send URLs and titles to @file-RS-bot.\n'
                                    'Use /command1 to start counting files.\n'
                                    'Use /command2 to print the number of received files so far.')

async def command1(update: Update, context: CallbackContext) -> None:
    global counting
    counting = True
    received_messages.clear()
    await update.message.reply_text('Start counting files.')

async def command2(update: Update, context: CallbackContext) -> None:
    global counting
    counting = False
    await update.message.reply_text(f'Number of received files so far: {len(received_messages)}')
    print(f'Number of received files so far: {len(received_messages)}')

    # Process the received messages and pair each URL with its title
    url_title_pairs = {}
    for i in range(0, len(received_messages), 2):
        if i + 1 < len(received_messages):
            url = received_messages[i]
            title = received_messages[i + 1]
            url_title_pairs[url] = title

    # Print the URL-title pairs
    for url, title in url_title_pairs.items():
        print(f'URL: {url}, Title: {title}')

    # Save the URL-title pairs to a text file
    file_path = r"C:\Users\Pouya\Documents\url_title_pairs.txt"
    with open(file_path, 'w', encoding='utf-8') as file:
        for url, title in url_title_pairs.items():
            file.write(f'URL: {url}, Title: {title}\n')

    print(f"Data saved to {file_path}")


async def handle_message(update: Update, context: CallbackContext) -> None:
    if counting:
        received_messages.append(update.message.text)

def main() -> None:
    print("Please send URLs and titles to @file-RS-bot.")
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("command1", command1))
    application.add_handler(CommandHandler("command2", command2))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == '__main__':
    main()