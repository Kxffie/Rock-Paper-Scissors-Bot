import nextcord
from nextcord.ext import commands
import random

intents = nextcord.Intents.all()
client = commands.Bot(command_prefix="rps!", intents=intents)

@client.event
async def on_ready():
    print(f'-----\nLogged in as: {client.user}\n-----')

@client.command()
async def play(ctx, choice):
    userChoice = choice.lower()
    choices = ["rock", "paper", "scissors"]
    hands = {'rock_scissors': "Rock smashes scissors, you win!",
            'paper_rock':"Paper covers rock, you win.",
            'scissors_paper':"Scissors cuts paper, you win!",
            'rock_paper': "Rock smashes scissors, you win!",
            'paper_scissors': "Paper covers rock, you lose.",
            'scissors_rock': "Rock smashes scissors, you lose.",
            'paper_paper': "It's a tie",
            'rock_rock': "It's a tie",
            'scissors_scissors': "It's a tie"
            }
    if userChoice in choices:
        computerChoice = random.choice(choices)
        await ctx.send(hands[f'{userChoice}_{computerChoice}'])
    else:
        await ctx.send(f"Invalid choice '{userChoice}'")

client.run("PUT YOUR TOKEN HERE")
