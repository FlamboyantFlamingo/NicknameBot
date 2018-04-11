import discord,asyncio
client = discord.Client()

global Token
Token = open("BotToken.txt", "r")

@client.event
async def on_ready():
    print('NicknameBot has started!')
    print('Programmed by Flamboyant Flamingo')
    print('tinyurl.com/flamingoYT')
    await client.change_presence(game=discord.Game(name='!credits'))

@client.event
async def on_message(message):
  
    if message.content.startswith('!credits'):
        await client.send_message(message.author, 'Programmed by Flamboyant Flamingo')
        await client.send_message(message.author, 'https://tinyurl.com/flamingoYT')

    if message.content.startswith('!nickall'):
        for role in message.author.roles:
            if ('administrator', True) in role.permissions:
                nickname = str(message.content).split(' ')
                for user in client.get_all_members():
                    try:
                        await client.change_nickname(user, nickname[1])
                    except:
                        print('User '+str(user)+' was skipped')

    if message.content.startswith('!unnickall'):
        for role in message.author.roles:
            if ('administrator', True) in role.permissions:
                for user in client.get_all_members():
                    try:
                        await client.change_nickname(user, None)
                    except:
                        print('User '+str(user)+' was skipped')

client.run(str(Token.read()))
