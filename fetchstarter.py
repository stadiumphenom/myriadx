# fetchstarter.py
import requests

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Space_Nebula.jpg/640px-Space_Nebula.jpg"
out_path = "start.png"

with open(out_path, "wb") as f:
    f.write(requests.get(url).content)

print("Downloaded test image to start.png")
