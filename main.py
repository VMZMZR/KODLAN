import discord
from bot_logic import gen_pass  
from bot_logic import flip_coin  
# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi Friend!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\Bye My Friend")
    else:
        await message.channel.send("Tu contraseña es:" + gen_pass(10))
    if message.content.startswith("$flip"):
        await message.channel.send("salio:" + flip_coin())

client.run("MTI0MDExMjgwMjQ0NjgzOTg3OA.GoKG3M.MM5N7JZ0IIW7XwSjzJ_UjvH_8JLaK8UhY7ALh4")
