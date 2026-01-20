import asyncio
import aiohttp
import time

URL = "http://localhost:8080"
TOTAL_REQUEST = 1000
CONCURRENT = 1000
TIMEOUT = 5

success = 0
failed = 0

async def send_request(session, i):
    global success, failed
    try:
        async with session.get(URL, timeout=TIMEOUT) as resp:
            await resp.read()
            if resp.status == 200:
                success += 1
            else:
                failed += 1
    except Exception:
        failed += 1

async def main():
    start = time.time()

    connector = aiohttp.TCPConnector(limit=CONCURRENT)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(TOTAL_REQUEST):
            tasks.append(send_request(session, i))
            if len(tasks) >= CONCURRENT:
                await asyncio.gather(*tasks)
                tasks = []
        if tasks:
            await asyncio.gather(*tasks)

    duration = time.time() - start
    rps = round(TOTAL_REQUEST / duration, 2)

    print("\n===== LOAD TEST RESULT =====")
    print("Target        :", URL)
    print("Total Request :", TOTAL_REQUEST)
    print("Success       :", success)
    print("Failed        :", failed)
    print("Duration      :", round(duration, 2), "seconds")
    print("RPS           :", rps)

asyncio.run(main())