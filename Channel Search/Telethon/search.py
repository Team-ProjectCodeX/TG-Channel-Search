# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/Qewertyy
# PROVIDED BY https://t.me/ProjectCodeX

# USERBOT REQUIRED!!

from yourbot import(
    userbot as ub,
    app
)
from telethon import(
    errors,
    events, 
    Button
)
from telethon.tl.types import InputMessagesFilterPhotos

@app.on(events.NewMessage(incoming=True, pattern=r"^[!/]search|^[!/]find ?(.*)"))
async def mangastash(event):
  channel_id = -100123456789
  channel_username = "Channel_Username"
  query = event.message.text.split(" ", 1)
  try:
    query = query[1]
  except IndexError:
    await event.reply("This will work like `/search name`\nexample: `/search one piece`")
    return
  if event.reply_to_msg_id:
    event = await event.get_reply_message()
  keybtns = []
  text = ''
  user = f"[{event.sender.first_name}](tg://user?id={event.sender_id})"
  #🔽 this only filter messages based on query with photo in it
  #async for message in ub.iter_messages(channel_id, search=query, filter=InputMessagesFilterPhotos):
  #🔽 will filter every message based on query
  async for message in ub.iter_messages(channel_id, search=query):
    text = message.raw_text
    msg_id = message.id 
    link = f"https://t.me/{channel_username}/{str(msg_id)}"
    btns.append([Button.url(text =f'{text[:20]}',url= link)])
  if btns == []:
    await event.reply(
            "Not found!")
  else:
    await event.reply(
        f"Hey {user}, Found some results..\n",
        buttons=keybtns)
