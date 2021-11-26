from discord.ext import commands
import requests
from connectDB.connectDB import database
from connectDB import table
from method.cf_submissions import Cf_submissions

class Handle(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief="insert or update handle codeforces")
    async def handle(self, ctx, handle: str):
        if database.update_handle(str(ctx.author), handle):
            await ctx.send("Thiết lập handle codeforces thành công")
            return
        else:
            await ctx.send("Không thể thay đổi handle codeforces")
            return

    # @commands.command(brief="visualize")
    # async def get_handle(self, ctx):
    #     print(str(ctx.author))
    #     res =  database.get_handle(str(ctx.author))
    #     await ctx.send(res)
    #     return
        

    # @commands.command(brief="visualize")
    # async def cf_vs(self, ctx, handle: str):
    #     response = requests.get(f"https://codeforces.com/api/user.status?handle={handle}")
    #     data = response.json()["result"]
    #     cf_submissions = Cf_submissions(data)
    #     ratio = cf_submissions.getRatioTags()
    #     link = cf_submissions.visualizeRatioTags(ratio)
    #     print(link)


    
def setup(bot):
    bot.add_cog(Handle(bot))