import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "18943318"))
    API_HASH = os.environ.get("API_HASH", "f00b7def1f034b90a866d382078bd68f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "DRACULA_T22BOT")
    SUPPORT = os.environ.get("SUPPORT", "DRACULA_SUPPORT")
    CHANNEL = os.environ.get("CHANNEL", "DRACULA")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
