#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Priyanshh
# the logging things
import logging

# the Strings used for this "thing"
from translation import Translation

from pyrogram import (
    Client,
    Filters
)

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Pro  ", "When World will End..😎")
    return expires_at


@Client.on_message(Filters.command(["help", "about"]))
async def help_user(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(Filters.command(["me"]))
async def get_me_info(bot, update):
    # LOGGER.info(update)
    chat_id = str(update.from_user.id)
    chat_id, plan_type, expires_at = GetExpiryDate(chat_id)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.CURENT_PLAN_DETAILS.format(
            chat_id,
            plan_type,
            expires_at
        ),
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )


@Client.on_message(Filters.command(["start"]))
async def start(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_to_message_id=update.message_id
    )


@Client.on_message(Filters.command(["upgrade"]))
async def upgrade(bot, update):
    # LOGGER.info(update)
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.UPGRADE_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
