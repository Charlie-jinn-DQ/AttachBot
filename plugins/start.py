#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#Secret configs
from config import Config

from telegram import ParseMode

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"""Hi Dear.

  I am *Attach Bot*.`

  I can attach medias to your long text 😎`.

  ☛  *Send any media, and reply the text you want, to generate the attached post*

  I can attach medias to your long text.`""", parse_mode=ParseMode.MARKDOWN)
