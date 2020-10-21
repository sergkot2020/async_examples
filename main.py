import asyncio
from datetime import datetime


async def save_text_in_db(v):
    print(f'начали сохранение => {v}')
    await asyncio.sleep(1)
    print(f'закончили запись в БД => {v}')


async def main3():
    urls = [1, 2, 3, 4, 5]
    coros = [get_from_db(i) for i in urls]
    result = await asyncio.gather(*coros)
    print(result)
    return result


async def get_from_db(i):
    print(f'Делаем долгий запрос => {i}')
    await asyncio.sleep(i)
    print(f'Закончили запрос => {i}')
    await save_text_in_db(i)
    print(f'done => {i}')
    return f'done => {i}'

start = datetime.now()
print(start)
asyncio.run(main3())
finish = datetime.now()
print(finish)
print(f'time => {finish - start}')



