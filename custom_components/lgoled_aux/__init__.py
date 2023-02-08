import asyncio
from .aiopylgtv import WebOsClient

DOMAIN = "lgoled_aux"

ATTR_MODE = "mode"
ATTR_IP = "ip"
DEFAULT_MODE = "dolbyHdrStandard"


def setup(hass, config):
    """Set up is called when Home Assistant is loading our component."""

    async def handle_picture_settings(call):
        """Handle the service call."""
        mode = call.data.get(ATTR_MODE, DEFAULT_MODE)
        ip = call.data.get(ATTR_IP, None)

        if ip == None:
            return False

        client = await WebOsClient.create(ip=ip,key_file_path=hass.config.path("lgoled_aux.db"))
        await client.disconnect()    
        await client.connect()
        await client.set_current_picture_mode(pic_mode=mode)

    hass.services.register(DOMAIN, "set_picture_mode", handle_picture_settings)

    # Return boolean to indicate that initialization was successful.
    return True
