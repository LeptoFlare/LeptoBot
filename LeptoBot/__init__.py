from discord.ext.commands import Bot

from .env import env
from .log import logger


class Client(Bot):
    """Subclass of commands.Bot containing helpful constants."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logger

    async def on_ready(self):
        """Ready event."""
        self.logger.info(f'Logged in as {client.user}.')


client = Client(command_prefix='!')
