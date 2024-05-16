
import os
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = '6cdd6abf63bb4c77a2db843ed8a066f8'

from wechaty import Wechaty
import os

import asyncio
async def main():
    bot = Wechaty()
    bot.on('scan', lambda status, qrcode, data: print('Scan QR Code to login: {}\nhttps://wechaty.js.org/qrcode/{}'.format(status, qrcode)))
    bot.on('login', lambda user: print('User {} logged in'.format(user)))
    bot.on('message', lambda message: print('Message: {}'.format(message)))
    await bot.start()

asyncio.run(main())