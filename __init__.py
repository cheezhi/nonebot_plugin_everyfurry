from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message

from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import time
from .DecisionSource import decision
import urllib.parse
import urllib.request
from urllib import request, error




today_furry = on_command("everyfurry", aliases={'今日兽兽',})

@today_furry.handle()
async def send_audio(bot: Bot, event: Event, state: T_State):
    msg_text = decision()

    try:
        if msg_text[4] != 0:
            msg_pic = f"[CQ:image,file={msg_text[3]},id=40000]"
            time.sleep(2)
            await today_furry.send(Message(msg_text[1]))
            time.sleep(2)
            await today_furry.send(Message(msg_text[2]))
            time.sleep(2)
            await today_furry.send(Message(msg_pic))
            time.sleep(2)
            print(msg_text)
        else:
            await today_furry.send(Message('emmm，今天貌似没有推送唉owo'))
    except Exception as e:
        time.sleep(2)
        await today_furry.send(f'发生错误：{e}')

            
