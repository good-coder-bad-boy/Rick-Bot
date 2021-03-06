from discord import FFmpegPCMAudio, User, File
from discord.ext import commands
from keepalive import keep_alive
from os.path import realpath
from os import environ

bot = commands.Bot(command_prefix="$")

@bot.command()
async def rickroll(ctx):
	successes = 0

	for user in [u for u in ctx.message.mentions if not u.bot]:
		if isinstance(user, User):
			await user.send("Cheers! 🎉", file=File(fp=open("rick.mp3", "rb"), filename="<class IOFileBuffer.MP3(file='cheers.mp3')>", spoiler=True))
		else:
			UserVoiceChannel = user.voice.channel
			if UserVoiceChannel:
				VoiceChannel = await UserVoiceChannel.connect()
				await VoiceChannel.play(FFmpegPCMAudio(source=realpath("rick.mp3")))
				successes += 1

	await ctx.reply("%d Rickroll%s successfully created." % (successes, "s" * (successes != 1)), mention_author=False)

keep_alive()
bot.run(environ["TOKEN"])
