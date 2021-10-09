import discord
from discord.ext import commands
 
TOKEN = "ODk2MDIyNDM5ODU3OTA5NzYx.YWBD7A.2_hY34ORN2JgJHlR2GdnQpjST60"

client = commands.Bot(command_prefix=".")

intents = discord.Intents.default()
intents.members = True





@client.event
async def on_ready():
    print('bot ready')
    
    
    


#store 
@client.command()
async def Store(ctx):
    embed=discord.Embed(title="***Store***", description="*dsg minecrft Store*", color=0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/webstore/logos/aa2416c9358d767b4d37328418284816c8456537.png")
    embed.add_field(name="Ranks", value="Buy for ranks do *.Ranks*", inline=False)
    embed.add_field(name="Spawners", value="Buy for Spawners do *.Spawners*", inline=False)
    embed.add_field(name="Money", value="Buy for inagem money do *.Money*", inline=False)
    embed.add_field(name="Eggs", value="Buy for minecraft eggs do *.Eggs*", inline=False)
    embed.add_field(name="Commands", value="Buy for commands  do *.Commands*", inline=False)
    embed.add_field(name=" info ",  value="enter ther .(you command)", inline=False)
    await ctx.send(embed=embed)
 
#StoreHelp #Icon = https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.freepik.com%2Ffree-icon%2Fhelp-circled_318-10762.jpg&f=1&nofb=1
@client.command()
async def StoreHelp(ctx):
    embed=discord.Embed(title="***StoreHelp***", description="*Store for Help*", color=0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimage.freepik.com%2Ffree-icon%2Fhelp-circled_318-10762.jpg&f=1&nofb=1")
    embed.add_field(name="**.Store**", value="open Store ", inline=False)
    embed.add_field(name="**.Rank**", value="Open Rank Store", inline=False)
    embed.add_field(name="**.Spawners**", value="Open Spawners Store", inline=False)
    embed.add_field(name="**.Money**", value="Open ingame money Store", inline=False)
    embed.add_field(name="**.Eggs**", value="Open game Eggs Store", inline=False)
    embed.add_field(name="**.Commands**",  value="open Game Valid Command buy Store", inline=False)
    embed.add_field(name="**.Rank_(Ranks name)**",  value="Viwe Rank", inline=False)
    embed.add_field(name="**.Buy_(Rank name)**",  value="Buy and gift Rank", inline=False)
    embed.add_field(name="**.Buy_(Spawner name)**",  value="Buy and gift spawners", inline=False)
    embed.add_field(name="**.Buy_(Money package Name )**",  value="Buy and gift inagme money", inline=False)
    embed.add_field(name="**.Buy_(Egg name )**",  value="Buy and gift eggs", inline=False)
    embed.add_field(name="**.Buy_(Command name )**",  value="Buy and gift commands", inline=False)
    
    await ctx.send(embed=embed)

 
#Ranks    
@client.command()           #https://dunb17ur4ymx4.cloudfront.net/webstore/logos/aa2416c9358d767b4d37328418284816c8456537.png
async def Ranks(ctx):
    embed=discord.Embed(title="***Store***", description="*dsg minecrft  Ranks Store*", color=0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fi.imgur.com%2FRWxoASF.jpg&f=1&nofb=1")
    embed.add_field(name="VIP       1.60 USD", value="Vip Rank  **1.60 USD**", inline=False)
    embed.add_field(name="PRIME Rank        2.60 USD", value="Prime Rank   ** 2.60 USD**", inline=False)
    embed.add_field(name="PRIME+ Rank       4.00 USD", value="Prime+ Rank   **4.00 USD**", inline=False)
    embed.add_field(name="PREMIUM Rank      6.00 USD", value="premium Rank   **6.00 USD**", inline=False)
    embed.add_field(name="LORD Rank     9.00 USD", value="lord Rank  **9.00 USD**", inline=False)
    embed.add_field(name="TITAN RANK       15.00 USD", value="titen rank   **15.00 USD**", inline=False)
    embed.add_field(name=" info ",  value="enter ther .Rank_(Rankname)", inline=False)
    await ctx.send(embed=embed)


#ranks vip  

@client.command() 
async def Rank_Vip(ctx):
    embed=discord.Embed(title="***VIP Rank***", description="*VIP Rank   1.60 USD, (1 Month Valid)*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/5f2060ddef301374fc4cc3e5721754f96ab13b26.png")
    embed.add_field(name="Items", value = " `1500 claim blocks`. `3500 ingame money`. `Homes - 2 (/sethome <name>)`" ,inline=False)
    embed.add_field(name="***available commands***", value = " `-------------------`" ,inline=False)
    embed.add_field(name="/kits VIP", value = " **1.** `diamond helemt with unbraking 2 protection 2  ` **2.** `diamond chestplate with unbraking 2 protection 2  ` **3.** `diamond leggings with unbraking 2 protection 2` **4.** `diamond boots with unbraking 2 protection 2 ` **5.** `diamond sword with unbraking 2 sharpness 1` **6.** `diamond pickaxe with unbraking 2 efficiency 1` **7.** ` diamond helmet with unbraking 2 efficiency 1`  **8.** ` enchanted golden apple 5`  (kit available in every 7 days) " ,inline=False)
    embed.add_field(name="/heal", value = " `You can heal any time without food`" ,inline=False)
    embed.add_field(name="/feed   ", value = " `restore your whole hunger bar`" ,inline=False)
    embed.add_field(name="/workbench", value = " `a portable crafting table you can use any time`" ,inline=False)
    await ctx.send(embed=embed)
    
    #ranks   PRIME Rank

@client.command() 
async def Rank_Prime(ctx):
    embed=discord.Embed(title="***Prime Rank***", description="*Prime Rank   2.60 USD, (1 Month Valid)*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/72d90ff70c9d332b6a909385064ac5794676a2de.png")
    embed.add_field(name="Items", value = " `2500 claim blocks`. `5000 ingame money`. `Homes - 3 (/sethome <name>)` .`one Player warp`" ,inline=False)
    embed.add_field(name="***available commands***", value = " `-------------------`" ,inline=False)
    embed.add_field(name="/kits  prime", value = " **1.** `diamond helemt with unbraking 2 protection 2  ` **2.** `diamond chestplate with unbraking 2 protection 2  ` **3.** `diamond leggings with unbraking 2 protection 2` **4.** `diamond boots with unbraking 2 protection 2 ` **5.** `diamond sword with unbraking 2 sharpness 1` **6.** `diamond pickaxe with unbraking 2 efficiency 1` **7.** ` diamond helmet with unbraking 2 efficiency 1`  **8.** ` enchanted golden apple 10 `  (kit available in every 7 days) " ,inline=False)
    embed.add_field(name="/heal", value = " `You can heal any time without food`" ,inline=False)
    embed.add_field(name="/ec", value = " `can open ender chest anytime without crafting it`" ,inline=False)
    embed.add_field(name="/feed   ", value = " `restore your whole hunger bar`" ,inline=False)
    embed.add_field(name="/workbench", value = " `a portable crafting table you can use any time`" ,inline=False)
    await ctx.send(embed=embed)
    
    
        #ranks   PRIME+ Rank

@client.command() 
async def Rank_Prime_Plus (ctx):
    embed=discord.Embed(title="***Prime+ Rank***", description="*Prime+ Rank   4.00 USD, (1 Month Valid)*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/72d90ff70c9d332b6a909385064ac5794676a2de.png")
    embed.add_field(name="Items", value = " `5000 claim blocks`. `7000 ingame money`. `Homes - 4 (/sethome <name>)` .`one Player warp`" ,inline=False)
    embed.add_field(name="***available commands***", value = " `-------------------`" ,inline=False)
    embed.add_field(name="/kits  primeplus", value = " **1.** `diamond helemt with unbraking 2 protection 2 projectile protection 2` **2.** `diamond chestplate with unbraking 2 protection 2 projectile protection 2` **3.** `diamond leggings with unbraking 2 protection 2 blast protection 2` **4.** `diamond boots with unbraking 2 protection 2 fether falling 2` **5.** `diamond sword with unbraking 2 sharpness 2 looting 2` **6.** `diamond pickaxe with unbraking 2 efficiency 2` **7.** ` diamond helmet with unbraking 2 efficiency 2 fire protection 2`  **8.** `Enchanted Bow with unbraking 2 infinity `  **9.** `enchanted golden apple 10 ` (kit available in every 7 days) " ,inline=False)
    embed.add_field(name="/fly", value = " `you can fly`" ,inline=False)
    embed.add_field(name="/skull", value = " `you can get player heads`" ,inline=False)
    embed.add_field(name="/disposal   ", value = " `a nother backup like enderchest`" ,inline=False)
    embed.add_field(name="/fireball", value = " `you can throw fireballs without making it`" ,inline=False)
    embed.add_field(name="/firewrks", value = " `allow you to modify a stack of fireworks`" ,inline=False)
    await ctx.send(embed=embed)       

    #ranks   PREMIUM Rank

@client.command() 
async def Rank_Premium(ctx):
    embed=discord.Embed(title="***Premium Rank***", description="*Premium  Rank   6.00 USD, (1 Month Valid)*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/c4b9da4a3cd3fa151244787116187cb61045d2e0.png")
    embed.add_field(name="Items", value = "`Keeping inventories & XP`  `15000 claim blocks`. `15000 ingame money`. `Homes - 5 (/sethome <name>)`" ,inline=False)
    embed.add_field(name="***available commands***", value = " `-------------------`" ,inline=False)
    embed.add_field(name="/kits  PREMIUM", value = " **1.** `netherite helemt with unbraking 3 protection 3 projectile protection 3 mending` **2.** `netherite chestplate with unbraking 3 protection 3 projectile protection 3 mending` **3.** `netherite leggings with unbraking 3 protection 3 blast protection 3 mending` **4.** `netherite boots with unbraking 3 protection 3 fether falling 3 mending` **5.** `netherite sword with unbraking 3 sharpness 3 looting 3 mending` **6.** `netherite pickaxe with unbraking 3 efficiency 3 mending` **7.** `netherite helmet with unbraking 3 efficiency 3 fire protection 3 mending`  **8.** `Enchanted Bow with unbraking 3 infinity mending`  **9.** `5 block of netherite` **10.** `enchanted golden apple 10` (kit available in every 14 days) " ,inline=False)
    embed.add_field(name="/heal", value = " `You can heal any time without food`" ,inline=False)
    embed.add_field(name="/ec", value = " `can open ender chest anytime without crafting it`" ,inline=False)
    embed.add_field(name="/feed   ", value = " `restore your whole hunger bar`" ,inline=False)
    embed.add_field(name="/workbench", value = " `a portable crafting table you can use any time`" ,inline=False)
    embed.add_field(name="/fly", value = " `you can fly`" ,inline=False)
    embed.add_field(name="/skull", value = " `you can get player heads`" ,inline=False)
    embed.add_field(name="/disposal   ", value = " `a nother backup like enderchest`" ,inline=False)
    embed.add_field(name="/fireball", value = " `you can throw fireballs without making it`" ,inline=False)
    embed.add_field(name="/firewrks", value = " `allow you to modify a stack of fireworks`" ,inline=False)
    embed.add_field(name="/compass", value = " `compass without crafting`" ,inline=False)
    embed.add_field(name="/jump ", value = " `high jump`" ,inline=False)
    embed.add_field(name="/near ", value = " `find near by players`" ,inline=False)
    await ctx.send(embed=embed)
    
    
#LORD Rank
@client.command() 
async def Rank_Lord(ctx):
    embed=discord.Embed(title="***LORD  Rank***", description="*LORD   Rank   6.00 USD, (2 Month Valid)*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/87d5dc051eb22fc69e527467765ffb59633349b6.png")
    embed.add_field(name="Items", value = "`Keeping inventories & XP`  `15000 claim blocks`. `15000 ingame money`. `Homes - 8 (/sethome <name>)`" ,inline=False)
    embed.add_field(name="***available commands***", value = " `-------------------`" ,inline=False)
    embed.add_field(name="/kits  LORD ", value = " **1.** `solbound netherite helemt with unbraking 3 protection 3 projectile protection 3 mending` **2.** `solbound netherite chestplate with unbraking 3 protection 3 projectile protection 3 mending` **3.** `solbound netherite leggings with unbraking 3 protection 3 blast protection 3 mending` **4.** `solbound netherite boots with unbraking 3 protection 3 fether falling 3 mending` **5.** `solbound netherite sword with unbraking 3 sharpness 3 looting 3 mending` **6.** `solbound netherite pickaxe with unbraking 3 efficiency 3 mending` **7.** `solbound netherite helmet with unbraking 3 efficiency 3 fire protection 3 mending`  **8.** `solbound Enchanted Bow with unbraking 3 infinity mending`  **9.** `10 block of netherite` **10.** `emerald Block 40`**11.** `enchanted golden apple 10` (kit available in every 14 days) " ,inline=False)
    embed.add_field(name="/tp", value = "`teleport to players without player permissions`" ,inline=False)
    embed.add_field(name="/depth", value = "`you can messure depth`" ,inline=False)
    embed.add_field(name="/god", value = "`god mode`" ,inline=False)
    embed.add_field(name="/heal", value = " `You can heal any time without food`" ,inline=False)
    embed.add_field(name="/ec", value = " `can open ender chest anytime without crafting it`" ,inline=False)
    embed.add_field(name="/feed   ", value = " `restore your whole hunger bar`" ,inline=False)
    embed.add_field(name="/workbench", value = " `a portable crafting table you can use any time`" ,inline=False)
    embed.add_field(name="/fly", value = " `you can fly`" ,inline=False)
    embed.add_field(name="/skull", value = " `you can get player heads`" ,inline=False)
    embed.add_field(name="/disposal   ", value = " `a nother backup like enderchest`" ,inline=False)
    embed.add_field(name="/fireball", value = " `you can throw fireballs without making it`" ,inline=False)
    embed.add_field(name="/firewrks", value = " `allow you to modify a stack of fireworks`" ,inline=False)
    embed.add_field(name="/compass", value = " `compass without crafting`" ,inline=False)
    embed.add_field(name="/jump ", value = " `high jump`" ,inline=False)
    embed.add_field(name="/near ", value = " `find near by players`" ,inline=False)
    await ctx.send(embed=embed)
    
#titan Rank
@client.command() 
async def Rank_Titan(ctx):
    embed=discord.Embed(title="***LORD  Rank***", description="*LORD   Rank   6.00 USD, (2 Month Valid)*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/62343e299da5ad5628887aa0c710e28dc8e599f0.png")
    embed.add_field(name="Items", value = "`Keeping inventories & XP`  `15000 claim blocks`. `15000 ingame money`. `Homes - 10 (/sethome <name>)`" ,inline=False)
    embed.add_field(name="***available commands***", value = " `-------------------`" ,inline=False)
    embed.add_field(name="/kits  Over-Lord ", value = " **1.** `solbound netherite helemt with unbraking 3 protection 3 projectile protection 3 mending` **2.** `solbound netherite chestplate with unbraking 3 protection 3 projectile protection 3 mending` **3.** `solbound netherite leggings with unbraking 3 protection 3 blast protection 3 mending` **4.** `solbound netherite boots with unbraking 3 protection 3 fether falling 3 mending` **5.** `solbound netherite sword with unbraking 3 sharpness 3 looting 3 mending` **6.** `solbound netherite pickaxe with unbraking 3 efficiency 3 mending` **7.** `solbound netherite helmet with unbraking 3 efficiency 3 fire protection 3 mending`  **8.** `solbound Enchanted Bow with unbraking 3 infinity mending`  **9.** `10 block of netherite` **10.** `emerald Block 40`**11.** `enchanted golden apple 10` (kit available in every 14 days) " ,inline=False)
    embed.add_field(name="/setwarp", value = "`you can set warps in server`" ,inline=False)
    embed.add_field(name="/depth", value = "`you can messure depth`" ,inline=False)
    embed.add_field(name="/god", value = "`god mode`" ,inline=False)
    embed.add_field(name="/heal", value = " `You can heal any time without food`" ,inline=False)
    embed.add_field(name="/ec", value = " `can open ender chest anytime without crafting it`" ,inline=False)
    embed.add_field(name="/feed   ", value = " `restore your whole hunger bar`" ,inline=False)
    embed.add_field(name="/workbench", value = " `a portable crafting table you can use any time`" ,inline=False)
    embed.add_field(name="/fly", value = " `you can fly`" ,inline=False)
    embed.add_field(name="/skull", value = " `you can get player heads`" ,inline=False)
    embed.add_field(name="/disposal   ", value = " `a nother backup like enderchest`" ,inline=False)
    embed.add_field(name="/fireball", value = " `you can throw fireballs without making it`" ,inline=False)
    embed.add_field(name="/firewrks", value = " `allow you to modify a stack of fireworks`" ,inline=False)
    embed.add_field(name="/compass", value = " `compass without crafting`" ,inline=False)
    embed.add_field(name="/jump ", value = " `high jump`" ,inline=False)
    embed.add_field(name="/near ", value = " `find near by players`" ,inline=False)
    await ctx.send(embed=embed)
#######################################################Vip gift and buy #####################################
            
                        #Buy Ranks
                               
            
                #Vip buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#god buy    
@client.command() 
async def Buy_Vip(ctx):
    embed=discord.Embed(title="***Vip Rank***", description="Buy and Gift Vip Rank here",url="https://dsg-minecraft-server.tebex.io/package/4678872", color = 0xDAA311)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")
    embed.add_field(name="***Buy and Gift Vip Rank****", value="-https://dsg-minecraft-server.tebex.io/checkout/packages/add/4678872/single", inline=False)
    embed.add_field(name="***Vip Rank[Price : 1.60 USD]****", value="-`Buy and Gift Vip Rank [Price : 1.60 USD]`", inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the rank = https://dsg-minecraft-server.tebex.io/package/4678872")#god buy    
    
#######################################################Prime gift and buy #####################################
 # https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fbuy-now-red-button-website-element-online-shop-icon-shopping-cart-icon-buy-now-red-button-website-element-online-shop-icon-185930834.jpg&f=1&nofb=1           
                        #Buy Ranks
                               
            
                #Prime buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#god buy    
@client.command() 
async def Buy_Prime(ctx):
    embed=discord.Embed(title="***Prime Rank***", description="Buy and Gift Prime Rank here",url="https://dsg-minecraft-server.tebex.io/package/4678883", color = 0xDAA311)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")
    embed.add_field(name="***Buy and Gift Prime Rank****", value="-https://dsg-minecraft-server.tebex.io/package/4678883", inline=False)
    embed.add_field(name="***Prime Rank[Price : 2.60 USD]****", value="-`Buy and Gift Prime Rank [Price :2.60 USD]`", inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the rank = https://dsg-minecraft-server.tebex.io/package/4678883")#god buy    
    

            
                #Vip buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#######################################################/prime gift an buy####################################
#######################################################prime + gift and buy #####################################
            
                        #Buy Ranks
                               
            
                #Prime buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#god buy    
@client.command() 
async def Buy_Prime_Plus(ctx):
    embed=discord.Embed(title="***Prime+ Rank***", description="Buy and Gift Prime+ Rank here",url="https://dsg-minecraft-server.tebex.io/package/4678886", color = 0xDAA311)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")
    embed.add_field(name="***Buy and Gift Prime+ Rank****", value="-https://dsg-minecraft-server.tebex.io/package/4678886", inline=False)
    embed.add_field(name="***Prime+ Rank[Price : 4.00 USD]****", value="-`Buy and Gift Prime+ Rank [Price :4.00 USD]`", inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the rank = https://dsg-minecraft-server.tebex.io/package/4678886")#god buy    
    

            
                #Prime+ buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#######################################################/prime gift an buy###########################################################################################prime + gift and buy #####################################
            
                        #Buy Ranks
                               
            
                #Lord buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#god buy    
@client.command() 
async def Buy_Lord(ctx):
    embed=discord.Embed(title="***Lord Rank***", description="Buy and Gift Lord Rank here",url="https://dsg-minecraft-server.tebex.io/package/4678891", color = 0xDAA311)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")
    embed.add_field(name="***Buy and Gift Prime+ Rank****", value="-https://dsg-minecraft-server.tebex.io/package/4678891", inline=False)
    embed.add_field(name="***Lord Rank[Price : 9.00 USD]****", value="-`Buy and Gift Lord Rank [Price :9.00 USD]`", inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the rank = https://dsg-minecraft-server.tebex.io/package/4678891")#god buy    
    

            
                #lorad buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#######################################################/prime gift an buy####################################                #Prime+ buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#######################################################/Titan gift an buy###########################################################################################prime + gift and buy #####################################
            
                        #Buy Ranks
                               
            
                #titanbuy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#god buy    
@client.command() 
async def Buy_Titan(ctx):
    embed=discord.Embed(title="***Titan Rank***", description="Buy and Gift Titan Rank here",url="https://dsg-minecraft-server.tebex.io/package/4678896", color = 0xDAA311)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")
    embed.add_field(name="***Buy and Gift Titan Rank****", value="-https://dsg-minecraft-server.tebex.io/package/4678896", inline=False)
    embed.add_field(name="***Titan Rank[Price : 15.00 USD]****", value="-`Buy and Gift Titan Rank [15.00 USD]`", inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the rank = https://dsg-minecraft-server.tebex.io/package/4678896")#god buy    
    

            
                #titan buy and gift #Cart icon = https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1
#######################################################/prime gift an buy####################################


#############################################Spawner Buy####################################################
@client.command() 
async def Spawners(ctx):
    embed=discord.Embed(title="***Spawner***", description="*Spawner Store .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="Cow Spawner  2.50 USD ", value = " `Cow spawn Spawner `" ,inline=False)
    embed.add_field(name="Pig Spawner  2.50 USD", value = " `Pig Spawn Spanwer`" ,inline=False)
    embed.add_field(name="Skeleton Spawner   2.50 USD", value = " `Skeleton Spawn Spawner`" ,inline=False)
    embed.add_field(name="Zombie Spawner   2.50 USD", value = " `Zombie Spawn Spawner`" ,inline=False)
    embed.add_field(name="Blaze Spawner    2.50 USD", value = " `Blaz Spawn Spawner`" ,inline=False)
    await ctx.send(embed=embed)

####Spawner_Cow#########    
@client.command() 
async def Spawner_Cow(ctx):
    embed=discord.Embed(title="***Spawner Cow ***", description="*Spawner Cow info and buy*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Cow Spawner 2.50 USD  ", value = " `Cow spawn Spawner `" ,inline=False)
    embed.set_footer(text="You Want Buy Spawner do .Buy_Cow_Spawner")
    await ctx.send(embed=embed)
    
####Spawner_Pig#########    
@client.command() 
async def Spawner_Pig(ctx):
    embed=discord.Embed(title="***Spawner Pig ***", description="*Spawner pig info and buy .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/014787509904f7d4b7e6a17e593a2e8dbaf5c7d4.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="pig  Spawner 2.50 USD  ", value = " `pig  spawn Spawner `" ,inline=False)
    embed.set_footer(text="You Want Buy Spawner do .Buy_Pig_Spawner")
    await ctx.send(embed=embed)  

####Spawner_Skeleton#########    
@client.command() 
async def Spawner_Skeleton(ctx):
    embed=discord.Embed(title="***Spawner Skeleton ***", description="*Spawner Skeleton info and buy .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/bd5aeab379323160f1e00f8b075961430c0ef4e3.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Skeleton Spawner 2.50 USD  ", value = " `Skeleton spawn Spawner `" ,inline=False)
    embed.set_footer(text="You Want Buy Spawner do .Buy_Skeleton_Spawner")
    await ctx.send(embed=embed)  
    
####Spawner_Zombie#########    
@client.command() 
async def Spawner_Zombie(ctx):
    embed=discord.Embed(title="***Spawner Zombie ***", description="*Spawner Zombie info and buy .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/f7b0a22e6fe9446bbf9b055da843471f8ceb3975.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Zombie Spawner 2.50 USD  ", value = " `Zombie spawn Spawner `" ,inline=False)
    embed.set_footer(text="You Want Buy Spawner do .Buy_Zombie_Spawner")
    await ctx.send(embed=embed) 
    
####Spawner_Blaze#########    
@client.command() 
async def Spawner_Blaze(ctx):
    embed=discord.Embed(title="***Spawner Blaze***", description="*Spawner Blaze info and buy .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Blaze Spawner 2.50 USD  ", value = " `Blaze spawn Spawner `" ,inline=False)
    embed.set_footer(text="You Want Buy Spawner do .Buy_Blaz_Spawner")
    await ctx.send(embed=embed)  

#######################Spawners buy and Gift######################################################
####BUy and gift Cow spawner#########    
@client.command() 
async def Buy_Cow_Spawner(ctx):
    embed=discord.Embed(title="***Buy Cow Spawner***", description="*Buy and gift cow Spawnr.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Spawner ", value = " https://dsg-minecraft-server.tebex.io/package/4710355" ,inline=False)
    embed.add_field(name="Cow Spawner 2.50 USD  ", value = " `Cow spawn Spawner `" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Spanwer = https://dsg-minecraft-server.tebex.io/package/4710355")    
    
    ####BUy and gift Pig spawner#########    
@client.command() 
async def Buy_Pig_Spawner(ctx):
    embed=discord.Embed(title="***Buy Pig Spawner***", description="*Buy and gift pig Spawnr.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Spawner ", value = " https://dsg-minecraft-server.tebex.io/package/4710356" ,inline=False)
    embed.add_field(name="Pig Spawner 2.50 USD  ", value = " `Pig spawn Spawner `" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Spanwer = https://dsg-minecraft-server.tebex.io/package/4710356")        
    
    ####BUy and gift Pig spawner#########    
@client.command() 
async def Buy_Skeleton_Spawner(ctx):
    embed=discord.Embed(title="***Buy Skeleton Spawner***", description="*Buy and gift Skeleton Spawnr.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Spawner ", value = " https://dsg-minecraft-server.tebex.io/package/4710358" ,inline=False)
    embed.add_field(name="Skeleton Spawner 2.50 USD  ", value = " `Skeleton spawn Spawner `" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Spanwer = https://dsg-minecraft-server.tebex.io/package/4710358") 
    
    ####BUy and gift Zombie spawner#########    
@client.command() 
async def Buy_Zombie_Spawner(ctx):
    embed=discord.Embed(title="***Buy Zombie Spawner***", description="*Buy and gift Zombie Spawnr.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Spawner ", value = " https://dsg-minecraft-server.tebex.io/package/4710359" ,inline=False)
    embed.add_field(name="Zombie Spawner 2.50 USD  ", value = " `Zombie spawn Spawner `" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Spanwer = https://dsg-minecraft-server.tebex.io/package/4710359")       

    ####BUy and gift Blaze spawner#########    
@client.command() 
async def Buy_Blaze_Spawner(ctx):
    embed=discord.Embed(title="***Buy Blaze Spawner***", description="*Buy and gift Blaze Spawnr.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Spawner ", value = " https://dsg-minecraft-server.tebex.io/package/4710362" ,inline=False)
    embed.add_field(name="Blazee Spawner 2.50 USD  ", value = " `Blaze spawn Spawner `" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Spanwer = https://dsg-minecraft-server.tebex.io/package/4710362")    


###########################eggs#######################################

@client.command() 
async def Eggs(ctx):
    embed=discord.Embed(title="***Eggs***", description="*Eggs Store .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette3.wikia.nocookie.net%2Fminecraft%2Fimages%2F8%2F87%2FSpawn_Eggs.gif%2Frevision%2Flatest%3Fcb%3D20120216160343&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="5 x Cow eggs  2.00 USD ", value = " `Cow spawn Egg `" ,inline=False)
    embed.add_field(name="5 x Sheep eggs  2.00 USD ", value = " `Sheep spawn Egg `" ,inline=False)
    embed.add_field(name="5 x Pig  eggs  2.00 USD ", value = " `Pig  spawn Egg `" ,inline=False)
    embed.add_field(name="2 x Dogs eggs  2.00 USD ", value = " `Dogs  spawn Egg `" ,inline=False)
    embed.add_field(name="2 x Cats eggs  2.00 USD ", value = " `Cats  spawn Egg `" ,inline=False)
    embed.add_field(name="5 x Parrot eggs  3.00 USD ", value = " `Parrot  spawn Egg `" ,inline=False)
    embed.add_field(name="2 x Zombie eggs  2.50", value = " `Zombie  spawn Egg `" ,inline=False)
    embed.add_field(name="2 x Skeleton eggs  2.50", value = " `Skeleton  spawn Egg `" ,inline=False)
    embed.add_field(name="2 x Creeper eggs  2.50", value = " `Creeper  spawn Egg `" ,inline=False)
    embed.set_footer(text=".(Egg name)_Egg  exsample:  .Cow_Egg ")
    await ctx.send(embed=embed)
    
            #################Cow egg######################################

@client.command() 
async def Cow_Egg(ctx):
    embed=discord.Embed(title="***Cow Egg ***", description="*5 Cow spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/47b16593084740faeb036804e7aff8fabd44a442.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="5 x Cow eggs  2.00 USD ", value = " `Cow spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 5 eggs do .Buy_Cow_Eggs ")
    await ctx.send(embed=embed)
    
    #######################Sheep egg #####################################
@client.command() 
async def Sheep_Egg(ctx):
    embed=discord.Embed(title="***Sheep Egg ***", description="*5 Sheep spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/9822898d5a74e2150bf18722a7c464c184951b8c.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="5 x Sheep eggs  2.00 USD ", value = " `Sheep spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 5 eggs do .Buy_Sheep_Eggs ")
    await ctx.send(embed=embed)  

    #######################Pig egg #####################################
@client.command() 
async def Pig_Egg(ctx):
    embed=discord.Embed(title="***Pig Egg ***", description="*5 Pig spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/5842f515724bc6b85d472e65b6936e6bb61d5e53.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="5 x Pig eggs  2.00 USD ", value = " `Pig spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 5 eggs do .Buy_Pig_Eggs ")
    await ctx.send(embed=embed)    
    
    
    #######################2 x Dogs eggs #####################################
@client.command() 
async def Dogs_Egg(ctx):
    embed=discord.Embed(title="***Dogs Egg ***", description="*2 Dogs spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/8fbdd89396b82a95c5f7b0c10185a4f0d34b036c.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="2 x Dogs eggs  2.00 USD ", value = " `Dogs spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 2 eggs do .Buy_Dogs_Eggs ")
    await ctx.send(embed=embed)
    
    
    #######################2 x Dogs eggs #####################################
@client.command() 
async def  Cats_Egg(ctx):
    embed=discord.Embed(title="*** Cats  Egg ***", description="*2  Cats  spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette3.wikia.nocookie.net%2Fminecraft%2Fimages%2F8%2F87%2FSpawn_Eggs.gif%2Frevision%2Flatest%3Fcb%3D20120216160343&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="2 x  Cats  eggs  2.00 USD ", value = " ` Cats  spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 2 eggs do .Buy_ Cats _Eggs ")
    await ctx.send(embed=embed)

    #######################5 x Parrot eggs #####################################
@client.command() 
async def  Parrot_Egg(ctx):
    embed=discord.Embed(title="*** Parrot  Egg ***", description="*5  Parrot  spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fgamepedia.cursecdn.com%2Fminecraft_gamepedia%2Fthumb%2Fe%2Fee%2FParrot_Spawn_Egg_JE1_BE1.png%2F150px-Parrot_Spawn_Egg_JE1_BE1.png%3Fversion%3D99371fdaebc692d8113cb1caf1421972&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="5 Parrot  eggs 3.00 USD ", value = " ` Parrot  spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 5 eggs do .Buy_Parrot_Eggs ")
    await ctx.send(embed=embed)

    #######################2 x Villager eggs #####################################
@client.command() 
async def Villager_Egg(ctx):
    embed=discord.Embed(title="*** Villager  Egg ***", description="*2  Villager spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/811f9157168c22624f4731c59bf19ac610b36921.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="2 Villager eggs 2.00 USD ", value = " ` Villager  spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 2 eggs do .Buy_Villager_Eggs ")
    await ctx.send(embed=embed)


    #######################2 x Villager eggs #####################################
@client.command() 
async def Zombie_Egg(ctx):
    embed=discord.Embed(title="*** Zombie  Egg ***", description="*2 Zombie spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/365b17f8530c469b56877b4b58d335801518630e.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="2 Zombie eggs 2.50 USD ", value = " ` Zombie  spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 2 eggs do .Buy_Zombie_Eggs ")
    await ctx.send(embed=embed)    
    
    #######################2 x Skeleton eggs #####################################
@client.command() 
async def Skeleton_Egg(ctx):
    embed=discord.Embed(title="*** Skeleton  Egg ***", description="*2 Skeleton spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/7e1c8cabca7e92ef572ffc067e3f45470cfe2a7c.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="2 Skeleton eggs 2.50 USD ", value = " ` Skeleton  spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 2 eggs do .Buy_Skeleton_Eggs ")
    await ctx.send(embed=embed)


    #######################2 x Creeper eggs #####################################
@client.command() 
async def Creeper_Egg(ctx):
    embed=discord.Embed(title="*** Creeper  Egg ***", description="*2 Creeper spawn Eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.kindpng.com%2Fpicc%2Fm%2F138-1380154_minecraft-creeper-egg-png-transparent-png.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="2 Creeper eggs 2.50 USD ", value = " ` Creeper  spawn Egg `" ,inline=False)
    embed.set_footer(text="You want Buy this 2 eggs do .Buy_Creeper_Eggs ")
    await ctx.send(embed=embed)

###################Buy Eggs#############################
###Buy Cow_Egg####
@client.command() 
async def Buy_Cow_Eggs(ctx):
    embed=discord.Embed(title="***Buy Cow Eggs***", description="*Buy and gift 5 Cow eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708446" ,inline=False)
    embed.add_field(name="5 Cow eggs 2.00 USD  ", value = " `Cow spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708446")    
    
###Buy Sheep_Egg####
@client.command() 
async def Buy_Sheep_Eggs(ctx):
    embed=discord.Embed(title="***Buy Sheep Eggs***", description="*Buy and gift 5 Sheep eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708450" ,inline=False)
    embed.add_field(name="5 Sheep eggs 2.00 USD  ", value = " `Sheep spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708450")
    
    ###Buy Pig_Egg####
@client.command() 
async def Buy_Pig_Eggs(ctx):
    embed=discord.Embed(title="***Buy Pig Eggs***", description="*Buy and gift 5 Pig eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708454" ,inline=False)
    embed.add_field(name="5 Pig eggs 2.00 USD  ", value = " `Pig spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708454")        
    
    
    ###Buy Pig_Egg####
@client.command() 
async def Buy_Dogs_Eggs(ctx):
    embed=discord.Embed(title="***Buy Dogs Eggs***", description="*Buy and gift 2 Dogs eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708466" ,inline=False)
    embed.add_field(name="2 Dogs eggs 2.00 USD  ", value = " `Dogs spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708466")        
    
    
    ###Buy Cats_Egg####
@client.command() 
async def Buy_Cats_Eggs(ctx):
    embed=discord.Embed(title="***Buy Cats Eggs***", description="*Buy and gift 2 Cats eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708467" ,inline=False)
    embed.add_field(name="2 Cats eggs 2.00 USD  ", value = " `Cats spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708467")        
    
    ###Buy Parrot_Egg####
@client.command() 
async def Buy_Parrot_Eggs(ctx):
    embed=discord.Embed(title="***Buy Parrot Eggs***", description="*Buy and gift 5 Parrot eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708460" ,inline=False)
    embed.add_field(name="5 Parrot eggs 3.00 USD  ", value = " `Parrot spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708460")        
    
    ###Buy Villager_Egg####
@client.command() 
async def Buy_Villager_Eggs(ctx):
    embed=discord.Embed(title="***Buy Villager Eggs***", description="*Buy and gift 2 Villager eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708457" ,inline=False)
    embed.add_field(name="2 Villager eggs 2.00 USD  ", value = " `Villager spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708457")  

    ###Buy Villager_Egg####
@client.command() 
async def Buy_Zombie_Eggs(ctx):
    embed=discord.Embed(title="***Buy Zombie Eggs***", description="*Buy and gift 2 Zombie eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = " https://dsg-minecraft-server.tebex.io/package/4708462" ,inline=False)
    embed.add_field(name="2 Zombie eggs 2.50 USD  ", value = " `Zombie spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708462")       

    ###Buy Skeleton _Egg####
@client.command() 
async def Buy_Skeleton_Eggs(ctx):
    embed=discord.Embed(title="***Buy Skeleton  Eggs***", description="*Buy and gift 2 Skeleton  eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = "https://dsg-minecraft-server.tebex.io/package/4708464" ,inline=False)
    embed.add_field(name="2 Skeleton  eggs 2.50 USD  ", value = " `Skeleton  spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708464")    
  
  ###Buy Skeleton _Egg####
@client.command() 
async def Buy_Creeper_Eggs(ctx):
    embed=discord.Embed(title="***Buy  Creeper  Eggs***", description="*Buy and gift 2  Creeper  eggs.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Eggs ", value = "https://dsg-minecraft-server.tebex.io/package/4708465" ,inline=False)
    embed.add_field(name="2  Creeper  eggs 2.50 USD  ", value = " ` Creeper  spawn egss`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Eggs = https://dsg-minecraft-server.tebex.io/package/4708465")    

##############inagame money #######################################
@client.command() 
async def Money(ctx):
    embed=discord.Embed(title="***Money(Ingame)***", description="*Ingame money  Store .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/0d496dcc9c4f74d067e11dd3a9ab4fb456e65ab9.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="10,000 Money   1.00 USD", value = " `10000 inagme money .Buy This .I_Money  `" ,inline=False)
    embed.add_field(name="20,000 Money   2.00 USD ", value = " `20000 inagame money.  Buy This .II_Money`" ,inline=False)
    embed.add_field(name="30,000 Money   3.00 USD ", value = " `30000 ingame money.   Buy This .III_Money`ree_Money`" ,inline=False)
    embed.add_field(name="40,000 Money   4.00 USD ", value = " `40000 inagme money.  Buy This .IV_Money`" ,inline=False)
    embed.add_field(name="50,000 Money   4.50 USD ", value = " `50000 ingame money.   Buy This .V_Money`" ,inline=False)
    embed.set_footer(text=".(MoneyBlace)_Money  exsample:  .10,000_Money ")
    await ctx.send(embed=embed)
  #################buy money###########################################
    #######################Money  #####################################
    
    

@client.command() 
async def I_Money(ctx):
    embed=discord.Embed(title="*** 10,000 Money ***", description="*ingame money*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/0d496dcc9c4f74d067e11dd3a9ab4fb456e65ab9.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="10,000 inagme money  1.00 USD ", value = " ` Ingame money `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_I_Money ")
    await ctx.send(embed=embed)

@client.command() 
async def II_Money(ctx):
    embed=discord.Embed(title="*** 20,000 Money ***", description="*ingame money.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/0d496dcc9c4f74d067e11dd3a9ab4fb456e65ab9.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="20,000 inagme money  2.00 USD ", value = " ` Ingame money `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_II_Money ")
    await ctx.send(embed=embed)
    
@client.command() 
async def III_Money(ctx):
    embed=discord.Embed(title="*** 30,000 Money ***", description="*ingame money.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/0d496dcc9c4f74d067e11dd3a9ab4fb456e65ab9.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="30,000 inagme money  3.00 USD ", value = " ` Ingame money `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_III_Money ")
    await ctx.send(embed=embed)
@client.command() 
async def IV_Money(ctx):
    embed=discord.Embed(title="*** 40,000 Money ***", description="*ingame money.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/0d496dcc9c4f74d067e11dd3a9ab4fb456e65ab9.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="40,000 inagme money  4.00 USD ", value = " ` Ingame money `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_IV_Money ")
    await ctx.send(embed=embed)
    
@client.command() 
async def V_Money(ctx):
    embed=discord.Embed(title="*** 50,000 Money ***", description="*ingame money.*", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/0d496dcc9c4f74d067e11dd3a9ab4fb456e65ab9.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="10,000 inagme money  4.50 USD ", value = " ` Ingame money `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_V_Money ")
    await ctx.send(embed=embed)

  
      ###10000 Buy money###########################################
@client.command() 
async def Buy_I_Money(ctx):
    embed=discord.Embed(title="***10,000 money***", description="*10,000 inagme money [I]  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Money ", value = "https://dsg-minecraft-server.tebex.io/package/4682215" ,inline=False)
    embed.add_field(name="10,000 Money  1.00 USD", value = " `10000 ingame money`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682215")    
   

  ###20000 money###########################################
@client.command() 
async def Buy_II_Money(ctx):
    embed=discord.Embed(title="***20,000 money***", description="*20,000 inagme money [II]  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Money ", value = "https://dsg-minecraft-server.tebex.io/package/4682216" ,inline=False)
    embed.add_field(name="20,000 Money  2.00 USD", value = " `20000 ingame money`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682216")    

  ###30000 money###########################################
@client.command() 
async def Buy_III_Money(ctx):
    embed=discord.Embed(title="***30,000 money***", description="*30,000 inagme money [III]  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Money ", value = "https://dsg-minecraft-server.tebex.io/package/4682218" ,inline=False)
    embed.add_field(name="30,000 Money  3.00 USD", value = " `30000 ingame money`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682218")    
  
  ###40000 money###########################################
@client.command() 
async def Buy_IV_Money(ctx):
    embed=discord.Embed(title="***40,000 money***", description="*40,000 inagme money [IV]  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Money ", value = "https://dsg-minecraft-server.tebex.io/package/4682219" ,inline=False)
    embed.add_field(name="40,000 Money  4.00 USD", value = " `40000 ingame money`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682219")    

  ###50000 money###########################################
@client.command() 
async def Buy_V_Money(ctx):
    embed=discord.Embed(title="***50,000 money***", description="*50,000 inagme money [V]  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Money ", value = "https://dsg-minecraft-server.tebex.io/package/4682220" ,inline=False)
    embed.add_field(name="50,000 Money  4.50 USD", value = " `40000 ingame money`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682220")    

  





##############################################################Commands##################################
@client.command() 
async def Commands(ctx):
    embed=discord.Embed(title="***Money(Ingame)***", description="*Ingame money  Store .*", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fw7.pngwing.com%2Fpngs%2F849%2F1006%2Fpng-transparent-brown-block-illustration-minecraft-pocket-edition-command-block-mod-block-game-video-game-survival.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fminecraft%2Fimages%2F2%2F2d%2FMonster_Spawner.png%2Frevision%2Flatest%3Fcb%3D20111015163758&f=1&nofb=1
    embed.add_field(name="FLY Command   1.00 USD", value = " `Fly command   1 week .Fly_Command`" ,inline=False)
    embed.add_field(name="HEAL Command   2.00 USD ", value = " `Get access for HEAL command for  1 week   .Heal_Command`" ,inline=False)
    embed.add_field(name="5 Player Warps  3.00 USD ", value = " `5 Player warps    .Pw_V_Command `" ,inline=False)
    embed.add_field(name="10 Player Warps   4.00 USD ", value = " `10 Player warps.   .Pw_X_Command`" ,inline=False)
    await ctx.send(embed=embed)
###############Buy Commands##################################
##########fly##############################
@client.command() 
async def Fly_Command(ctx):
    embed=discord.Embed(title="***Fly Command***", description="*Get access for Fly command for 1 Week  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/e17989d0387a1c66621fe9061c3e29923ea5a95a.jpg")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="fly 2.00 USD", value = " `Fly command for 1 Week`" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_Fly_Command")
    await ctx.send(embed=embed)
###########################Heal######################################################


@client.command() 
async def Heal_Command(ctx):
    embed=discord.Embed(title="***Heal Command***", description="*Get access for heal command for 1 Week  *", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/8ea32734bb282efd565bc269d5db2e69f0c8f67e.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Heal  2.00 USD", value = " `Heal command for 1 Week`" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_Heal_Command ")
    await ctx.send(embed=embed)
    
    
###############5pw ####################################################################   
@client.command() 
async def Pw_V_Command (ctx):
    embed=discord.Embed(title="***Player warps 5 Command***", description="*player warps 5 *", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/8ea32734bb282efd565bc269d5db2e69f0c8f67e.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="5 player warps 4.00 USD", value = " `pw 5 command `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_Pw_V_Command ")
    await ctx.send(embed=embed)
  
  ###############5pw ####################################################################   
@client.command() 
async def Pw_X_Command (ctx):
    embed=discord.Embed(title="***Player warps 10 Command***", description="*Player warps 10 *", color = 0x0328fc)
    embed.set_thumbnail(url="https://dunb17ur4ymx4.cloudfront.net/packages/images/8ea32734bb282efd565bc269d5db2e69f0c8f67e.png")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="10 player warps 7.00 USD", value = " `pw 10 command `" ,inline=False)
    embed.set_footer(text="You want Buy  money  do .Buy_Pw_X_Command ")
    await ctx.send(embed=embed)
   
#############################Buy####################command
#######################fly buy gift################################################################
@client.command() 
async def Buy_Fly_Command(ctx):
    embed=discord.Embed(title="***Fly command***", description="*Fly COmmand buy and gift *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Command", value = "https://dsg-minecraft-server.tebex.io/package/4682227" ,inline=False)
    embed.add_field(name="Fly command 2.00 USD", value = " `Fly command`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682227")    
##########################Heal##########################
@client.command() 
async def Buy_Heal_Command(ctx):
    embed=discord.Embed(title="***Heal command***", description="*Heal Command buy and gift *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Command", value = "https://dsg-minecraft-server.tebex.io/package/4682230" ,inline=False)
    embed.add_field(name="Heal command 2.00 USD", value = " `Heal command`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682230")    

##########################pw_V##########################
@client.command() 
async def Buy_Pw_V_Command(ctx):
    embed=discord.Embed(title="***Player warps 5 command***", description="*5 player warps buy and gift *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Command", value = "https://dsg-minecraft-server.tebex.io/package/4682233" ,inline=False)
    embed.add_field(name="5 player warps command 4.00 USD", value = " `pw command`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682233")    

##########################pw_X##########################
@client.command() 
async def Buy_Pw_X_Command(ctx):
    embed=discord.Embed(title="***Player warps 10 command***", description="*10 player warps buy and gift *", color = 0x0328fc)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_208967.png&f=1&nofb=1")   # url image https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngitem.com%2Fpimgs%2Fm%2F247-2471666_minecraft-cow-png-mc-cow-transparent-png.png&f=1&nofb=1
    embed.add_field(name="Gift and buy Command", value = "https://dsg-minecraft-server.tebex.io/package/4682233" ,inline=False)
    embed.add_field(name="10 player warps command 7.00 USD", value = " `pw command`" ,inline=False)
    await ctx.send(embed=embed)
    await ctx.author.send("buy And Gift the Money = https://dsg-minecraft-server.tebex.io/package/4682233")    





# eggs imeg https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.kindpng.com%2Fpicc%2Fm%2F138-1380154_minecraft-creeper-egg-png-transparent-png.png&f=1&nofb=1    
client.run(TOKEN)

