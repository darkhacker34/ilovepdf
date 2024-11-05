# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

file_name = "ILovePDF/plugins/group/start.py"

from plugins import *
from plugins.utils import *
from configs.config import images, dm
from pyrogram import Client, filters, enums
import logging

# Configure logging if not already configured
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@ILovePDF.on_message(filters.group & filters.incoming & filters.command("start"))
async def start(bot, message):
    try:
        # Send "typing" action to chat
        await message.reply_chat_action(enums.ChatAction.TYPING)
        
        # Reply with a message text
        await message.reply_text("𝗠𝗲𝗿𝗴𝗲 𝗬𝗼𝘂𝗿 𝗠𝗚 𝗤𝘂𝗼𝘁𝗮𝘁𝗶𝗼𝗻", quote=False)
        
        # Delete the command message
        await message.delete()
        
    except Exception as e:
        # Log the exception with file name and error details
        logger.exception("🐞 %s: %s" % (file_name, e), exc_info=True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding! XD
