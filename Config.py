import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "7706053"))
    API_HASH = os.environ.get("API_HASH", "a87b492b8fe379c5fd63793d29ca7a27")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6052272434:AAEqTpPpzWkJSKH4-3HIvTqQoL7TRVd1eX8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1ApWapzMBu5_8p658jqN_U3wj3a98Ybu6u8Kz0ltS3cMJ7ZSP8K_rRrJbkI3zXy_z8IEqOeKdgfaxRnIwRSDHzGqhhWMuwE4CcrH0iMc2Bf_yxRLRQXGK6ejXzdz1numD-G4Xeot-1EiNGx7XEA2ySAlDEYTwFNCIm8JdiuwtlVp2IaUT8PyZey7ejC7JyU91wkuNGEIC14PMPq43Kc0blEhMmFGySChKtrJ1pWH5eg97Rah9qD63Fyoqr5pgRlsTfwCDB2pEDHIICfQ1PRMf0sLLoIgWgyiro_TpjUuZe9Ja2f_A8_M1aVxBLxiy3qw-Xi3flVA47LL38CbDy2z381TDyfn6Zgs=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Al3x4nderbot")
    SUPPORT = os.environ.get("SUPPORT", "M_L_F")
    CHANNEL = os.environ.get("CHANNEL", "FoR4Lex")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/2ad68bd0e391a69163d0a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
