from base64 import b64encode
from anthropic import Anthropic

client = Anthropic()

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        base64_image = b64encode(image_data).decode('utf-8')
    return base64_image
# Example usage

"""
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {"role": "user", "content": "Hello, Claude! "}
    ]
)
"""

base64_image = encode_image("image.jpg")
response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Give the name of the animal in this image.",
                    },
                    {"type": "image",
                    "source": {"type": "base64",
                               "media_type": "image/jpeg",
                               "data": base64_image}
                }
            ]
        }
    ]
)

print(response.content[0].text)