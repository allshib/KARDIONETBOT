from create_bot import bot
from aiogram import types
import requests
from handlers import config
import json
import os
from bs4 import BeautifulSoup
from aiogram import types
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib.ticker import NullLocator, LinearLocator, FixedLocator


def FindAuthToken(session):
    soup = BeautifulSoup(session.get(config.url).content, features="html.parser")
    urltoken = soup.find('input', dict(name='__RequestVerificationToken'))['value']
    return urltoken


def GetAuthData(mail, passw, urltoken):
    data = {
        'Input.Email': mail,
        'Input.Password': passw,
        '__RequestVerificationToken': urltoken,
        'Input.RememberMe': 'false'
    }
    return data


def Auth(data, url, session):
    session.post(config.url, data=data)
    if(session.get(config.url2).url == config.url2):
        return True
    return False


def CreateDiag(num, date, arr):
    diag = json.dumps({
        "stageId": num,  # Тип анкеты
        "birthDay": date,  # Дата рождения
        "data": arr  # Массив параметров диагностики
    })
    return diag


def UseProgramNew(diag):
    response2 = requests.request("POST", config.urlNew, headers=config.headers, data=diag)
    print(response2.text)
    if (response2.status_code != requests.codes.ok):
        print(response2.status_code)
        return 'Ошибка'
    print('Использую программу')
    return response2.text


def UseProgram(diag, session):
    response2 = session.post(config.url3, json=diag)
    if (response2.status_code != requests.codes.ok):
        print(response2.status_code)
        return 'Ошибка'
    print('Использую программу')
    return response2.text


async def plots(message, ready):
    fig, ax = plt.subplots()
    ax.bar(config.x_list, ready, color=['red', 'green', 'blue', 'violet', 'yellow', 'gray', 'orange', 'violet'])
    plt.ylim(0, 100)
    fig.set_figwidth(11)    # ширина Figure
    fig.set_figheight(8)    # высота Figure
    ax.xaxis.set_major_locator(FixedLocator([0, 1, 2, 3, 4, 5, 6, 7]))
    ax.set_xticklabels(config.x_list, fontsize=8, weight='semibold', rotation=12)
    ax.grid(axis='y')
    ax.yaxis.set_major_locator(LinearLocator(5))
    temp = 'saved_figure{0}.png'.format(message.from_user.id)
    plt.savefig(temp)
    await bot.send_photo(chat_id=message.chat.id, photo=open(temp, 'rb'))
    os.remove(temp)
