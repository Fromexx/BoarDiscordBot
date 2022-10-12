from tkinter.tix import Select
from discord.ext import commands
from discord.ui import View
import discord

from ShowFormsButton.ButtonShowForms import ButtonShowForms
from CreateFormButton.ButtonCreateForm import ButtonCreateForm

from UserForms import UserForms
import config

prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
UserForms = UserForms()

@bot.event
async def on_message(message: discord.Message):
    if(not message.guild):
        if(message.content.startswith(prefix)):
            await bot.process_commands(message)
            return
 
@bot.command()
async def start(ctx):
    view = View()

    ButtonShowForms(label="", style=discord.ButtonStyle.gray, view=view, emoji="ℹ", userForms=UserForms, forms=UserForms.get_all_forms_of_user(ctx.author.id, True), authorID=ctx.author.id)
    ButtonCreateForm(label="", style=discord.ButtonStyle.gray, view=view, emoji="➕", client=bot, ctx=ctx)

    await ctx.send(content="MainMessage", view=view)

@bot.command()
async def clear(ctx, count):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(count))

bot.run(config.TOKEN)
