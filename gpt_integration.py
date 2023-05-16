import bleak_connect_tb
import asyncio
import openai

openai.api_key = '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'

asyncio.run(bleak_connect_tb.main())

print("ENVIRONMENT SENSOR STATS:\n")

print("Temperature in Fahrenheit:", round(
    bleak_connect_tb.temp_in_fahrenheit, 2))
print("Humidity:", str(bleak_connect_tb.humidity) + "%")
print("UV Index:", bleak_connect_tb.uv_index)


def generateRecommendation(temperatureFahrenheit, humidityPercent, uvIndex):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="""

            Right now, it is {temperature}°F with a humidity percent of {humidity} and a UV index of {uv_index}.
            Should I go outside or stay inside, and why? If I can go outside, can you please recommend the proper 
            clothing given these weather conditions?

            """.format(temperature=temperatureFahrenheit, humidity=humidityPercent, uv_index=uvIndex),
        temperature=0.5,
        max_tokens=1000,
        frequency_penalty=0.0,
        presence_penalty=1
    )

    return response["choices"][0]["text"]


print("\n")
print("Here's the recommendation:", generateRecommendation(
    bleak_connect_tb.temp_in_fahrenheit, bleak_connect_tb.humidity, bleak_connect_tb.uv_index))
