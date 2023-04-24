from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "25472819"))
API_HASH = getenv("API_HASH", "f2db2616807ff248dcf07bde10df0631")
BOT_TOKEN = getenv("BOT_TOKEN", "6164180478:AAEmmvOpkZcvdZbG-CcdaAdxTjoWZ4P5K78")
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuxKodHJpVNeR-XfuNEIHoTRKd9yJNLTQ08W97mG0kJztS0N_3dFTXVoHCy-WXcjGANoWctpLwkhRml6K2aMV3xVyJgffQe30JMI5bY1TkdrbB0zC5Ph8OJEIUZ-Ap_eZyjXHBaQy2Ihbhr-eVBW96bLg715kwahk6xfd8PhLhWWjlXn9xJ5VuFqGAEGZOvg_wDV8I06nijsZfBk-kflWnH-yTCv1vsmqrPHRsWI8XxNUbm9DrEAW8UxKdDFARcooRnGg9IYhGbSy0q6FCv8IpIM7QXhXWe_i67g5EJ5Oa0dOZPyUoCrRNE92ql2gZv6SPVGU3MNC7ik5Upt7Vxv8uMo=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "JEEEW")
ALIVE_NAME = getenv("ALIVE_NAME", "EHOUDE")
BOT_USERNAME = getenv("BOT_USERNAME", "SAEKOMUZICBOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "R_R_H_H")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "R_R_H_H")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
