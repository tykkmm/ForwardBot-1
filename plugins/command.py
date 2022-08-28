import os
import logging
import random
import asyncio
from pyrogram import Client, filters, enums 
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
import re
import json
import base64
logger = logging.getLogger(__name__) 

FLOOD = int(environ.get("FLOOD", "10"))
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
