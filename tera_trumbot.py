# ©@fligher

import os
import traceback
import requests
from pyrogram import StopPropagation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import MessageNotModified
import logging
import asyncio
from datetime import datetime
from pyrogram.enums import ChatMemberStatus
from os import environ
import time
import datetime
import re
logging.basicConfig(level=logging.INFO)


api_id = environ.get('TELEGRAM_API','') #telegram api
if len(api_id) == 0:
    logging.error("TELEGRAM_API variable is missing! Exiting now")
    exit(1)

api_hash = environ.get('TELEGRAM_HASH', '') #telegram hash
if len(api_hash) == 0:
    logging.error("TELEGRAM_HASH variable is missing! Exiting now")
    exit(1)
    
bot_token = environ.get('BOT_TOKEN', '') #telegram bot token
if len(bot_token) == 0:
    logging.error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)

dump_id = environ.get('DUMP_CHAT_ID', '') #dumpchat id
if len(dump_id) == 0:
    logging.error("DUMP_CHAT_ID variable is missing! Exiting now")
    exit(1)
else:
    dump_id = int(dump_id)

fsub_id = environ.get('FSUB_ID', '') #force sub id must bot present in that chat as admin with full rights
if len(fsub_id) == 0:
    logging.error("FSUB_ID variable is missing! Exiting now")
    exit(1)
else:
    fsub_id = int(fsub_id)
  
ad_name=environ.get("ADMIN_NAME",'') #admin name without @
if len(ad_name) == 0:
    logging.error("ADMIN_NAME variable is missing! Exiting now")
    exit(1)
else:
  ad_name=("fligher")

trumbot = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

#must include admin id in below fields
#no mongodb used here So after restart you need to add the auth users using /add

authorized_users = [] #add admin_id
auth = [] #add admin_id
banned_users=[] #don't add your id 🤣
RAPIDAPI_KEY = "11eee86599mshbf603b746bfbec8p15b3cfjsn2d5c3a75f0f6" by @fligher don't change it 

