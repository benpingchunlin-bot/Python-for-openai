from base64 import b64encode
from openai import OpenAI

client = OpenAI()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        base64_image = b64encode(image_data).decode('utf-8')
    return base64_image
# Example usage

base64_image = encode_image("image.jpg")
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Give the name of the animal in this image.",
                    },
                    {"type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}  
                }
            ]
        }
    ]
)
print(response.choices[0].message.content)