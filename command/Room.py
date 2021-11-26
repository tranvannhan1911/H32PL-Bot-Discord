from discord.ext import commands
import discord
import asyncio
import os
import random
import json
import re



class Room(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief="add private room")
    async def add_icpc(self, ctx, *member):
        print(member, member[0][3:-1])
        # user = self.bot.get_user("3766")
        # print(user)
        print(self.bot.guilds[0].get_member(member[0][3:-1]))
        # print(self.bot.guilds[0].members)
        print(self.bot.guilds)
        # print(self.bot.guilds)
        
    
def setup(bot):
    bot.add_cog(Room(bot))