@trumbot.on_message(filters.command("add") & filters.user(auth))
async def handle_add_command(client, message: Message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    new_user_id = int(message.text.split()[1])
  if new_user_id in authorized_users:
      await message.reply_text("User Already added check here /listid")
  authorized_users.append(new_user_id)
  current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  s=await message.reply_text(f"#ADDED\n\nUser ID {new_user_id}\n added to the authorized list.\n{current_time}")
  await client.send_message(dump_id,s)
  try:
      await client.send_photo(chat_id=new_user_id,photo="https://th.bing.com/th/id/OIG1.BM1ARNXCdPpLPYlhcZMG?w=1024&h=1024&rs=1&pid=ImgDetMain",caption="You can now use the Bot \nEnjoy ........😃😃😃😃😃",ttl_seconds=5)
  except Exception as e:
      logging.error(f"Error sending message to removed user: {e}")


@trumbot.on_message(filters.command("remove") & filters.user(auth))
async def handle_remove_command(client, message: Message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    new_user_id = int(message.text.split()[1])
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    authorized_users.remove(new_user_id)
    ds=await message.reply_text(f"#REMOVED\n\nUser ID {new_user_id}\nhas been removed from the authorized users list\n\n{current_time}.")
    await client.send_message(dump_id,ds)
    # Send a message to the removed user
    try:
        await client.send_message(chat_id=new_user_id, text="You have been removed from the list ,so You Can't use the bot @{ad_name}.")
    except Exception as e:
        logging.error(f"Error sending message to removed user: {e}")

@trumbot.on_message(filters.command("listid") & filters.user(auth))
async def handle_listid_command(client, message: Message):
    if authorized_users:
        user_ids_string = ", ".join(str(user_id) for user_id in authorized_users)
        await message.reply_photo(photo="https://th.bing.com/th/id/OIG1.6n3kV_Q6QFxMnKv5Wrng?pid=ImgGn",caption=f"ALOWED user IDs:\n<code>{user_ids_string}</code>\n")
    else:
        await message.reply_text("No authorized users yet.")

@trumbot.on_message(filters.command("bids") & filters.user(auth))
async def handle_bids_command(client, message: Message):
    if banned_users:
        user_ids_string = ", ".join(str(user_id) for user_id in banned_users)
        await message.reply_text(f"Banned user IDs:\n<code>{user_ids_string}</code>\n")
    else:
        await message.reply_text("No banned users yet.")

@trumbot.on_message(filters.command("ban_user") & filters.user(auth))
async def handle_ban_command(client, message: Message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    new_user_id = int(message.text.split()[1])
  if new_user_id in banned_users:
      await message.reply_text("User Already banned check here /bids")
  banned_users.append(new_user_id)
  current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  s=await message.reply_text(f"#BANNED\n\nUser ID {new_user_id}\nTIME : {current_time}")
  await client.send_message(ldump_id,s)
  try:
      await client.send_photo(chat_id=new_user_id, photo="https://th.bing.com/th/id/OIG4.T5ZyP2wXKGQXTV4gOsW.?w=1024&h=1024&rs=1&pid=ImgDetMain",caption="You were Banned 🚫 contact @{ad_name}.",ttl_seconds=10)
  except Exception as e:
      logging.error(f"Error in ban user: {e}")
    


@trumbot.on_message(filters.command("unban_user") & filters.user(auth))
async def handle_unban_command(client, message: Message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    new_user_id = int(message.text.split()[1])
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    banned_users.remove(new_user_id)
    ds=await message.reply_text(f"#UN_BAN_USER\n\nUser ID {new_user_id}\nhas been removed from the banned_users list\n\n{current_time}.")
    await client.send_message(ldump_id,ds)
    # Send a message to the removed user
    try:
        await client.send_photo(chat_id=new_user_id,photo="https://th.bing.com/th/id/OIG4.vkXa3ZWeWu.9ofPqnxi.?pid=ImgGn",caption="You are freed now, but **WE** will watching you 👀.",ttl_seconds=10)
    except Exception as e:
        logging.error(f"Error unbanning user: {e}")

@trumbot.on_message(filters.command("aboutme"))
async def handle_aboutme_command(client, message: Message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    
    # Check if user is VIP
    is_vip = user_id in authorized_users
    is_banned = user_id in banned_users

    status_message = f"Your Status🔮\n\nYour Name:{user_mention}\n\nYour UserID:{user_id}\n\n"
    if is_vip:
        status_message += "✅ AUTHORISED: Yes[You Are A Member conatct]\n\n"
    else:
        status_message += "❌ UNAUTHORISED: No[You Are a Non Member@{ad_name}]\n\n"
    if is_banned:
        status_message += "❌ Banned: Yes[You are Banned to use this bot@{ad_name}]\n\n"
    else:
        status_message += "✅ Banned: No[You can Use this bot Freely]\n\n"

    await message.reply_photo(photo="https://th.bing.com/th/id/OIG3.xmDHokCGzHGbd67XMhw1?w=1024&h=1024&rs=1&pid=ImgDetMain",caption=f"{status_message}",ttl_seconds=10)

@trumbot.on_message(filters.command("start") & filters.private)
async def startprivate(client, message):
    # return
    sticker_message = await message.reply_sticker("CAACAgUAAxkBAAEMQHdmYo50TrYqla-D-9MTJ9cj4tUiGwACewUAAkqEQFcT4jJC1FozBTUE")
    await asyncio.sleep(2)
    await sticker_message.delete()
    user_mention = message.from_user.mention
    reply_message = f"ᴡᴇʟᴄᴏᴍᴇ, {user_mention}.\n\n🌟 ɪ ᴀᴍ ᴀ ᴛᴇʀᴀʙᴏx ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ. sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴛʜɪɴ ғᴇᴡ sᴇᴄᴏɴᴅs ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ ✨\n\n𝖴𝗌𝖾 <blockquote>/help</blockquote> 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖼𝗁𝖾𝖼𝗄 𝗆𝗒 𝖿𝖾𝖺𝗍𝗎𝗋𝖾.\n\nAnd Check Your Status <blockquote>/aboutme</blockquote>"
    join_button = InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://t.me/movie_time_botonly")
    developer_button = InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ ⚡️", url="https://t.me/fligher")
    bt_button=InlineKeyboardButton("Bot List🤖",url="https://te.legra.ph/TRUMBOTS-BOTS-LIST-06-01")
    reply_markup = InlineKeyboardMarkup([[join_button, developer_button],[bt_button]])

    await message.reply_photo(
        photo="https://th.bing.com/th/id/OIG4.kIKwAP6q4rN21rOhb71Z?pid=ImgGn",
        caption=reply_message,
        reply_markup=reply_markup
    )
    raise StopPropagation

async def is_user_member(client, user_id):
    try:
        member = await client.get_chat_member(fsub_id, user_id)
        logging.info(f"User {user_id} membership status: {member.status}")
        if member.status in [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]:
            return True
        else:
            return False
    except Exception as e:
        logging.error(f"Error checking membership status for user {user_id}: {e}")
        return False


@trumbot.on_message(filters.command("about"))
async def about_command(client,message):
    text = f"""<b>♻️ ᴍʏ ɴᴀᴍᴇ : TeraBypasser
🌀 ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/MOVIE_Time_BotOnly">​🇹​​🇷​​🇺​​🇲​​🇧​​🇴​​🇹​​🇸</a>
🌺 ʜᴇʀᴏᴋᴜ : <a href="https://heroku.com/">ʜᴇʀᴏᴋᴜ</a>
📑 ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ 3.10.5</a>
🇵🇲 ғʀᴀᴍᴇᴡᴏʀᴋ : <a href="https://docs.pyrogram.org/">ᴘʏʀᴏɢʀᴀᴍ 2.0.30</a>
👲 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href="https://t.me/fligher">​🇲​​🇾​​🇸​​🇹​​🇪​​🇷​​🇮​​🇴​</a></b>
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('👥 Group', url=f"https://t.me/trumbotchat"),
            InlineKeyboardButton('TRUMBOTS', url=f"https://t.me/movie_time_botonly")
            ],[
            InlineKeyboardButton('❤️Me', url=f"https://t.me/fligher"),
            InlineKeyboardButton('Bot Lists 🤖', url=f"https://te.legra.ph/TRUMBOTS-BOTS-LIST-06-01"),
            ]
    ]
    x=await message.reply_photo(
        photo="https://th.bing.com/th/id/OIG4.kIKwAP6q4rN21rOhb71Z?pid=ImgGn",
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await asyncio.sleep(10)
    await message.delete()
    await x.delete()

@trumbot.on_message(filters.command("help"))
async def help_command(client,message):
    text = f"""𝖧𝗂 𝖨 𝖺𝗆 𝖲𝗂𝗆𝗉𝗅𝖾 𝖳𝖾𝗋𝖺𝖡𝗈𝗑 𝖡𝗒𝗉𝖺𝗌𝗌𝖾𝗋 😶‍🌫️ 𝖺𝗇𝖽 𝖣𝗈𝗐𝗇𝗅𝗈𝖺𝖽𝖾𝗋 ⚡️

🌟𝖨 𝖢𝖺𝗇 𝖶𝗈𝗋𝗄 𝖫𝗂𝗇𝗄𝗌 𝖮𝗇𝖾 𝖡𝗒 𝖮𝗇𝖾 𝖲𝖾𝗇𝖽 𝖳𝗁𝖾 𝖫𝗂𝗇𝗄𝗌 𝖮𝗇𝖾 𝖺𝖿𝗍𝖾𝗋 𝖠𝗇𝗈𝗍𝗁𝖾𝗋\n
#NOTE\n\n✨Due To Some Restriction Only auth users can use the bot
𝖬𝗒 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌 🕹️:
/start - ^_^
/about - ♨︎_♨︎
/help - ?!
/aboutme - You🫵🏻
/bypass - Bypass terabox links
/add - ADMIN COMMAND [Add user to use the bot]
/remove - ADMIN COMMAND [Remove User ]
/listid - ADMIN COMMAD [check  auth users]
/bids - ADMIN COMMAND [check banned users]
𝖱𝖾𝗉𝗈𝗋𝗍 𝖠𝗇𝗒 𝖤𝗋𝗋𝗈𝗋: @TRUMBOTCHAT
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('👥 Group', url=f"https://t.me/trumbotchat"),
            InlineKeyboardButton('TRUMBOTS', url=f"https://t.me/movie_time_botonly")
            ],[
            InlineKeyboardButton('❤️Me', url=f"https://t.me/fligher"),
            InlineKeyboardButton('Bot Lists 🤖', url=f"https://te.legra.ph/TRUMBOTS-BOTS-LIST-06-01"),
            ]
    ]
    x=await message.reply_photo(
        photo="https://th.bing.com/th/id/OIG1.wpCbEABl07148yEBR_vl?pid=ImgGn",
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    await asyncio.sleep(15)
    await message.delete()
    await x.delete()

@trumbot.on_message(filters.command(["bypass"]))
async def rterabox_downloader(client: Client, message: Message):
    user_id = message.from_user.id
    is_member = await is_user_member(client, user_id)

    if not is_member:
        join_button = InlineKeyboardButton("ᴊᴏɪɴ ❤️🚀", url="https://t.me/movie_time_botonly") #add your force subchannel url
        reply_markup = InlineKeyboardMarkup([[join_button]])
        await message.reply_text("😈ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ😈.", reply_markup=reply_markup)
        return 
  
    if user_id not in normal_user:
        await message.reply_text("SOrry Dude DUe To SOme Restrictions Only Auth Peoples Can USe, If You Want Acces => contact admin @fligher")
        return
    
    if user_id in banned_users:
        await message.reply_text("You are or banned👁️‍🗨️. contact admin @fligher")
        return

    if len(message.text.split()) == 1:  # Check if only the command is sent
        x=await message.reply_photo(
            photo="https://th.bing.com/th/id/OIG1.wpCbEABl07148yEBR_vl?w=1024&h=1024&rs=1&pid=ImgDetMain",  # Replace with your image URL
            caption="Send like this: `/bypass your_terabox_link`",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(text="Developer", url="https://t.me/movie_time_botonly")]]
            )
        )
        await asyncio.sleep(5)
        await message.delete()
        await x.delete()
   
    else:
        b=await client.send_message(chat_id=message.chat.id,text="Bypassing................")
        
    try:
        url = message.text.split(" ",1)[1].strip()
        response = requests.get(
            "https://terabox-downloader-tool.p.rapidapi.com/api",
            headers={
                "x-rapidapi-key": RAPIDAPI_KEY,
                "x-rapidapi-host": "terabox-downloader-tool.p.rapidapi.com"
            },
            params={"data":url}
        )
            
    
    
        response.raise_for_status()  # Raise an exception for bad status codes
        download_link = response.json()["link"]
        thumb_p=response.json()["thumb"]
        si=response.json()["size"]
        video_title=response.json()["file_name"]
                


        markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text='Downlaod',
                            url=download_link
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            text='DeveLopeR',
                            url='https://t.me/movie_time_botonly'
                        )
                    ]
                ]
            )
        await asyncio.sleep(5)
        await message.delete()
        await b.delete()
        message_text = f"🎬 <b>Title:</b> {video_title}\n\n📦 <b>Size:</b>{si}\n\nMade with ❤ 🏆 by @TRUMBOTCHAT\n\nYour Terabox link is bypassed check below button"
        bp=await client.send_photo(
                chat_id=message.chat.id,
                photo=thumb_p,
                caption=message_text,
                reply_markup=markup
            )
        await client.send_message(chat_id=ldump_id,text=f"#BYPASSED📄\n\nNAME👦🏻👧🏻: {user_mention}\n\nLINK🖇️: {url}\n\nLINK📍:{download_link}\n\nWHEN🕐:{current_time}")
    except Exception as e:
        pass
if __name__ == "__main__":
    trumbot.run()
