from discord.ext import commands
import random
from discordDir.modules.helpers import *

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


class Game:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.game_over = False

    def make_a_guess(self, guess):
        if guess == self.number_to_guess:
            self.game_over = True
            return "Congratulations! You've guessed the number!"
        elif guess < self.number_to_guess:
            return "Too low!"
        else:
            return "Too high!"


game = Game()


@bot.command()
async def guess(ctx, number: int):
    if game.game_over:
        await ctx.send("The game is over! Please start a new game.")
    else:
        result = game.make_a_guess(number)
        await ctx.send(result)


@bot.command()
async def new_game(ctx):
    global game
    game = Game()
    await ctx.send("A new game has been started!")


# 定义一个名为 "hello" 的命令
@bot.command()
async def hello(ctx):
    print("AAA")
    await ctx.send("Hello, world!")


@bot.event
async def on_message(message):
    # 如果 bot 自己发送的消息，忽略
    if message.author == bot.user:
        return

    # 检查 bot 是否被提及
    if bot.user in message.mentions:
        await message.channel.send(f"Hello {message.author.mention}, you mentioned me.")

    # 必须添加这一行，否则覆盖了原有的命令系统
    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(TOKEN)
