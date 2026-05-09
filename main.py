import discord 
from discord.ext import commands 
# Traer desde model_utils la función get_class
from model_utils import get_class 

MODEL_PATH = "keras_model.h5"
LABELS_PATH = "labels.txt"

intents = discord.Intents.default()
intents.message_content = True 

bot = commands.Bot(command_prefix="$", intents = intents)

@bot.event
async def on_ready():
    print(f"Bot conenctado como {bot.user}")

# $hola
@bot.command()
async def hola(ctx):
    await ctx.send("Hola, como estás??")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename

            await attachment.save(f"./{file_name}")

        try:
            class_name, confidence = get_class(
                MODEL_PATH,
                LABELS_PATH,
                file_name
            )

            if confidence < 0.6:
                await ctx.send("No estoy seguro, lo siento")
            else:
                await ctx.send(
                    f"Creo que es: {class_name} \nCon una confianza del: {confidence:.2f}"
                )

        except Exception as e:
            await ctx.send("Hubo un error procesando la imagen")
            print(e)

    else:
        await ctx.send("Olvidaste la imagen")


bot.run("Put your token here!!")