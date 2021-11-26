from discord.ext import commands
import discord
import asyncio
import os
import random
import json
import re
from datetime import datetime
from connectDB.connectDB import database
from connectDB import table

class PoTD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief="add problems to potd")
    async def potd(self, ctx, handle: str):
        if database.update_handle(str(ctx.author), handle):
            await ctx.send("Thiết lập handle codeforces thành công")
            return
        else:
            await ctx.send("Không thể thay đổi handle codeforces")
            return

        
    
def setup(bot):
    bot.add_cog(PoTD(bot))