import random
import nltk
import json
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


with open('BOT_CONFIG.json', encoding='utf-8') as f:
  BOT_CONFIG = json.load(f)
del BOT_CONFIG['intents']['price']
del BOT_CONFIG['intents']['thanks']
del BOT_CONFIG['intents']['purchase']
len(BOT_CONFIG['intents'].keys())
print(BOT_CONFIG['intents'].values())


def clean(text):
  clean_text = ''
  for ch in text.lower():
    if ch in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
      clean_text = clean_text + ch
  return clean_text
# def get_intent(text):
#   for intent in BOT_CONFIG['intents'].keys():
#     for example in BOT_CONFIG['intents'][intent]['examples']:
#       if nltk.edit_distance(clean(text), clean(example))/max(len(clean(example)), len(clean(text))) < 0.4:
#         return intent
#   return 'intent не найден'
def get_intent_by_model(text):
  return clf.predict(vectorizer.transform([text]))[0]
def bot(input_text):
  intent = get_intent_by_model(input_text)
  return random.choice(BOT_CONFIG['intents'][intent]['responses'])

texts = []
y = []
for intent in BOT_CONFIG['intents'].keys():
  for example in BOT_CONFIG['intents'][intent]['examples']:
    texts.append(example)
    y.append(intent)

train_texts, test_texts, y_train, y_test = train_test_split(texts, y, test_size = 0.2, random_state = 42)

vectorizer = CountVectorizer(ngram_range=(1,3), analyzer='char_wb')
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

vocab = vectorizer.get_feature_names_out()
print(len(vocab))

clf = RandomForestClassifier(n_estimators=300).fit(X_train, y_train)
print(clf.score(X_train,y_train), clf.score(X_test,y_test))

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    input_text = update.message.text
    update.message.reply_text(bot(input_text))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5019813886:AAEapnTOJJCF19GTTjUHqa3TLpsFGYZtdic")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()


