import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

# Bot settings
PORT = environ.get("PORT", "8080")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/ae598689ad820eb6fc3a1.jpg https://telegra.ph/file/09e5cdea72f4120e09a47.jpg https://telegra.ph/file/25a2855da84f0b35bc6f6.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/ddc8d37e206ca3c0820b3.png")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/8180269540655a03b1742.gif")
NEWGRP = environ.get("NEWGRP", "https://telegra.ph/file/4407fd523f1e0b46df1d0.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', '')
auth_grp = environ.get('AUTH_GROUPS', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
FILDLT_CNL = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('FILDLT_CNL', '0').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "MiNiFiLX-Auto-Bot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Channel Button Links
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/MiNiFiLX_Auto_Group')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/MiNiFiLX')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/+KL6-out5MalkNzA1')
MSG_ALRT = environ.get('MSG_ALRT', '<b>Share and Support Us ❤️</b>')

# Custom Chats
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1001506291887'))
HOW_DWLD_LINK = environ.get('HOW_DWLD_LINK', 'https://t.me/Artrlc09/35')

# Log Channels
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
RQST_LOG_CHANNEL = int(environ.get('RQST_LOG_CHANNEL', ''))

# Bot Options
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "[{file_name}](https://t.me/MiNiFiLX)\n\n<b>Join Our Offical Channel & Group @MiNiFiLX_Support ❤️</b>")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>{mention}'s Qᴜᴇʀʏ ☞ <code>{query}</code>\n\n<b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n💀 Rᴇʟᴇᴀsᴇ :  <b>{release_date}</b> <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>#{genres}</b></b>\n\n<b>🔅 ᴍᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @NxVaen</b>")
KD_IMDB_TEMPLATE = environ.get("KD_IMDB_TEMPLATE", "<b><b>🏷 Tɪᴛʟᴇ</b> : <a href={url}>{title}</a>\n\n🌟 Rᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10\n <b>{countries}</b>\n\n🎭 Gᴇɴʀᴇs : <b>{genres}</b></b>\n\n<b>")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

# Auto Delete , Filter & Auto Filter
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
MAUTO_DELETE = is_enabled((environ.get('MAUTO_DELETE', "True")), True)

# Delete Time
DELETE_TIME = int(environ.get('DELETE_TIME', 700))
SPL_DELETE_TIME = int(environ.get('SPL_DELETE_TIME', 30))

# Url Shortner
URL_SHORTENR_WEBSITE = environ.get('URL_SHORTENR_WEBSITE', '')
URL_SHORTNER_WEBSITE_API = environ.get('URL_SHORTNER_WEBSITE_API', '')

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
