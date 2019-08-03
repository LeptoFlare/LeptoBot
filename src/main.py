"""Main file that holds the Off the Dial Bot code."""
from logging import getLogger
import json
from coloredlogs import install as install_color
import discord


class Client(discord.Client):
    """The CLIENT for the Off The Dial Discord bot."""

    logger = getLogger(__name__)
    install_color(
        level="INFO",
        fmt="%(asctime)s: %(levelname)s: %(message)s",
        datefmt="%m/%d %H.%M.%S"
    )

    async def on_ready(self):
        """Call when bot is ready."""
        Client.logger.info("%s is logged in.", self.user.name)

    async def on_message(self, message):
        """Call when message is sent."""

    async def on_member_join(self, member):
        """Call a member joins a guild."""
        person_role = member.guild.get_role(598870617412075550)
        await member.add_roles(person_role)


def main():
    """Call Main function."""
    with open("../config.json", "r") as infile:
        try:
            token = json.load(infile)["token"]

        except (KeyError, FileNotFoundError):
            raise EnvironmentError(
                "Your config.json file is either missing, or incorrect. Check your config.json and ensure it has the key 'token'."
            )
    CLIENT.run(token)


if __name__ in "__main__":
    CLIENT = Client()
    main()
