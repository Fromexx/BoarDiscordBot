from discord.ui import View, Select
import discord

from Enum import WeaponType

import CreateFormButton.NewForm
from CreateFormButton.AskForSkinNameAndPrice import AskForSkinNameAndPrice


class SelectWeapon():
    def __init__(self, selectWeaponType: Select):
        self.__selectWeaponType = selectWeaponType

    async def selectWeapon_callback(self, interaction):
        selectedWeaponType = self.__selectWeaponType.values[0]
        CreateFormButton.NewForm.write_new_form_value(selectedWeaponType)

        if(selectedWeaponType == WeaponType.Pistol):
            choisePistolView = View()

            selectPistol = Select(
            placeholder="Select a weapon!",
            options=
            [
                discord.SelectOption(label="P2000", emoji="🔫", description=""),
                discord.SelectOption(label="Glock-18", emoji="🔫", description=""),
                discord.SelectOption(label="USP-S", emoji="🔫", description=""),
                discord.SelectOption(label="Dual Berettas", emoji="🔫", description=""),
                discord.SelectOption(label="P250", emoji="🔫", description=""),
                discord.SelectOption(label="Five-SeveN", emoji="🔫", description=""),
                discord.SelectOption(label="Tec-9", emoji="🔫", description=""),
                discord.SelectOption(label="CZ75-Auto", emoji="🔫", description=""),
                discord.SelectOption(label="Desert Eagle", emoji="🔫", description=""),
                discord.SelectOption(label="Revolver R8", emoji="🔫", description="")
            ])

            askForSkinNameAndPriceObject = AskForSkinNameAndPrice(selectPistol, self.__client, self.__ctx)
            selectPistol.callback = askForSkinNameAndPriceObject.ask_for_price_and_skinName
            choisePistolView.add_item(selectPistol)

            await interaction.response.send_message(content="Choise weapon:", view=choisePistolView)

        elif(selectedWeaponType == WeaponType.Shotgun):
            choiseShotgunView = View()

            selectShotgun = Select(
            placeholder="Select a weapon!",
            options=
            [
                discord.SelectOption(label="Nova", emoji="🔫", description=""),
                discord.SelectOption(label="XM1014", emoji="🔫", description=""),
                discord.SelectOption(label="MAG-7", emoji="🔫", description=""),
                discord.SelectOption(label="Saved-Off", emoji="🔫", description="")
            ])

            askForSkinNameAndPriceObject = AskForSkinNameAndPrice(selectShotgun, self.__client, self.__ctx)
            selectShotgun.callback = askForSkinNameAndPriceObject.ask_for_price_and_skinName
            choiseShotgunView.add_item(selectShotgun)

            await interaction.response.send_message(content="Choise weapon:", view=choiseShotgunView)
