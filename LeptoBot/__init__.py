"""LeptoBot"""
from discord import Intents
from discord.ext.commands import Bot

from .env import env
from .log import logger
from . import cogs


class Client(Bot):
    """Subclass of commands.Bot containing helpful constants."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger

    async def on_ready(self):
        """Ready event."""
        self.logger.info(f'Logged in as {client.user}.')

intents = Intents.default()
intents.members = True
client = Client(command_prefix='!', intents=intents)

cogs.register_cogs(client)
