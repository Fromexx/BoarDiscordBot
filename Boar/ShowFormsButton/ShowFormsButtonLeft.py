from discord.ui import Button, View
import discord

class ShowFormsButtonLeft(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, emoji: str, view: View, forms: list, showFormsConfig):
        button = Button(label=label, style=style, emoji=emoji)
        button.callback = self.callback
        self.__view = view
        self.__view.add_item(button)

        self.__forms = forms
        self.__showFormsConfig = showFormsConfig

    async def callback(self, interaction):
        if(self.__showFormsConfig.index == 0):
            return

        self.__showFormsConfig.index  -= 1

        await interaction.response.edit_message(content=self.__forms[self.__showFormsConfig.index], view=self.__view)
