from discord.ui import Select
import discord

import CreateFormButton.NewForm
from UserForms import UserForms

class AskForSkinNameAndPrice():
    def __init__(self, selectedItemType: Select, client: discord.Client, ctx):
        self.__selectedItemType = selectedItemType
        self.__client = client
        self.__ctx = ctx
    
    async def ask_for_price_and_skinName(self, interaction):
        CreateFormButton.NewForm.write_new_form_value(self.__selectedItemType.values[0])

        await interaction.response.send_message(content="Write knfie name:")

        knifeNameMessage = await self.__client.wait_for('message', check=self.check(self.__ctx.author), timeout=30)
        CreateFormButton.NewForm.write_new_form_value(knifeNameMessage.content)

        await self.__ctx.send(content="Write knfie price:")
        knifePriceMessage = await self.__client.wait_for('message', check=self.check(self.__ctx.author), timeout=30)
        print(knifePriceMessage.content)

        CreateFormButton.NewForm.write_new_form_value(knifePriceMessage.content)
        CreateFormButton.NewForm.write_new_form_value(f"User: {self.__ctx.author.id}")

        UserForms().write_form_on_file(form=CreateFormButton.NewForm.newForm)

    def check(self, author):
        def inner_check(message):
            return True
        return inner_check
