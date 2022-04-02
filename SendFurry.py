from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import time
from DecisionSource import decision


today_furry = on_keyword({'今日兽兽'})
# on_keyword是接收某关键词的意思，api

@today_furry.handle()
async def send_audio(bot: Bot, event: Event, state: T_State):
    msg_text = decision()
    # msg_date = f"[CQ:at,qq={msg_text[0]}]"
    # msg_pic_text = f"[CQ:at,qq={msg_text[1]}]"
    try:
        if msg_text[4] == 1:
            msg_pic = f"[CQ:image,file={msg_text[3]},type=show,id=40004]"
            time.sleep(0.5)
            await today_furry.send(Message(msg_text[1]))
            time.sleep(0.5)
            await today_furry.send(Message(msg_text[2]))
            time.sleep(0.5)
            await today_furry.send(Message(msg_pic))
            time.sleep(0.5)
            print(msg_text)
        else:
            await today_furry.send(Message('emmm，今天貌似没有推送唉owo'))
    except:
        await today_furry.send(Message('emmm，今天貌似没有推送唉owo'))


    
