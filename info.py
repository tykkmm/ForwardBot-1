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
API_ID = int(environ['29426486'])
API_HASH = environ['d71ad4ec048ab41677a1a439b21ff0c9']
BOT_TOKEN = environ['7355006985:AAEY8ijg4CP-8GgcliRGJja87Tby78QT7To']
SESSION = environ.get('forwarderofty', 'Media_search') 

# Admins
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
