import pystray
import requests
from PIL import Image, ImageDraw
from io import BytesIO
from time import sleep

def setup(icon):
    input("Enter to cancel")
    icon.stop()

response = requests.get("https://www.duckdns.org/img/ducky_icon_medium.png")
image = Image.open(BytesIO(response.content))
icon = pystray.Icon("PyDuckDNS Icon", icon=image, title="PyDuckDNS")
icon.run()