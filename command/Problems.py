from discord.ext import commands
import discord
import requests
import json
import random

class Problems(commands.Cog):
    TAGS = (
        "2-sat", "binary search", "bitmasks", 
        "brute force", "chinese remainder theorem", "combinatorics", 
        "constructive algorithms", "data structures", "dfs and similar",
        "divide and conquer", "dp", "dsu", "expression parsing", "fft", 
        "flows", "games", "geometry", "graph matchings", "graphs", "greedy",
        "hashing", "implementation", "interactive", "math", "matrices",
        "meet-in-the-middle", "number theory", "probabilities","schedules", 
        "shortest paths", "sortings", "string suffix structures", "strings",
        "ternary search", "trees", "two pointers"
    )
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief="random a problem with tag and difficult", description="h32>>random <tag> <operator> <difficult>")
    async def random(self, ctx, tag, operator, difficult: int):
        # print(type(tag))
        tags = tag.split(";")
        new_tags = []
        for tag in tags:
            try:
                tag = int(tag)
                tag = self.TAGS[tag]
                
            except:
                pass
            new_tags.append(tag)
            
        tags = ";".join(new_tags)
        response = requests.get(f"https://codeforces.com/api/problemset.problems?tags={tags}")
        data = response.json()["result"]["problems"]
        data_filtered = []
        for i in data:
            if "rating" in i.keys():
                if operator == "<" and i["rating"] < difficult:
                    data_filtered.append(i)
                if operator == ">" and i["rating"] > difficult:
                    data_filtered.append(i)
                if operator == "<=" and i["rating"] <= difficult:
                    data_filtered.append(i)
                if operator == ">=" and i["rating"] >= difficult:
                    data_filtered.append(i)

        print(len(data_filtered))

        if len(data_filtered) == 0:
            await ctx.send("Không có kết quả")
            return

        problem = random.choice(data_filtered)
        
        # print(problem)
        title = f"Problem {problem['contestId']}{problem['index']}: {problem['name']}"
        url = f"https://codeforces.com/problemset/problem/{problem['contestId']}/{problem['index']}"
        
        # embed
        embed = discord.Embed(title = title, description=tags, url = url, color=0x198BCC)
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/ZD64VJDF_Jer28fVXPzWceg3WKvNlcuEBTstZS6moM4/https/codeforces.org/s/62839/images/codeforces-telegram-square.png?width=80&height=80")
        await ctx.send(embed=embed)
        
    @commands.command(brief="get all tags")
    async def cf_get_tags(self, ctx):
        description = ""
        i = 0
        for item in self.TAGS:
            description += str(i)+". "+item+"\n"
            i += 1
        embed = discord.Embed(title="Codeforce Tags:\n", description=description)
        await ctx.send(embed=embed)

    
def setup(bot):
    bot.add_cog(Problems(bot))