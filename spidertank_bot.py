import discord
from discord.ext import commands
import pickle

token = ""

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), status=discord.Status.online, activity=None)

@bot.command(aliases=['인사', '헬로'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 헬로~')
'''
IDs = {'id':'0000000000000000'}

with open('IDs.pickle','wb') as f:
        pickle.dump(IDs, f)
        f.close()
'''
with open('IDs.pickle','rb') as f:
        IDs = pickle.load(f)
        f.close()

print(IDs)

@bot.command()
async def helpme(ctx):
    await ctx.reply("Hi, I'm [KING]Spider Tanks BOT. Here's usage!\n\n!id (username) :아이디조회\n\n!save (username) (user's id)  :아이디등록\n\n!delete (username)  :아이디삭제\n\n!list  :모든 ID보기\n\n!helpme  :도움말")


@bot.command()
async def save(ctx, nick, id):
    IDs[f"{nick}"] = id
    with open('IDs.pickle','wb') as f:
        pickle.dump(IDs, f)
        f.close()
    await ctx.reply(f'{nick}님의 user ID: {id} 추가완료!')


@bot.command()
async def delete(ctx, nick):
    try:
        id = IDs[f"{nick}"]
        await ctx.reply(f'{nick}님의 user ID: {id} 삭제완료!')
    except KeyError:
        nick = nick.lower()
        try:
            id = IDs[f"{nick}"]
        except KeyError:
            await ctx.reply(f'{nick}님의 user ID는 저장되어있지 않습니다.') 
    

@bot.command()
async def id(ctx, nick):
    try:
        id = IDs[f"{nick}"]
        await ctx.reply(f'{nick}님의 user ID: {id}')
    except KeyError:
        nick = nick.lower()
        print(nick)
        try:
            id = IDs[f"{nick}"]
        except KeyError:
            await ctx.reply(f'{nick}님의 user ID는 저장되어있지 않습니다.')    
        

@bot.command()
async def list(ctx):
    l=''
    for user in IDs.keys():
        id = IDs[f'{user}']
        l = l + f"{user},  {id}\n"
        
    await ctx.reply(f'{l}')

    
bot.run(token)
