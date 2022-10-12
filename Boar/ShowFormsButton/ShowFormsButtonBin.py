from discord.ui import Button, View
import discord

class ShowFormsButtonBin(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, emoji: str, view: View, forms: list, showFormsConfig, userForms, authorId: int):
        button = Button(label=label, style=style, emoji=emoji)
        button.callback = self.callback
        self.__view = view
        self.__view.add_item(button)

        self.__forms = forms
        self.__showFormsConfig = showFormsConfig
        self.__userForms = userForms
        self.__authorId = authorId

    async def callback(self, interaction):
        self.__userForms.delete_form_of_user(self.__authorId, self.__showFormsConfig.index)
        self.__forms.pop(self.__showFormsConfig.index)

        if(self.__showFormsConfig.index == len(self.__forms)):
            self.__showFormsConfig.index -= 1

        if(self.__showFormsConfig.index == -1):
            await interaction.response.edit_message(content="You haven`t any forms!", view=None)
            return
        
        await interaction.response.edit_message(content=self.__forms[self.__showFormsConfig.index], view=self.__view)
