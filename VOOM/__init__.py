from .VOOM import VOO


async def setup(bot):
    await bot.add_cog(VOO(bot))
