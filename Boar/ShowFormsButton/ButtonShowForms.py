from discord.ui import View, Select, Button
import discord

from ShowFormsButton.ShowFormsButtonLeft import ShowFormsButtonLeft
from ShowFormsButton.ShowFormsButtonRight import ShowFormsButtonRight
from ShowFormsButton.ShowFormsButtonBin import ShowFormsButtonBin
from ShowFormsConfig import Config
from UserForms import UserForms

class ButtonShowForms(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, view: View, emoji:None, userForms, forms: list, authorID: int):
        button = Button(label=label, style=style, emoji=emoji)
        button.callback = self.buttonShowForms_clicked
        view.add_item(button)
        self.__forms = forms
        self.__authorId = authorID
        self.__userForms = userForms

        self.index = 0

    async def buttonShowForms_clicked(self, interaction):
        if(len(UserForms().get_all_forms_of_user(self.__authorId, False)) == 0):
            await interaction.response.send_message(content="You haven`t any forms!")
            return

        showFormsView = View()
        showFormsConfig = Config()

        ShowFormsButtonLeft(label="", style=discord.ButtonStyle.gray, emoji="⬅", view=showFormsView, forms=self.__forms, showFormsConfig=showFormsConfig)
        ShowFormsButtonRight(label="", style=discord.ButtonStyle.gray, emoji="➡", view=showFormsView, forms=self.__forms, showFormsConfig=showFormsConfig)
        ShowFormsButtonBin(label="", style=discord.ButtonStyle.gray, emoji="🗑", view=showFormsView, forms=self.__forms, showFormsConfig=showFormsConfig, userForms=self.__userForms, authorId=self.__authorId)

        await interaction.response.send_message(content=self.__forms[0], view=showFormsView)
