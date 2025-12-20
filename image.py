from openai import OpenAI

Client = OpenAI()

url = "https://images.dog.ceo/breeds/hound-afghan/n02088094_1003.jpg"
response = Client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Give the name of the animal in the image."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": url
                    },
                },
            ],
        }
    ],
)
print(response.choices[0].message.content)
