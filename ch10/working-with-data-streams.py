import faust

from numpy.random import default_rng
rng = default_rng(12345)


app = faust.App("sample", broker="kafka://localhost")


class Record(faust.Record, serializer="json"):
    id_string: str
    value: float

topic = app.topic("sample-topic", value_type=Record)

@app.agent(topic)
async def process_record(records):
    async for record in records:
        print(f"Got {record.id_string}: {record.value}")


@app.timer(interval=1.0)
async def producer1(app):
    await app.send(
        "sample-topic",
        value=Record(id_string="producer 1", value=rng.uniform(0, 2))
    )

@app.timer(interval=2.0)
async def producer2(app):
    await app.send(
        "sample-topic",
        value=Record(id_string="producer 2", value=rng.uniform(0, 5))
    )



app.main()