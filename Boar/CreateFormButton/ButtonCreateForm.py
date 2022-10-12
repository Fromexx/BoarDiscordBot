from discord.ui import View, Select, Button
import discord

from CreateFormButton.SelectItemTypeCallback import SelectItemType
import CreateFormButton.NewForm

from Enum import WeaponType

class ButtonCreateForm(Button):
    def __init__(self, label: str, style: discord.ButtonStyle, view: View, emoji:None, client: discord.Client, ctx):
        button = Button(label=label, style=style, emoji=emoji)
        button.callback = self.buttonCreateForm_clicked
        view.add_item(button)

        CreateFormButton.NewForm.createNewForm()
        
        self.__client = client
        self.__ctx = ctx

        self.index = 0

    async def buttonCreateForm_clicked(self, interaction):
        createFormView = View()

        self.__selectItemType = Select(
            placeholder="Select a item type!",
            options=
            [
                discord.SelectOption(label="Weapon", emoji="🔫", description="Weapon item"),
                discord.SelectOption(label="Graffiti", emoji="🖌️", description="Graffiti item"), 
                discord.SelectOption(label="Sticker", emoji="💮", description="Sticker for weapon"),
                discord.SelectOption(label="Patch", emoji="⚜", description="Agent with a patch"),
                discord.SelectOption(label="Agent", emoji="🤺", description="Agent"),
                discord.SelectOption(label="Key", emoji="🗝", description="Key for a container"),
                discord.SelectOption(label="Container", emoji="🔐", description="Container"),
                discord.SelectOption(label="Music", emoji="🎵", description="A set of music"),
                discord.SelectOption(label="Knife", emoji="🔪", description="Knife"),
                discord.SelectOption(label="Gloves", emoji="🧤", description="Gloves"),
                discord.SelectOption(label="Label", emoji="🔖", description="Label"),
                discord.SelectOption(label="Pass", emoji="📃", description="Pass"),
                discord.SelectOption(label="Souvenir", emoji="🎁", description="Souvenir")
            ])

        selectItemTypeObject = SelectItemType(selectItemType=self.__selectItemType, client=self.__client, ctx=self.__ctx)
        self.__selectItemType.callback = selectItemTypeObject.selectItemType_callback
        createFormView.add_item(self.__selectItemType)

        await interaction.response.send_message(content="Choose a item type, that you want to sell:", view=createFormView)
