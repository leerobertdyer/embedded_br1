import subprocess, json, random, requests

# with open("affirmations.json") as f:
#     data = json.load(f)

# affirmation = random.choice(data)

# espeak = subprocess.Popen(
#     ["espeak", "-s", "70", "-p", "30", "-a", "200", "--stdout", affirmation["text"]],
#     stdout=subprocess.PIPE
# )
# subprocess.run(["aplay", "-D", "plughw:1,0"], stdin=espeak.stdout)
# espeak.wait()

with open("audioTestOne.wav", "rb") as f:
    response = requests.post(
        # "https://api.leedyer.com/stt",
        "http://localhost:3000/br1/stt",
        files={"audio": ("audioTestOne.wav", f, "audio/wav")},
        headers={"x-chat-api-secret": ""}
    )
print(response.json())
