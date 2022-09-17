from discord.ui import Button, View
import discord

class BinButtons(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, view: View, emoji=None):
        super().__init__(label=label, style=style, emoji=emoji)
        self.__view = view

    async def callback(self, interaction):
        await interaction.response.edit_message(content=, view=self.__view)
