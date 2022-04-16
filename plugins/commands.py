import os
import logging
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION
from utils import Media, get_file_details
from pyrogram.errors import UserNotParticipant
from database import Database
logger = logging.getLogger(__name__)

Pikachu = ["https://telegra.ph/file/0dffd7381e3b3c4f6e08f.jpg",
           "https://telegra.ph/file/510985728b633ebbb71d0.jpg",
           "https://telegra.ph/file/bdb5db81985f0b896bb80.jpg",
           "https://telegra.ph/file/b4f803331e770982f2931.jpg",
           "https://telegra.ph/file/43508ab0a34dbc621e760.jpg",
           "https://telegra.ph/file/0dffd7381e3b3c4f6e08f.jpg",
           "https://telegra.ph/file/510985728b633ebbb71d0.jpg",
           "https://telegra.ph/file/bdb5db81985f0b896bb80.jpg",
           "https://telegra.ph/file/b4f803331e770982f2931.jpg",
           "https://telegra.ph/file/bdb5db81985f0b896bb80.jpg",
           "https://telegra.ph/file/b4f803331e770982f2931.jpg",
           "https://telegra.ph/file/b4f803331e770982f2931.jpg",
           "https://telegra.ph/file/510985728b633ebbb71d0.jpg"]




@Client.on_message(filters.command("start"))
async def start(bot, cmd):
    usr_cmdall1 = cmd.text
    if usr_cmdall1.startswith("/start subinps"):
        if AUTH_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
            try:
                user = await bot.get_chat_member(int(AUTH_CHANNEL), cmd.from_user.id)
                if user.status == "kicked":
                    await bot.send_message(
                        chat_id=cmd.from_user.id,
                        text="Sorry Sir, You are Banned to use me.",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                ident, file_id = cmd.text.split("_-_-_-_")
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="** 𝙷𝙴𝚈 𝙱𝚁𝚄𝙷 🙋‍♀️ 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴𝙽'𝚃 𝚈𝙴𝚃 𝙹𝙾𝙸𝙽𝙴𝙳 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙼𝚈 𝚄𝙿𝙳𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚜𝙴 𝙼𝙴\n𝙰𝙵𝚃𝙴𝚁 𝙹𝙾𝙸𝙽𝚒𝙽𝙶 𝙲𝙻𝙸𝙲𝙺 𝚃𝚁𝚈 𝙰𝙶𝙰𝙸𝙽 𝚃𝙾 𝙶𝙴𝚃 𝚈𝚘𝚄𝚁 𝙼𝙾𝚅𝙸𝙴 😇!! **",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔰 JOIN OUR CHANNEL 🔰", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton(" 🔄 𝙏𝙧𝙮 𝘼𝙜𝙖𝙞𝙣", callback_data=f"checksub#{file_id}")
                            ]
                        ]
                    ),
                    parse_mode="markdown"
                )
                return
            except Exception:
                await bot.send_message(
                    chat_id=cmd.from_user.id,
                    text="Something went Wrong.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        try:
            ident, file_id = cmd.text.split("_-_-_-_")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [[

                       InlineKeyboardButton("🍿 𝙅𝙊𝙄𝙉 𝙊𝙐𝙍 𝙂𝙍𝙊𝙐𝙋 🍿", url="https://t.me/Movies_4you"),
                    ]]
                await bot.send_cached_media(
                    chat_id=cmd.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")
    elif len(cmd.command) > 1 and cmd.command[1] == 'subscribe':
        invite_link = await bot.create_chat_invite_link(int(AUTH_CHANNEL))
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💙𝙅𝙊𝙄𝙉 𝙈𝙔 𝙐𝙋𝘿𝘼𝙏𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇🧡", url=invite_link.invite_link)
                    ]
                ]
            )
        )
    else:
        await cmd.reply_photo(photo = random.choice(Pikachu),
            caption=START_MSG,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("➕ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ➕", url= "https://t.me/Mafia_AutoFilter_V3_Bot?startgroup=true")
                    ],
                    [
                        InlineKeyboardButton("𝙎𝙚𝙖𝙧𝙘𝙝 𝙝𝙚𝙧𝙚🔎", switch_inline_query_current_chat=''),
                        InlineKeyboardButton("𝘼𝙣𝙮 𝙃𝙚𝙡𝙥 💡", url="telegram.me/Movies_4you")
                    ],
                    [
                        InlineKeyboardButton("𝙈𝙮 𝘿𝙚𝙫 🔥", url="https://t.me/KingOf_univers"),
                        InlineKeyboardButton("𝙐𝙥𝙙𝙖𝙩𝙚𝙯 🤓", url="https://t.me/Movies4youbackup")
                    ],
                    [
                        InlineKeyboardButton("𝘼𝙗𝙤𝙪𝙩 😎", callback_data="about")
                    ]    
                ]
            )
        )


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Show total files in database"""
    msg = await message.reply("Peace Mama Processing...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'Peace Mama Itha Total Saved files 🔥: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        await msg.edit('File not found in database')


@Client.on_message(filters.private & filters.command("stats"))
async def sts(c, m):
    if not await db.is_user_exist(update.from_user.id):
	    await db.add_user(update.from_user.id)
    if m.from_user.id not in ADMIN_ID:
        await m.delete()
        return
    await m.reply_text(
        text=f"**Total Users in Database 📂:** `{await db.total_users_count()}`\n\n**Total Users with Notification Enabled 🔔 :** `{await db.total_notif_users_count()}`",
        parse_mode="Markdown",
        quote=True
    )


@Client.on_message(filters.private & filters.command("broadcast") & filters.user(BOT_OWNER) & filters.reply, group=1)
async def broadcast(bot, update):
	broadcast_ids = {}
	all_users = await db.get_all_users()
	broadcast_msg = update.reply_to_message
	while True:
	    broadcast_id = ''.join([random.choice(string.ascii_letters) for i in range(3)])
	    if not broadcast_ids.get(broadcast_id):
	        break
	out = await update.reply_text(text=f"Broadcast Started! You will be notified with log file when all the users are notified.")
	start_time = time.time()
	total_users = await db.total_users_count()
	done = 0
	failed = 0
	success = 0
	broadcast_ids[broadcast_id] = dict(total = total_users, current = done, failed = failed, success = success)
	async with aiofiles.open('broadcast.txt', 'w') as broadcast_log_file:
	    async for user in all_users:
	        sts, msg = await send_msg(user_id = int(user['id']), message = broadcast_msg)
	        if msg is not None:
	            await broadcast_log_file.write(msg)
	        if sts == 200:
	            success += 1
	        else:
	            failed += 1
	        if sts == 400:
	            await db.delete_user(user['id'])
	        done += 1
	        if broadcast_ids.get(broadcast_id) is None:
	            break
	        else:
	            broadcast_ids[broadcast_id].update(dict(current = done, failed = failed, success = success))
	if broadcast_ids.get(broadcast_id):
	    broadcast_ids.pop(broadcast_id)
	completed_in = datetime.timedelta(seconds=int(time.time()-start_time))
	await asyncio.sleep(3)
	await out.delete()
	if failed == 0:
	    await update.reply_text(text=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.", quote=True)
	else:
	    await update.reply_document(document='broadcast.txt', caption=f"broadcast completed in `{completed_in}`\n\nTotal users {total_users}.\nTotal done {done}, {success} success and {failed} failed.")
	os.remove('broadcast.txt')
