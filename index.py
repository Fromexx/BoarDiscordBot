from discord.ext import commands
from discord.ui import Button, View
import discord

from UserForms import UserForms
import config

prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
botId = 1005177524181024848
UserForms = UserForms()
index = 0

def add_number_at_index(number: int):
    global index
    index += number

@bot.event
async def on_ready():
    print("Bot has logged!")

@bot.event
async def on_message(message: discord.Message):
    if(message.content.startswith(prefix)):
        await bot.process_commands(message)
        return

    if(message.channel.id == 1018207042042875934 and message.author.id != botId):
        UserForms.write_form_on_file(message.content + f" User: {message.author.id}")

@bot.command()
async def alp(ctx):
    global index
    index = 0

    forms = UserForms.get_all_forms_of_user(ctx.author.id, True)
    view = View()

    async def buttonLeft_clicked(interaction):
        if(index == 0):
            return
        add_number_at_index(-1)
        await interaction.response.edit_message(content=forms[index], view=view)

    async def buttonRight_clicked(interaction):
        if(index == len(forms) - 1):
            return
        add_number_at_index(1)
        await interaction.response.edit_message(content=forms[index], view=view)

    async def buttonBin_clicked(interaction):
        UserForms.delete_form_of_user(ctx.author.id, index)
        forms.pop(index)

        if(index > 0):
            add_number_at_index(-1)

        await interaction.response.edit_message(content=forms[index], view=view)

    buttonLeft = Button(label="", style=discord.ButtonStyle.gray, emoji="⬅")
    buttonRight = Button(label="", style=discord.ButtonStyle.gray, emoji="➡")
    buttonBin = Button(label="", style=discord.ButtonStyle.gray, emoji="🗑")
    buttonLeft.callback = buttonLeft_clicked
    buttonRight.callback = buttonRight_clicked
    buttonBin.callback = buttonBin_clicked
    view.add_item(buttonLeft)
    view.add_item(buttonRight)
    view.add_item(buttonBin)

    await ctx.send(forms[0], view=view)
 
@bot.command()
async def clear(ctx, count):
    await ctx.message.delete()
    await ctx.channel.purge(limit=int(count))

bot.run(config.TOKEN)
