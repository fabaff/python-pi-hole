"""
Copyright (c) 2018 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio
import json

import aiohttp

from pihole import PiHole


async def main():
    """Get the data from a Pi-hole instance."""
    async with aiohttp.ClientSession() as session:
        data = PiHole('192.168.0.214', loop, session)
        await data.get_data()

        # Get the raw data
        print(json.dumps(data.data, indent=4, sort_keys=True))

        print("Status:", data.status)
        print("Domains being blocked:", data.domains_being_blocked)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

