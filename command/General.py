from discord.ext import commands
import discord
from datetime import datetime
import imgkit
from yattag import Doc
# import wkhtmltopdf 

doc, tag, text, line = Doc().ttl()

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # @commands.command(brief="help")
    # async def help(self, ctx):
    #     with tag("html"):
    #         with tag("body"):
    #             with tag('ul', id='grocery-list'):
    #                 line('li', 'Tomato sauce', klass="priority")
    #                 line('li', 'Salt')
    #                 line('li', 'Pepper')
    #     # html_file = open("template/help.html", "w")
    #     # html_file.write(doc.getvalue())
    #     # html_file.close()
    #     imgkit.from_string(doc.getvalue(), 'template/out.jpg')
    #     await ctx.send(doc.getvalue())
    #     return


def setup(bot):
    bot.add_cog(General(bot))