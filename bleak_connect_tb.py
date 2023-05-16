from bleak import BleakClient


async def main():

    address = "EEFE8AEA-2FE3-BBD7-4C0D-F2D2BA211799"

    # char = dict()

    async with BleakClient(address) as client:
        print(client.is_connected)

        services = client.services

        for service in services:
            # print('service', service.handle, service.uuid, service.description)

            characteristics = service.characteristics

            for char in characteristics:
                # print('characteristic', char.handle, char.uuid,
                #       char.description, char.properties)

                descriptors = char.descriptors

                # for desc in descriptors:
                #     print('descriptor', desc)

        TEMPERATURE_MEASUREMENT_ID = '00002a6e-0000-1000-8000-00805f9b34fb'

        temp_bytes = await client.read_gatt_char(TEMPERATURE_MEASUREMENT_ID)

        raw_temperature = int.from_bytes(temp_bytes, 'little')

        global temp_in_celsius
        global temp_in_fahrenheit
        global humidity
        global uv_index

        temp_in_celsius = raw_temperature / 100
        temp_in_fahrenheit = temp_in_celsius * (9/5) + 32

        # print("Temperature in Celsius:", round(temp_in_celsius, 2))
        # print("Temperature in Fahrenheit:", round(temp_in_fahrenheit, 2))

        HUMIDITY_INDEX_ID = '00002a6f-0000-1000-8000-00805f9b34fb'

        humidity_bytes = await client.read_gatt_char(HUMIDITY_INDEX_ID)

        raw_humidity = int.from_bytes(humidity_bytes, 'little')
        humidity = raw_humidity/100

        # print("Humidity:", str(humidity) + "%")

        UV_INDEX_ID = '00002a76-0000-1000-8000-00805f9b34fb'

        uv_bytes = await client.read_gatt_char(UV_INDEX_ID)

        uv_index = int.from_bytes(uv_bytes, 'little')

        # print("UV Index:", uv_index)

        # await client.start_notify(TEMPERATURE_MEASUREMENT_ID, temperature_callback)
        # await asyncio.sleep(30)
        # await client.stop_notify(TEMPERATURE_MEASUREMENT_ID)
