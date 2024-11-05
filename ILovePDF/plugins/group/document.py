# This module is part of https://github.com/nabilanavab/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 nabilanavab

import os
import time
import asyncio
import logging
from PIL import Image
from pyrogram import Client as ILovePDF, filters, enums
from pyrogram.enums import ChatMemberStatus
from configs.config import images, MAX_FILE_SIZE, MAX_FILE_SIZE_IN_kiB, settings
from configs.db import invite_link, myID, BANNED_USR_DB
from plugins.utils import util, work
from pdf import PDF

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

file_name = "ILovePDF/plugins/group/document.py"

@ILovePDF.on_message(
    filters.group & filters.incoming & filters.command(["analyse", "check", "nabilanavab"])
)
async def gDOC(bot, message):
    """Main function to process group document analysis commands."""
    try:
        await message.reply_chat_action(enums.ChatAction.TYPING)
        lang_code = await util.getLang(message.chat.id)
        CHUNK, _ = await util.translate(text="gDOCUMENT", lang_code=lang_code)

        # Check bot's admin status
        if not await is_bot_admin(bot, message):
            return await message.reply(CHUNK["admin"], quote=True)

        # Validate message for document or image
        if not is_valid_message(message):
            return await message.reply(CHUNK["notDOC"], quote=True)

        # Check if user is banned
        if message.from_user.id in BANNED_USR_DB:
            return await message.reply("Attempting a sneaky con job, eh? Access denied!")

        # Check for force subscription
        if invite_link and not await is_user_subscribed(bot, message):
            return await send_subscription_prompt(bot, message, lang_code)

        # Validate user privileges
        if not await has_valid_privileges(bot, message, lang_code):
            return

        await message.delete()
        logFile = None

        # Handle image and document processing
        if message.reply_to_message.photo:
            return await handle_image_to_pdf(bot, message, CHUNK)
        else:
            return await handle_document_to_pdf(bot, message, CHUNK)

    except Exception as e:
        logger.exception("🐞 %s: %s", file_name, e)
        await work.work(message, "delete", True)


# ================== Helper Functions ================== #

async def is_bot_admin(bot, message):
    """Check if the bot has admin privileges in the group."""
    try:
        status = await bot.get_chat_member(message.chat.id, myID[0].id)
        return status.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]
    except Exception as e:
        logger.warning("Error checking bot admin status: %s", e)
        return False


def is_valid_message(message):
    """Verify if the message is a reply to a valid document or image."""
    return bool(message.reply_to_message and (message.reply_to_message.document or message.reply_to_message.photo))


async def is_user_subscribed(bot, message):
    """Check if the user is subscribed to the required channel."""
    try:
        user_status = await bot.get_chat_member(settings.UPDATE_CHANNEL, message.from_user.id)
        return user_status.status != "kicked"
    except Exception:
        return False


async def send_subscription_prompt(bot, message, lang_code):
    """Send a prompt for the user to subscribe if they are not already subscribed."""
    tTXT, tBTN = await util.translate("BAN['Force']", "BAN['ForceCB']", asString=True, lang_code=lang_code)
    tBTN = await util.createBUTTON(btn=await editDICT(tBTN, value=[invite_link[0], ""]), order="11")
    return await message.reply_photo(
        photo=images.WELCOME_PIC,
        caption=tTXT.format(message.from_user.first_name, message.from_user.id),
        reply_markup=tBTN,
        quote=True
    )


async def has_valid_privileges(bot, message, lang_code):
    """Validate if the user has necessary privileges to perform the command."""
    isAdmin = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id not in settings.ADMINS:
        if settings.ONLY_GROUP_ADMIN and isAdmin.status != ChatMemberStatus.ADMINISTRATOR:
            await message.reply(CHUNK["Gadmin"], quote=True)
            return False
        elif isAdmin.status != ChatMemberStatus.ADMINISTRATOR and message.from_user.id != message.reply_to_message.from_user.id:
            await message.reply(CHUNK["adminO"], quote=True)
            return False
    return True


async def handle_image_to_pdf(bot, message, CHUNK):
    """Handle adding an image as a PDF."""
    try:
        imageReply = await message.reply_to_message.reply_text(CHUNK["dlImage"], quote=True)
        if not isinstance(PDF.get(message.chat.id), list):
            PDF[message.chat.id] = []
        loc = await message.reply_to_message.download(f"work/{message.chat.id}.jpg")
        img = Image.open(loc).convert("RGB")
        PDF[message.chat.id].append(img)
        tBTN = await util.createBUTTON(CHUNK["generate"])
        return await imageReply.edit(
            CHUNK["imageAdded"].format(len(PDF[message.chat.id]), message.chat.id)
            + f"\n\n👤: {message.from_user.mention}",
            reply_markup=tBTN,
        )
    except Exception as e:
        logger.exception("Error in handle_image_to_pdf: %s", e)


async def handle_document_to_pdf(bot, message, CHUNK):
    """Handle converting a document to a PDF format."""
    fileNm, fileExt = os.path.splitext(message.reply_to_message.document.file_name)
    if exceeds_file_size_limit(message):
        tBTN = await util.createBUTTON(CHUNK["bigCB"])
        return await message.reply_photo(
            photo=images.BIG_FILE,
            caption=CHUNK["big"].format(MAX_FILE_SIZE, MAX_FILE_SIZE) + f"\n\n👤: {message.from_user.mention}",
            reply_markup=tBTN
        )
    # Continue with document handling here...
    # ...


def exceeds_file_size_limit(message):
    """Check if the file size exceeds the maximum allowed size."""
    return (message.from_user.id not in settings.ADMINS) and \
           MAX_FILE_SIZE and \
           message.reply_to_message.document.file_size >= int(MAX_FILE_SIZE_IN_kiB)
