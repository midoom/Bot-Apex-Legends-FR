import discord
from discord.ext import commands
import random
import requests

discordBotToken = "ENTRER LE TOKEN DU BOT" #Lisez "LisezMoi.md" pour plus d'informations pour obtenir le token 
trnApiKey= "ENTRER LA CLE API DE APEX TRACKER" #Lisez "LisezMoi.md" pour plus d'informations pour obtenir la clé API 
getLevel = "https://public-api.tracker.gg/apex/v1/standard/profile/" 
getLevelFromAzure = "https://apextrack.azurewebsites.net/api/apex/getUserByName?search="


client = commands.Bot(command_prefix = '?')

#Créer des rôles de niveau de 10 à 10 (ex: Niveau 0-10; Niveau 10-20;...; Niveau 90-100)
def getLevelRoleName(level):
    if (level>=0 and level <10):
        return "0-10"
    elif (level>=10 and level <20):
        return "10-20"
    elif (level>=20 and level <30):
        return "20-30"
    elif (level>=30 and level <40):
        return "30-40"
    elif (level>=40 and level <50):
        return "40-50"
    elif (level>=50 and level <60):
        return "50-60"
    elif (level>=60 and level <70):
        return "60-70"
    elif (level>=70 and level <80):
        return "70-80"
    elif (level>=80 and level <90):
        return "80-90"
    elif (level>=90 and level <100):
        return "90-100"
    elif (level>=100):
        return "Lenda"


def getRoleToAdd(roleName,roles):
    for role in roles:
        if roleName in role.name:
            return role

def getRolesToRemove(roles):
    rolesToRemove = []
    for role in roles:
        if ("-" in role.name):
            rolesToRemove.append(role)
    return rolesToRemove

def getPlatformId(platform):
    if(platform == "pc" or platform == "PC"):
        return 5
    elif (platform == "xbox" or platform == "XBOX"):
        return 1
    elif (platform == "ps4" or platform == "PS4"):
        return 2


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(pass_context = True)
async def lvl(ctx, platform,nickname):
    if ctx.message.channel.name == "Entrer le nom du channel": #Le bot peut faire éxécuter cette commande uniqument sur un seul channel, supprimez cette commande pour que la commande s'éxécute sur tout vos channels
        platformID = getPlatformId(platform)
        await client.reply("Cherche le niveau de {}" .format(nickname))
        headers = {
        "TRN-Api-Key": trnApiKey
        }

        request = requests.get("{}{}/{}".format(getLevel,platformID,nickname),headers=headers)
        json = request.json()
        #Cette commande est basé sur l'auto-role du niveau si vous n'en voulez supprimer ce bloc de commande
        if "data" in json:
            level = int(json["data"]["stats"][0]["value"])
            await client.reply("Vous êtes au niveau {}, votre grade à bien été assigné.".format(level))
            roles = ctx.message.server.roles 
            memberRoles = ctx.message.author.roles 
            rolesToRemove = getRolesToRemove(memberRoles) 
            await client.remove_roles(ctx.message.author, *rolesToRemove) 
            roleName = getLevelRoleName(level) 
            role = getRoleToAdd(roleName, roles) 
            await client.add_roles(ctx.message.author,role) 

        elif "errors" in json:
            await client.say(json["errors"][0]["message"])
        else:
            await client.say(json["error"])
    else:
        await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def clvl(ctx, platform, nickname):
    if ctx.message.channel.name == "vos-level": #Le bot peut faire éxécuter cette commande uniqument sur un seul channel, supprimez cette commande pour que la commande s'éxécute sur tout vos channels
        platformID = getPlatformId(platform)
        await client.reply("Recherche du level de {}".format(nickname))
        headers = {
        "TRN-Api-Key": trnApiKey
        }

        request = requests.get("{}{}/{}".format(getLevel,platformID,nickname),headers=headers)
        json = request.json()
        if "data" in json:
            level = int(json["data"]["stats"][0]["value"])
            await client.reply("{} est le niveau de {}.".format(level,nickname))
        elif "errors" in json:
            await client.reply(json["errors"][0]["message"])
        else:
            await client.reply(json["error"])
    else:
        await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def kills(ctx, platform, nickname):
    if ctx.message.channel.name == "vos-level": #Le bot peut faire éxécuter cette commande uniqument sur un seul channel, supprimez cette commande pour que la commande s'éxécute sur tout vos channels
        platformID = getPlatformId(platform)
        await client.reply("Recherche des kills de {}.".format(nickname))
        headers = {
        "TRN-Api-Key": trnApiKey
        }

        request = requests.get("{}{}/{}".format(getLevel,platformID,nickname),headers=headers)
        json = request.json()
        if "data" in json:
            kills = int(json["data"]["stats"][1]["value"])
            await client.reply("{} à tué {} personnes.".format(nickname,kills))
        elif "errors" in json:
            await client.reply(json["errors"][0]["message"])
        else:
            await client.reply(json["error"])
    else:
        await client.delete_message(ctx.message)
        
#Vous pouvez modifier les réponses pour le help mais ne changez pas le "ajuda"
@client.command(pass_context = True)
async def ajuda(ctx):
    embed = discord.Embed(
        title = "Aide",
        description = "Plateforme supporté : PC, PS4, XBOX",
        colour = discord.Colour.red()
    )
    embed.add_field(name = "?lvl", value = '"?lvl (plateforme) (pseudo)" Recherche votre niveau et vous alloue un grade.',inline = False)
    embed.add_field(name = "Exemple:", value = "?lvl PC LLinoor",inline = False)
    embed.add_field(name = "?clvl", value = '"?clvl (plateforme) (pseudo") Recherche votre niveau.',inline = False)
    embed.add_field(name = "Exemple:", value = "?clvl PC LLinoor",inline = False)
    embed.add_field(name = "?kills", value = '"?kills (plateforme) (pseudo)" Recherche vos kills.',inline = False)
    embed.add_field(name = "Exemple:", value = "?kills PC LLinoor.",inline = False)
    embed.set_footer(text = "Bonne game !")

    # msg = '{0.mention}, {1}'.format(ctx.message.author, "teste")
    # await client.send_message(ctx.message.channel, msg)

    await client.say(embed = embed)


client.run(discordBotToken)

#API Tracker by https://apex.tracker.gg/site-api
#Code source by https://github.com/AdautoP
#Enjoy :)
