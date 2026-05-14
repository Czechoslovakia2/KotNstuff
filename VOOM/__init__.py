from .VOOM import VOOM


async def setup(bot):
    await bot.add_cog(VOOM(bot))
