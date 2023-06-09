import json
import os 
import openai 
from pathlib import Path

PROMPT = "Nuclear reactor saving the world"

# Define and create a data directory called 'responses' that will hold the API responses as json files.
DATA_DIR = Path.cwd() / "responses"
print(DATA_DIR)
JSON_FILE = DATA_DIR / "image"
DATA_DIR.mkdir(exist_ok=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
    response_format="b64_json"
)

print(response["data"][0]["b64_json"][:50])

# For the file name, we are using the beginning of the sentence. 
# The latter is the time when the image has been created.
file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}"

with open(file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)
    # The output will not be the image. 
    # base64-encoded bits, which does not make for a great viewing experience if you are a human.
    # We will convert this into png file.
    # Now we need to convert this json file into png file.
print(file)

# convert.py
# The Script below will convert json file to png file.
'''
import json
from base64 import b64decode
from pathlib import Path

DATA_DIR = Path.cwd() / "responses"
JSON_FILE = DATA_DIR / f"{PROMPT[:5]}-{response['created']}"
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)
'''

# vary.py 
import json
import os
from base64 import b64decode
from pathlib import Path

import openai

DATA_DIR = Path.cwd() / "responses"
SOURCE_FILE = DATA_DIR / f"{PROMPT[:5]}-{response['created']}"

openai.api_key = os.getenv("OPENAI_API_KEY")

with open(SOURCE_FILE, mode="r", encoding="utf-8") as json_file:
    saved_response = json.load(json_file)
    image_data = b64decode(saved_response["data"][0]["b64_json"]) 
# decodes the image data using b64decode in the same mway we did in convert.py
# [0] is the first image we saved, we need to fix it accordingly, if we want to see the variation of other images.

# We are using the previous image as the source file for the variation.
response = openai.Image.create_variation(
    image=image_data,
    n=3,
    size="256x256",
    response_format="b64_json",
)

new_file_name = f"vary-{SOURCE_FILE.stem[:5]}-{response['created']}.json"

with open(DATA_DIR / new_file_name, mode="w", encoding="utf-8") as file:
    json.dump(response, file)

JSON_FILE = DATA_DIR / new_file_name
# JSON_FILE = "C:\Users\every\responses\vary-Nucle-1685559995.json"
IMAGE_DIR = Path.cwd() / "images" / JSON_FILE.stem

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

with open(JSON_FILE, mode="r", encoding="utf-8") as file:
    response = json.load(file)

for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    image_file = IMAGE_DIR / f"{JSON_FILE.stem}-{index}.png"
    with open(image_file, mode="wb") as png:
        png.write(image_data)
