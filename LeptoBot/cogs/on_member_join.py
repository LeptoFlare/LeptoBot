"""cogs.OnMemberJoin"""
from discord.ext import commands


class OnMemberJoin(commands.Cog):
    """Contains the on_member_join listener."""

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Assign the person role upon joining the server."""
        person_role = member.guild.get_role(598870617412075550)
        await member.add_roles(person_role)
