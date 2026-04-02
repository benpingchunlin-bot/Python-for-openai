import anthropic
import time

client = anthropic.Anthropic()

with open("files/transcript.txt", "r") as f:
    transcript = f.read()

start_time = time.time()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    messages=[{"role": "user", "content": f"Summarize the following video transcript.:\n{transcript}"}],
)
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Response time: {elapsed_time:.4f} seconds")
print(response.content[0].text)
