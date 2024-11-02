async def ping_command(message):
    latency = round(client.latency * 1000)  # Convert to ms
    await message.channel.send(f'Pong! Latency is {latency}ms')
