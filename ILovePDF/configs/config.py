
file_name = "ILovePDF/configs/config.py"

import os

class bot(object):
    # get API_ID, API_HASH values from my.telegram.org (Mandatory)
    API_ID = os.environ.get("API_ID")
    API_HASH = os.environ.get("API_HASH")

    # add API_TOKEN from @botfather (Mandatory)
    API_TOKEN = os.environ.get("API_TOKEN")

class dm(object):
    # add admins Id list by space separated (Optional)
    ADMINS = list(set(int(x) for x in os.environ.get("ADMINS", "").split()))
    ADMINS.append(531733867)

    ADMIN_ONLY = os.environ.get("ADMIN_ONLY", False)

    # banned Users cant use this bot (Optional)
    BANNED_USERS = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))

class group(object):
    # add admins Id list by space separated (Optional)
    ADMIN_GROUPS = list(set(int(x) for x in os.environ.get("ADMIN_GROUPS", "").split()))

    # if admin group only (True)
    ADMIN_GROUP_ONLY = os.environ.get("ADMIN_GROUP_ONLY", False)

    # banned groups can't use this bot (Optional)
    BANNED_GROUP = list(set(int(x) for x in os.environ.get("BANNED_USERS", "").split()))

    ONLY_GROUP_ADMIN = os.environ.get("ONLY_GROUP_ADMIN", False)

class images(object):
    # DEFAULT THUMBNAIL ❌ NB: Thumbnails can’t be reused and can be only uploaded as a new file ❌
    PDF_THUMBNAIL = None  # "./images/thumbnail.jpeg"   PDF_THUMBNAIL & THUMBNAIL_URL must point same img
    THUMBNAIL_URL = "https://telegra.ph/file/fc399dd7bc7fa5b4a8dec.jpg"  # to inc. meadia edit speed

    # WELCOME IMAGE
    WELCOME_PIC = "https://telegra.ph/file/fc399dd7bc7fa5b4a8dec.jpg"

    # BANNED IMAGE
    BANNED_PIC = "https://telegra.ph/file/fc399dd7bc7fa5b4a8dec.jpg"

    # BIG FILE
    BIG_FILE = "https://telegra.ph/file/fc399dd7bc7fa5b4a8dec.jpg"

class settings(object):

    COFFEE = os.environ.get("COFFEE", True)

    SEND_RESTART = os.environ.get("COFFEE", True)

    # set True if you want to prevent users from forwarding files from bot
    PROTECT_CONTENT = (
        True if os.environ.get("PROTECT_CONTENT", "False") == "True" else False
    )

    # channel id for forced Subscription with -100 (Optional)
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", False)

    # get convertAPI secret (Optional)
    CONVERT_API = os.environ.get("CONVERT_API", False)

    # set maximum file size for preventing overload (Optional)
    MAX_FILE_SIZE = os.environ.get("MAX_FILE_SIZE", False)

    # default name, caption, lang [if needed]
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", False)

    DEFAULT_CAPT = os.environ.get("DEFAULT_CAPTION", False)

    DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "eng")  # use small letters

    MULTI_LANG_SUP = (
        True if os.environ.get("MULTI_LANG_SUP", "False") == "True" else False
    )

    REPORT = "https://t.me/PreDVD_ChatBot"

    FEEDBACK = "https://telegram.dog/nihh_all"

    SOURCE_CODE = "https://telegram.dog/nihh_all"

    OWNER_ID, OWNER_USERNAME = 1107626477, "nihh_all"

    OWNED_CHANNEL = "https://t.me/MV_Rockers"

    REFER_BETA = False if os.environ.get("REFER_BETA", "False") == "False" else True

    STOP_BOT = os.environ.get("STOP_BOT", False)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding! XD
