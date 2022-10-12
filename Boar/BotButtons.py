from discord.ui import Button, View
import discord

class BotButton(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, view: View, callback, emoji:None):
        button = Button(label=label, style=style, emoji=emoji)
        button.callback = callback
        view.add_item(button)
