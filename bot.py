import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import os
import json
import urllib
from urllib import request


level = []
name = []
bot = discord.Client()
bot_prefix="e!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready() :
    print("Bot çevrimiçi!")
    print("İsim : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print(str(len(bot.servers)) + " tane serverda çalışıyor!")
    print(str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!")
    await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!"))
    
def loll (usr: str):
    global level
    global name
    url = 'https://tr1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+ usr +'?api_key=' + os.environ.get('api')
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    level = data["summonerLevel"]
    name = data["name"]
    

    
@bot.command(pass_context=True)
async def rol(ctx, member:discord.Member):
    await bot.delete_message(ctx.message)
    role = discord.utils.get(member.server.roles, name='Kurucu💎')
    role = discord.utils.get(member.server.roles, name='Gamer')
    await bot.add_roles(member, role)

@bot.command(pass_context=True)
async def hadibakim(ctx) :
    await bot.say("Birileri demiş öldü şimdi yazsınlar KRAL geri döndü!")

@bot.command(pass_context=True)
async def dev(ctx) :
    await bot.say("Beni geliştiren anan")
    
@bot.command(pass_context=True)
async def öp(ctx, member:discord.Member) :
   urll = ["http://24.media.tumblr.com/tumblr_m8yxnswMgE1rc0fd6o1_r5_500.gif" , 
   "https://pa1.narvii.com/5823/a1ff3fbec588fdde66dd24293f2220233ce42076_hq.gif" , 
   "https://media1.tenor.com/images/0de1905e4a8b2bb465d04a1f96df7f85/tenor.gif" , 
   "https://media.giphy.com/media/Gj8bn4pgTocog/giphy.gif" , 
   "http://24.media.tumblr.com/8d6a96407131c70a80c91544cddd8260/tumblr_mvaj4jBG0D1r60ay5o1_500.gif" , 
   "https://media1.giphy.com/media/G3va31oEEnIkM/giphy.gif" , 
   "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif" , 
   "https://media0.giphy.com/media/bGm9FuBCGg4SY/200.gif" , 
   "https://cdn.discordapp.com/attachments/477066430391779369/479234380200411156/1498492571_tumblr_mmnhw59Lh81spgltio1_500.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni öpüyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sik(ctx, member:discord.Member) :
   urll = ["https://static.hentai-gifs.com/upload/20160703/19/36972/1.gif" , 
   "https://78.media.tumblr.com/931125762652e49075f26f954049c0da/tumblr_msvseafYc01sflbiso1_1280.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-sexe-hentai.gif" , 
   "https://78.media.tumblr.com/3acd627d51c3484deb5a1349dba15f61/tumblr_nerlc5vPvU1u3p95io1_500.gif" , 
   "https://68.media.tumblr.com/37320d7ba87cc087713cd5f42ceff0fa/tumblr_ok06xwuKen1v2hfg0o1_500.gif" ,
   "https://78.media.tumblr.com/188f0818225d5f1c579a0eb5010b0c90/tumblr_o5498914Dp1ugdh13o1_500.gif" , 
   "https://78.media.tumblr.com/852fc9eff5caf44be79e92295676fbd1/tumblr_o549fohYOD1ugdh13o8_540.gif" ,
   "https://78.media.tumblr.com/54a670815a39bde673bdaaa35f08a88d/tumblr_o548wwiAhn1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/65b0296ed9d5e12e79ac1c02c4502b63/tumblr_o548y9hptR1ugdh13o1_500.gif" , 
   "https://78.media.tumblr.com/916f8497317b49edb5802fa6aa411f47/tumblr_o5492gX7Ir1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/de046b1380f663bf05d4833de2ec8078/tumblr_o54939bHby1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/9cdba610e7f393539718c12a010c12c1/tumblr_o5493vuIAk1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/5a030c57050ce1bcaa4c5efc116ad27a/tumblr_o5496dmxSS1ugdh13o1_500.gif" ,
   "https://static.hentai-gifs.com/upload/20160530/18/36676/1.gif", 
   "https://78.media.tumblr.com/bd1af323390c9dc5362a56a5ada27a3a/tumblr_p25vpc5DGO1vkkt9ro1_1280.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-hentai.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-hentai.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animations-hentai.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-manga-porno.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/scenes-hentai.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/scene-sexe-hentai-hard.gif" ,
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-mangas-pornos.gif" ,
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/dessins-hentai-sexe.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/sexe-hentai.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/scene-sexe-hentai-debout.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-plaisir.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-levrette-2.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/mangas-pornos-sexe.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animation-mangas-pornos.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/manga-sexe-porno.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-hentai-plaisir.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animation-hentai-sodomie.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/mangas-pornos-animes.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-sexe-trio.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-hentai-penetration.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-anime-sexe-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-gifs-sexe.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gifs-sexe-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-sexe-manga-porno.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/scene-chaude-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/fellation-gif-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animation-hentai-1.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/plaisirs-sexuels-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animation-sodomie-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/sexe-hentai-gif.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-animation.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/sexe-debout-gif-hentai.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-sexe-hentai-1.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-plaisir-solo.gif",
   "https://78.media.tumblr.com/49c0d8d34278a6cd1cfe7030e3eee16a/tumblr_p25vnrzC4R1vkkt9ro1_500.gif",
   "https://78.media.tumblr.com/a39ae50d2ba1ee6441a2d038e37c3732/tumblr_p25vjpiFyU1vkkt9ro1_500.gif",
   "https://78.media.tumblr.com/192e5b0335c16503e30d5fb2dfa18062/tumblr_omav74dggm1vkkt9ro3_1280.gif",
   "https://images.sex.com/images/pinporn/2015/09/23/620/13859134.gif",
   "https://i.imgur.com/rtmGBTC.gif"]
   if member.name == "ETDC" :
       await bot.say("Yakışmıyor sana " + ctx.message.author.name)
   else :
       embed = discord.Embed(title=ctx.message.author.name + " seni sikiyor " + member.name)
       embed.set_image(url=random.choice(urll))
       await bot.say(embed = embed)
    
@bot.command(pass_context=True)
async def sakso(ctx, member:discord.Member) :
   urll = ["https://78.media.tumblr.com/95a43cfe1124675948ee753941fe169e/tumblr_o8ufjuFpqI1urpdgno1_540.gif" , 
   "https://78.media.tumblr.com/c20426f84eda26c74e55c737b9257440/tumblr_omav14cUad1vkkt9ro2_500.gif" , 
   "http://68.media.tumblr.com/6f5df52d809ed9c7bd8d1f4c54d6829d/tumblr_njxjq6L4WV1u7ylgco1_400.gif" , 
   "https://78.media.tumblr.com/tumblr_m8z2uawCvV1rdw7hvo1_500.gif" , 
   "https://78.media.tumblr.com/07846221248f42eb6078b8188c25b419/tumblr_obi83jv6pa1vzttmyo1_500.gif" , 
   "https://static.hentai-gifs.com/upload/20160506/14/27001/1.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-gif.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/hentai-fellation.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-hentai-fellation.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-hentai-ejaculation.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/animations-hentai-fellation.gif",
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/fellation-hentai.gif",
   "https://78.media.tumblr.com/1ef63694b150c358c696552e6d0caa6a/tumblr_inline_oy14bahpdh1tl26vf_400.gif",
   "https://blog-imgs-75.fc2.com/m/o/m/momoerogazo/20150507135023e43.gif",
   "https://blog-imgs-75.fc2.com/m/o/m/momoerogazo/20150507134929e01.gif",
   "https://blog-imgs-75.fc2.com/m/o/m/momoerogazo/20150507135022844.gif"]
   if member.name == "ETDC" :
       await bot.say("Yakışmıyor sana " + ctx.message.author.name)
   else :
       embed = discord.Embed(title=ctx.message.author.name + " sana sakso çektiriyor " + member.name)
       embed.set_image(url=random.choice(urll))
       await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sev(ctx, member:discord.Member) :
   urll = ["https://media1.tenor.com/images/73a746bada06751716d3173fbb9e6864/tenor.gif" , 
   "https://media1.tenor.com/images/a4a2b1eaa47fd0d8d0951433bc59ab9a/tenor.gif" , 
   "https://media.giphy.com/media/K1InqndmlQDE4/giphy.gif" , 
   "https://i.pinimg.com/originals/2c/6e/4b/2c6e4bb81e44fe1a0b8c599f292e2be5.gif" , 
   "https://i.pinimg.com/originals/b6/9a/79/b69a790c15ebdc4a4bf9c16aa6dec786.gif" , 
   "https://media.giphy.com/media/lq72vRtxJtpgQ/giphy.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni seviyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sarıl(ctx, member:discord.Member) :
   urll = ["https://78.media.tumblr.com/2fe074ad467af41a8230b8d9d8e322f1/tumblr_omvj49wYnq1v8tshbo1_500.gif" , 
   "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif" , 
   "https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif" , 
   "https://media.giphy.com/media/3bqtLDeiDtwhq/giphy.gif" , 
   "https://78.media.tumblr.com/b4655e26f615a0e2081b9a6c90076539/tumblr_n13pt9SV4p1r45wgho2_500.gif" , 
   "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif" , 
   "https://i.gifer.com/B7bp.gif",
   "https://cdn.discordapp.com/attachments/357958080224559105/451687910090211338/171021_8687.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)


@bot.command(pass_context=True)
async def developer(ctx, member:discord.Member) :
   urll = ["https://media1.tenor.com/images/73a746bada06751716d3173fbb9e6864/tenor.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni seviyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def ahkmd(ctx, member:discord.Member) :
   embed = discord.Embed(title=ctx.message.author.name + " senin anana hükmediyor " + member.name)
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def dolar(ctx) :
    url = 'https://www.doviz.com/api/v1/currencies/all/latest'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    alis = data[0]["buying"]
    satis = data[0]["selling"]
    embed=discord.Embed(title="Dolar Kuru")
    embed.set_thumbnail(url="https://webiconspng.com/wp-content/uploads/2017/09/Dollar-PNG-Image-20560.png")
    embed.add_field(name="Satış", value=satis, inline=True)
    embed.add_field(name="Alış", value=alis, inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def euro(ctx) :
    url = 'https://www.doviz.com/api/v1/currencies/all/latest'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    alis = data[1]["buying"]
    satis = data[1]["selling"]
    embed=discord.Embed(title="Euro Kuru")
    embed.set_thumbnail(url="https://www.ayladt.com/images/farmanager-ayla-euro.png")
    embed.add_field(name="Satış", value=satis, inline=True)
    embed.add_field(name="Alış", value=alis, inline=True)
    await bot.say(embed=embed)

    
@bot.command(pass_context=True)
async def sterlin(ctx) :
    url = 'https://www.doviz.com/api/v1/currencies/all/latest'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    alis = data[2]["buying"]
    satis = data[2]["selling"]
    embed=discord.Embed(title="Sterlin Kuru")
    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTb3fo1Fn49kid84H3bFqIwuQSzGR38WiwSTztMSaT4LAVjskgtnQ")
    embed.add_field(name="Satış", value=satis, inline=True)
    embed.add_field(name="Alış", value=alis, inline=True)
    await bot.say(embed=embed)
   
@bot.command(pass_context=True)
async def manat(ctx) :
    url = 'https://www.doviz.com/api/v1/currencies/all/latest'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    alis = data[32]["buying"]
    satis = data[32]["selling"]
    embed=discord.Embed(title="Manat Kuru")
    embed.set_thumbnail(url="https://d30y9cdsu7xlg0.cloudfront.net/png/257351-200.png")
    embed.add_field(name="Satış", value=satis, inline=True)
    embed.add_field(name="Alış", value=alis, inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def soyle(ctx, *,content) :
    await bot.delete_message(ctx.message)
    await bot.say(content)



@bot.command(pass_context=True)
async def lol(ctx, msg):
    loll(msg)
    embed=discord.Embed()
    embed.set_thumbnail(url="http://avatar.leagueoflegends.com/tr/"+ msg +".png")
    embed.add_field(name=name, value="Level: " + str(level), inline=False)
    await bot.say(embed=embed)
    
    
@bot.command(pass_context=True)
async def kaçcm(ctx):
    x = random.randint(1, 40) 
    await bot.say(ctx.message.author.name + "'nin " + str(x) + " cm yarrağı var")

@bot.command(pass_context=True)
async def waifu(ctx) : 
    pers = ["hırslı" , "kibirli" , "garip" , "enerjik" , "nazik", "aceleci","iyi kalpli","melankoli","huysuz","dışına dönük","açık sözlü","şımarık","şakacı","sessiz","asi","ciddi","utangaç","kindar","kaçık"]
    age = ["15" , "16" , "17" , "18" , "19"]
    goz = ["mavi",
"kahverengi",
"koyu kahverengi",
"gri",
"yeşil",
"elâ",
"kehribar",
"akuamarin",
"masmavi",
"mavi",
"açık mavi",
"parlak yeşil",
"parlak turuncu",
"Parlak pembe",
"parlak mor",
"parlak gül",
"parlak turkuaz",
"parlak sarı",
"kahverengi",
"açık yeşil",
"kıpkırmızı",
"koyu mavi",
"koyu kahverengi",
"koyu gri",
"koyu yeşil",
"koyu turuncu",
"koyu Kırmızı",
"koyu Gül",
"koyu pembe",
"karanlık turkuaz",
"tozlu mavi",
"tozlu yeşil",
"tozlu turuncu",
"tozlu pembe",
"tozlu kırmızı",
"Gül kurusu",
"tozlu turkuaz",
"tozlu sarı",
"elektrik mavisi",
"yeşil",
"sıcak pembe",
"buz mavisi",
"çivit",
"lavanta",
"açık gri",
"leylak",
"limon dilimi",
"limon sarısı",
"Limon yeşili",
"eflatun",
"kestane rengi",
"gece yarısı mavisi",
"Portakal",
"erik mor",
"mor",
"kırmızı",
"pembe gül",
"kraliyet mor",
"Deniz mavisi",
"Deniz yeşili",
"gökyüzü mavi",
"kayrak mavi",
"turkuaz"
]
    sacstil = ["düzgünce örgülü" , "kısa kesilmiş" , "sol tarafı kesilmemiş" , "düzgünce sabitlenmiş" , "uzun örülmüş" , "kısa örülmüş" , "orta uzunlukta örülmüş " , "uzun at kuyruğu" , "orta uzunlukta at kuyruğu" , "kısa at at kuyruğu" , "salınık uzun" , "salınık kısa"]
    sactipi = ["düz" , "dalgalı" , "kıvırcık"]
    sacrengi = [ "kumral",
"siyah",
"sarı",
"kahverengi",
"koyu kahverengi",
"donuk sarı",
"altın sarısı",
"açık kahverengi",
"platin sarısı",
"kırmızı",
"krem",
"beyaz",
"kehribar",
"akuamarin",
"masmavi",
"mavi",
"açık mavi",
"parlak yeşil",
"parlak turuncu",
"Parlak pembe",
"parlak mor",
"parlak gül",
"parlak turkuaz",
"parlak sarı",
"kahverengi",
"açık yeşil",
"kıpkırmızı",
"koyu mavi",
"koyu kahverengi",
"koyu gri",
"koyu yeşil",
"koyu turuncu",
"koyu Kırmızı",
"koyu Gül",
"koyu pembe"
"karanlık turkuaz",
"tozlu mavi",
"tozlu yeşil",
"tozlu turuncu",
"tozlu pembe",
"tozlu kırmızı",
"Gül kurusu",
"tozlu turkuaz",
"tozlu sarı",
"elektrik mavisi",
"yeşil",
"sıcak pembe",
"buz mavisi",
"çivit",
"lavanta",
"açık gri",
"leylak",
"limon dilimi",
"limon sarısı",
"Limon yeşili",
"eflatun",
"kestane rengi",
"gece yarısı mavisi",
"Portakal",
"pastel mavi",
"pastel yeşil",
"pastel turuncu",
"pastel pembe",
"pastel mor",
"pastel gül",
"pastel turkuaz",
"pastel sarı",
"erik mor",
"mor",
"kırmızı",
"pembe gül",
"kraliyet mor",
"Deniz mavisi",
"Deniz yeşili",
"gökyüzü mavi",
"kayrak mavi",
"turkuaz"]
    giyim = ["genelde mütevazı elbiseler giyer" , "çok siyah giyinir" , "çok renkli giyinir" , "eski moda kıyafetler giymeyi sever" , "çirkin kıyafetleri giymeyi sever" , "oldukça muhafazakar elbiseler giyer"]
    boy = ["ortalama bir boya sahip" , "uzun boylu" , "biraz uzun boylu" , "çok uzun boylu" , "kısa boylu" , "biraz kısa boylu" , "çok kısa boylu"]
    agırlık = ["oldukça ince" , "biraz zayıf" , "ortalama bir ağırlıkta" , "biraz tombul" , "oldukça tombul" , "oldukça kaslı" , "bayağı kaslı"]
    kitap = ["Fantezi kitapları okumayı," , "Tarihsel kurgu okumayı," , "Korku kitapları okumayı," , "Gizem kitapları okumayı," , "Romantizm kitapları okumayı," , "Manga okumayı," , "Çizgi roman okumayı,"]
    film = [" fantezi filmleri izlemeyi," , " tarihi filmler izlemeyi," , " korku filmleri izlemeyi" , " gizem filmleri izlemeyi," , " romantizm filmleri izlemeyi," , " anime izlemeyi," , " çizgi film izlemeyi,"]
    sarki = [" ve J-POP dinlemeyi" , " ve klasik müzik dinlemeyi" , " ve metal dinlemeyi" , " ve death metal dinlemeyi" , " ve rap dinlemeyi" , " ve pop dinlemeyi" , " ve yöresel müzik dinlemeyi"]
    meme = ["çok küçük" , "biraz küçük" , "küçük" , "ortalama" , "biraz büyük" , "büyük" , "çok büyük"]
    waifu = "Bu " + random.choice(pers) + " " + random.choice(age) + " yaşında ki kız, " + random.choice(goz) + " renkli gözlere ve " + random.choice(sactipi) +" " +random.choice(sacrengi) +  " renginde " + random.choice(sacstil) + " saçlara sahip. O " + random.choice(agırlık) + ", " + random.choice(boy) + " ve " + random.choice(giyim) + "." + random.choice(kitap) + random.choice(film) + random.choice(sarki) + " seviyor ve " + random.choice(meme) + " göğüslere sahip"

    await bot.say(waifu)
   

@bot.command(pass_context=True)
async def husband(ctx) : 
    pers = ["hırslı" , "kibirli" , "garip" , "enerjik" , "nazik", "aceleci","iyi kalpli","melankoli","huysuz","dışına dönük","açık sözlü","şımarık","şakacı","sessiz","asi","ciddi","utangaç","kindar","kaçık"]
    age = ["15" , "16" , "17" , "18" , "19"]
    goz = ["mavi",
"kahverengi",
"koyu kahverengi",
"gri",
"yeşil",
"elâ",
"kehribar",
"akuamarin",
"masmavi",
"mavi",
"açık mavi",
"parlak yeşil",
"parlak turuncu",
"Parlak pembe",
"parlak mor",
"parlak gül",
"parlak turkuaz",
"parlak sarı",
"kahverengi",
"açık yeşil",
"kıpkırmızı",
"koyu mavi",
"koyu kahverengi",
"koyu gri",
"koyu yeşil",
"koyu turuncu",
"koyu Kırmızı",
"koyu Gül",
"koyu pembe",
"karanlık turkuaz",
"tozlu mavi",
"tozlu yeşil",
"tozlu turuncu",
"tozlu pembe",
"tozlu kırmızı",
"Gül kurusu",
"tozlu turkuaz",
"tozlu sarı",
"elektrik mavisi",
"yeşil",
"sıcak pembe",
"buz mavisi",
"çivit",
"lavanta",
"açık gri",
"leylak",
"limon dilimi",
"limon sarısı",
"Limon yeşili",
"eflatun",
"kestane rengi",
"gece yarısı mavisi",
"Portakal",
"erik mor",
"mor",
"kırmızı",
"pembe gül",
"kraliyet mor",
"Deniz mavisi",
"Deniz yeşili",
"gökyüzü mavi",
"kayrak mavi",
"turkuaz"
]
    sacstil = ["karışık" , "dağınık" , "uzun" , "kısa" , "normal uzuklukta" ]
    sactipi = ["düz" , "dalgalı" , "kıvırcık"]
    sacrengi = [ "kumral",
"siyah",
"sarı",
"kahverengi",
"koyu kahverengi",
"donuk sarı",
"altın sarısı",
"açık kahverengi",
"platin sarısı",
"kırmızı",
"krem",
"beyaz",
"kehribar",
"akuamarin",
"masmavi",
"mavi",
"açık mavi",
"parlak yeşil",
"parlak turuncu",
"Parlak pembe",
"parlak mor",
"parlak gül",
"parlak turkuaz",
"parlak sarı",
"kahverengi",
"açık yeşil",
"kıpkırmızı",
"koyu mavi",
"koyu kahverengi",
"koyu gri",
"koyu yeşil",
"koyu turuncu",
"koyu Kırmızı",
"koyu Gül",
"koyu pembe"
"karanlık turkuaz",
"tozlu mavi",
"tozlu yeşil",
"tozlu turuncu",
"tozlu pembe",
"tozlu kırmızı",
"Gül kurusu",
"tozlu turkuaz",
"tozlu sarı",
"elektrik mavisi",
"yeşil",
"sıcak pembe",
"buz mavisi",
"çivit",
"lavanta",
"açık gri",
"leylak",
"limon dilimi",
"limon sarısı",
"Limon yeşili",
"eflatun",
"kestane rengi",
"gece yarısı mavisi",
"Portakal",
"pastel mavi",
"pastel yeşil",
"pastel turuncu",
"pastel pembe",
"pastel mor",
"pastel gül",
"pastel turkuaz",
"pastel sarı",
"erik mor",
"mor",
"kırmızı",
"pembe gül",
"kraliyet mor",
"Deniz mavisi",
"Deniz yeşili",
"gökyüzü mavi",
"kayrak mavi",
"turkuaz"]
    giyim = ["genelde mütevazı elbiseler giyer" , "çok siyah giyinir" , "çok renkli giyinir" , "eski moda kıyafetler giymeyi sever" , "çirkin kıyafetleri giymeyi sever" , "oldukça muhafazakar elbiseler giyer"]
    boy = ["ortalama bir boya sahip" , "uzun boylu" , "biraz uzun boylu" , "çok uzun boylu" , "kısa boylu" , "biraz kısa boyly" , "çok kısa boylu"]
    agırlık = ["oldukça ince" , "biraz zayıf" , "ortalama bir ağırlıkta" , "biraz tombul" , "oldukça tombul" , "oldukça kaslı" , "bayağı kaslı"]
    kitap = ["Fantezi kitapları okumayı," , "Tarihsel kurgu okumayı," , "Korku kitapları okumayı," , "Gizem kitapları okumayı," , "Romantizm kitapları okumayı," , "Manga okumayı," , "Çizgi roman okumayı,"]
    film = [" fantezi filmleri izlemeyi," , " tarihi filmler izlemeyi," , " korku filmleri izlemeyi" , " gizem filmleri izlemeyi," , " romantizm filmleri izlemeyi," , " anime izlemeyi," , " çizgi film izlemeyi,"]
    sarki = [" ve J-POP dinlemeyi" , " ve klasik müzik dinlemeyi" , " ve metal dinlemeyi" , " ve death metal dinlemeyi" , " ve rap dinlemeyi" , " ve pop dinlemeyi" , " ve yöresel müzik dinlemeyi"]
    waifu = "Bu " + random.choice(pers) + " " + random.choice(age) + " yaşında ki erkek, " + random.choice(goz) + " renkli gözlere ve " + random.choice(sactipi) +" " +random.choice(sacrengi) +  " renginde " + random.choice(sacstil) + " saçlara sahip. O " + random.choice(agırlık) + ", " + random.choice(boy) + " ve " + random.choice(giyim) + "." + random.choice(kitap) + random.choice(film) + random.choice(sarki) + " seviyor."

    await bot.say(waifu)
    
    
bot.run(os.environ.get('token'))
