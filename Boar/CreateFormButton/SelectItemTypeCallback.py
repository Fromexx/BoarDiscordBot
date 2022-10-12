from discord.ui import View, Select
import discord

from Enum import ItemType

import CreateFormButton.NewForm
from CreateFormButton.AskForSkinNameAndPrice import AskForSkinNameAndPrice

class SelectItemType():
    def __init__(self, selectItemType: Select, client: discord.Client, ctx):
        self.__client = client
        self.__ctx = ctx
        self.__selectItemType = selectItemType

    async def selectItemType_callback(self, interaction):
        choiseItemType = self.__selectItemType.values[0]

        if(choiseItemType == ItemType.Weapon.name):
            CreateFormButton.NewForm.write_new_form_value(choiseItemType)
            choiseWeaponTypeView = View()

            selectWeaponType = Select(
            placeholder="Select a weapon type!",
            options=
            [
                discord.SelectOption(label="Pistol", emoji="🔫", description=""),
                discord.SelectOption(label="Shotgun", emoji="🔫", description=""),
                discord.SelectOption(label="MachineGun", emoji="🔫", description=""),
                discord.SelectOption(label="Submachine gun", emoji="🔫", description=""),
                discord.SelectOption(label="Rifle", emoji="🔫", description=""),
                discord.SelectOption(label="SniperRifle", emoji="🔫", description="")
            ])

            #self.__selectWeaponType.callback = 
            choiseWeaponTypeView.add_item(selectWeaponType)

            await interaction.response.send_message(content="Choise weapon type:", view=choiseWeaponTypeView)

            return

        elif(choiseItemType == ItemType.Knife.name):
            CreateFormButton.NewForm.write_new_form_value(choiseItemType)
            choiseKnifeView = View()

            selectKnife = Select(
            placeholder="Select a knife!",
            options=
            [
                discord.SelectOption(label="Bayonet", emoji="🔪", description=""),
                discord.SelectOption(label="Folding", emoji="🔪", description=""),
                discord.SelectOption(label="Knife with hook blade", emoji="🔪", description=""),
                discord.SelectOption(label="Kerambit", emoji="🔪", description=""),
                discord.SelectOption(label="Bayonet M9", emoji="🔪", description=""),
                discord.SelectOption(label="Hunting", emoji="🔪", description=""),
                discord.SelectOption(label="Butterfly", emoji="🔪", description=""),
                discord.SelectOption(label="Falchion", emoji="🔪", description=""),
                discord.SelectOption(label="Butt", emoji="🔪", description=""),
                discord.SelectOption(label="Bowie`s", emoji="🔪", description=""),
                discord.SelectOption(label="Navaja", emoji="🔪", description=""),
                discord.SelectOption(label="Stiletto", emoji="🔪", description=""),
                discord.SelectOption(label="Claw", emoji="🔪", description=""),
                discord.SelectOption(label="Bear", emoji="🔪", description=""),
                discord.SelectOption(label="Classic", emoji="🔪", description=""),
                discord.SelectOption(label="Paracord", emoji="🔪", description=""),
                discord.SelectOption(label="Survival", emoji="🔪", description=""),
                discord.SelectOption(label="Skeleton", emoji="🔪", description=""),
                discord.SelectOption(label="Tramp", emoji="🔪", description="")
            ])
            askForSkinNameAndPriceObject = AskForSkinNameAndPrice(selectKnife, self.__client, self.__ctx)
            selectKnife.callback = askForSkinNameAndPriceObject.ask_for_price_and_skinName
            choiseKnifeView.add_item(selectKnife)

            await interaction.response.send_message(content="Choise knife:", view=choiseKnifeView)

            return

        askForSkinNameAndPriceObject = AskForSkinNameAndPrice(self.__selectItemType, self.__client, self.__ctx)
        await askForSkinNameAndPriceObject.ask_for_price_and_skinName(interaction)
