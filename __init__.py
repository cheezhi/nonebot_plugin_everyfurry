from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message

from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import time
import urllib.parse
import urllib.request
from urllib import request, error
import asyncio
import aiohttp
from loguru import logger as l

today_furry = on_command("everyfurry", aliases={'今日兽兽', })


@today_furry.handle()
async def send_furry(bot: Bot, event: Event, state: T_State):
    msg = await get_furry_img()
    try:
        if msg is not None:
            msg_pic = f"[CQ:image,file={msg['pic']},id=40000]"
            await today_furry.send(
                Message(
                    f'嗷呜，{time.strftime("%m", time.localtime())}月{time.strftime("%d", time.localtime())}日兽兽推送'
                )
            )

            await today_furry.send(Message(
                f'''
来源：{msg["author"]}
简介：{msg["desc"]}
原文链接：{msg["org"]}
详情：{msg['date']}
'''))
            await today_furry.send(Message(msg_pic))
            l.info(msg)
        else:
            await today_furry.send(Message('emmm，今天貌似没有推送唉owo'))
    except Exception as e:
        asyncio.sleep(2)
        await today_furry.send(f'发生错误：{e}')


async def get_furry_img(d: str = 'today'):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://bot.hifurry.cn/everyfurry?date={d}') as resp:
            r = await resp.json()
            return (
                {
                    'pic': r['PictureUrl'],
                    'author': r['AuthorName'],
                    'desc': r['WorkInformation'],
                    'org': r['SourceLink'],
                    'date': f'https://bot.hifurry.cn/everyfurry?date={time.strftime("%Y%m%d")}',
                }
                if r['StateCode']
                else None
            )
