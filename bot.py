import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram.types import CallbackQuery
from googletrans import Translator
import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

TOKEN = os.environ.get("TOKEN", "")

APP_ID = int(os.environ.get("APP_ID", ""))

API_HASH = os.environ.get("API_HASH", "")

OWNER = os.environ.get("OWNER", "")

Deccan = Client(
        "ggt",
        bot_token=TOKEN,api_hash=API_HASH,
            api_id=APP_ID
    )
    
START_TEXT = """
Salut {}, 
Je suis Google Traducteur bot.

Envoyez moi un texte je le traduira dans les autres langues.

Dévellopée par @lesrobotsdecodingteam et @codingtuto
"""
HELP_TEXT = """
Suivez ces règles...

☛ Envoyez moi un mot/texte simplement.

☛ Sélectionnez ces langues suivantes!

<b><u>Langues :-</u></b>
Anglais, Tamil, Telugu, Hindi, Kannada, Malayalam, Korean, Japanese, Chinese, Greek, Français, Russian, Arabe, Spagnol, Italien, Uzbek, Latin, Polish, Mongolian, Marathi, Khazak, Myanmar, Indonesian, German
"""
ABOUT_TEXT = """
➠ **Bot : Google Traducteur Bot**

➠ **Langue :** Python3

➠ **Serveur :** Heroku

➠ **Library :** Pyrogram
"""

START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Dévellopeur👨‍💻', url=f"https://telegram.me/lesrobotsdecodingteam")
        ],[
        InlineKeyboardButton('Groupe 👥', url='https://telegram.me/codingtuto')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Dévelloppeur👨‍💻', url=f"https://telegram.me/lesrobotsdecodingteam")
        ],[
        InlineKeyboardButton('Groupe 👥', url='https://telegram.me/codingtuto')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Dévelloppeur👨‍💻', url=f"https://telegram.me/lesrobotsdecodingteam")
        ],[
        InlineKeyboardButton('Groupe 👥', url='https://telegram.me/Deccan_Supportz')
        ]]
    )

@Deccan.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=START_BUTTONS
    )
@Deccan.on_message(filters.private & filters.command(["help"]))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True
    )
@Deccan.on_message(filters.private & filters.command(["about"]))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=ABOUT_BUTTONS
    )
	
@Deccan.on_message(filters.text & filters.private )
def echo(client, message):

 keybord = InlineKeyboardMarkup( [
        [
        InlineKeyboardButton("Anglais", callback_data='en'),
        InlineKeyboardButton("Tamil", callback_data='ta'),
        InlineKeyboardButton("Telugu",callback_data='te')
        ],
        [
        InlineKeyboardButton("Hindi", callback_data='hi'),
        InlineKeyboardButton("Kannada", callback_data='kn'),
        InlineKeyboardButton("Malayalam",callback_data= 'ml')
        ],
        [
        InlineKeyboardButton("Korean", callback_data='ko'),
        InlineKeyboardButton("Japanese", callback_data='ja'),
        InlineKeyboardButton("Chinese", callback_data='zn-cn')
        ],
        [
        InlineKeyboardButton("Greek", callback_data='el'),
        InlineKeyboardButton("Français", callback_data='fr'),
        InlineKeyboardButton("Russian", callback_data='ru')
        ],
        [InlineKeyboardButton("Arabe", callback_data='ar'),
         InlineKeyboardButton("Spanish", callback_data='es'),
         InlineKeyboardButton("Italian", callback_data='it')
        ],
        [InlineKeyboardButton("Uzbek", callback_data='uz'),
         InlineKeyboardButton("Latin", callback_data='la'),
         InlineKeyboardButton("Polish", callback_data='po')
        ],
        [InlineKeyboardButton("Mongolian", callback_data='mn'),
         InlineKeyboardButton("Marathi", callback_data='mr'),
         InlineKeyboardButton("Kazakh", callback_data='kk')
        ],
        [InlineKeyboardButton("Myanmar", callback_data='my'),
         InlineKeyboardButton("Indonesian", callback_data='id'),
         InlineKeyboardButton("German", callback_data='de')
        ]
        
    ]
 
 )

 
 message.reply_text("**Sélectionnez une langue pour traduire** 👇",reply_to_message_id = message.message_id, reply_markup = keybord)
    
    

@Deccan.on_callback_query()
async def translate_text(bot,update):
  tr_text = update.message.reply_to_message.text
  cbdata = update.data
  translator = Translator()  
  translation = translator.translate(tr_text,dest=cb_data) 
  await update.message.edit(translation.text)
  	

Deccan.run()
