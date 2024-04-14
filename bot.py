#-- coding: utf-8 --
#import
import os
import copy
import json
import discord

#modules
from modules.log import init_logger

#commands
from commands.self.join import join #加入退出歡迎功能

#define
Logger = init_logger()
cwd = os.getcwd()
configs = {}
token = ""
for name in os.listdir(os.path.join(cwd,"config")): #讀取config目錄
    path = os.path.join(cwd,"config",name)
    if not os.path.isfile(path): #判斷檔案類型
        continue
    if len(name.split(".")) > 2:
        Logger.warning(f"\n偵測到不適當的config檔案\n路徑: \" {path} \"\n此檔案將不會被使用")
    if name.split(".")[len(name.split("."))-1] != "json": #判斷副檔名
        continue
    filename = name.split(".")[0]
    with open(path,encoding='utf-8') as f:
        if filename != "token":
            configs.update(copy.deepcopy(json.load(f)))
        else:
            token = copy.deepcopy((json.load(f))['token'])
print(configs)

#main

class Client(discord.Client):
    async def on_ready(self):
        Logger.info(f'Login as {self.user}!')

bot = Client()
bot.run(token)