import asyncio
import aiohttp
from loguru import logger as l
async def get_furry_img(d: str='today'):
    async with aiohttp.ClientSession() as session:
        async with session.get(f'https://bot.hifurry.cn/everyfurry?date={d}') as resp:
            r = await resp.json()
            return (
                {
                    'pic': r['PictureUrl'],
                    'author': r['AuthorName'],
                    'desc': r['WorkInformation'],
                    'org': r['SourceLink'],
                }
                if r['StateCode']
                else None
            )
print(asyncio.run(get_furry_img('20220918'))) 
