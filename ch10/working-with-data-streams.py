
import asyncio

from random import Random

MAX_SAMPLES = 1000

async def data_stream():
    rng = Random(12345)  # seeded for examples
    
    for i in range(MAX_SAMPLES):
        sleep_time = rng.random()*3.
#        await asyncio.sleep(sleep_time)
        
        yield {"event_no": i, "width": max(0.0, rng.gauss(3.0, 0.5))}


async def check_event(event):
    event_no  = event["event_no"]
    width = event["width"]
   
    if abs(width - 3.0) > 1.2:
        print(f"Event {event_no} not within range ({width})")



async def process_stream():
    async for event in data_stream():
       asyncio.create_task(check_event(event))




asyncio.run(process_stream())



