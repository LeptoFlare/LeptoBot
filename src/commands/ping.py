"""File containing the ping check."""
import discord


async def ping(message, client):
    """Ping command."""
    if message.content == "🏓":
        embed = discord.Embed(color=0xDE2E43)
        embed.add_field(
            name=f":ping_pong: Latency: `{round(client.latency*1000)}ms`",
            value="\u200B"
        )
        await message.channel.send(embed=embed)
        return True
    return False
