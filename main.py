from bot import Bot
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

Bot().run()


import os
import asyncio
from aiohttp import web

from bot import Bot  # adjust if your bot import is different

# Health check route
async def healthcheck(request):
    return web.Response(text="OK")

async def start_bot():
    await Bot().start()

async def main():
    # Start bot
    asyncio.create_task(start_bot())

    # Start HTTP server for health checks
    app = web.Application()
    app.router.add_get('/', healthcheck)

    port = int(os.environ.get("PORT", 8080))  # use the expected port!
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    print(f"Healthcheck server running on port {port}")
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
  
