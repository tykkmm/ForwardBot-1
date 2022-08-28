import os 
import logging
import random
import asyncio 
from os import environ
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
import re
import json
import base64
logger = logging.getLogger(__name__) 

START_PIC = environ.get("START_PIC", "https://telegra.ph/file/c832b9b2cf56637e762e9.jpg") 

@Client.on_message(filters.private & filters.command(["start"])) 
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""👋 Hai {message.from_user.mention} \nI'm an advanced forward bot with some useful features!""", 
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("❤ Support", url='https://t.me/Vysakh_XD'),
           InlineKeyboardButton("⚡️ Updates", url='https://t.me/Vysakh_XD')
           ],[
           InlineKeyboardButton("❓️ Help ❓️", callback_data='help')
           ]]   
          )
       )
@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋 Hai {message.from_user.mention} \nI'm an advanced forward bot with some useful features!""", 
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("❤ Support", url='https://t.me/Vysakh_XD'),
                InlineKeyboardButton("⚡️ Updates", url='https://t.me/Vysakh_XD')
                ],[
                InlineKeyboardButton("❓️ Help ❓️", callback_data='help')
                ]]   
                )
            )
        return 
    elif data == "help":
        await query.message.edit_text( 
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[ 
                InlineKeyboardButton("◀️ 𝙱𝙰𝙲𝙺", callback_data = "start")
                ]]
                )
            )
