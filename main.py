import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

client = discord.Client()


@bot.command(name='comandos')
async def nine_nine(ctx):
    await ctx.send('>marc\n'
                   '>ga\n'
                   '>wily\n'
                   '>xucrut\n'
                   '>carles\n'
                   '>subi\n'
                   '>puta\n'
                   'aporten :)')


@bot.command(name='marc')
async def nine_nine(ctx):
    await ctx.send('marc ets tontissim tiu 🥴marc ets tontissim tiu 🥴'
                   ' marc ets tontissim tiu 🥴marc ets tontissim tiu 🥴')


@bot.command(name='ga')
async def nine_nine(ctx):
    await ctx.send('saluden al dictador 👑 saluden al dictador 👑 '
                   ' saluden al dictador 👑 saluden al dictador 👑')


@bot.command(name='xucrut')
async def nine_nine(ctx):
    await ctx.send('s\'ha quedat bon dia :sun_with_face: sabeu que m\'ha passat avui? :frog:'
                   ' s\'ha quedat bon dia :sun_with_face: sabeu que m\'ha passat avui? :frog:')


@bot.command(name='wily')
async def nine_nine(ctx):
    await ctx.send('hoy me fume un verde 🤑🌿 hoy me fume un verde 🤑🌿'
                   ' hoy me fume un verde 🤑🌿 hoy me fume un verde 🤑🌿')


@bot.command(name='subi')
async def nine_nine(ctx):
    await ctx.send('otra noche de ASMR :lips: otra noche de ASMR :lips:'
                   ' otra noche de ASMR :lips: otra noche de ASMR :lips:')


@bot.command(name='carles')
async def nine_nine(ctx):
    await ctx.send('ke dise gato :point_right:  ke dise gato :cat:'
                   ' ke dise gato :point_right:  ke dise gato :cat:')


@bot.command(name='puta')
async def nine_nine(ctx):
    await ctx.send('magdala :kiss:'
                   ' 654130806')


bot.run('ODEzODgyMDQwOTc3MTk1MDM4.YDVwtw.GKjXtniFHPGJRqPIuVIrm4v4xjs')
