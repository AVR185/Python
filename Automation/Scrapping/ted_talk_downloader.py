from unittest import result
from urllib import response
from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup
import re # Regular Expression pattern matching
import sys # for argument parsing

# Exception Handling
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the TED Talk URL")

# URL Examples
# https://www.ted.com/talks/lucas_joppa_how_to_fix_the_bugs_in_the_net_zero_code?language=es
# https://www.ted.com/talks/dan_jorgensen_how_wind_energy_could_power_earth_18_times_over?language=es
# https://www.ted.com/talks/karen_lellouche_tordjman_siri_alexa_google_what_comes_next?language=es

answer = requests.get(url) # get content of the url

print("Download about to start")

soup = BeautifulSoup(answer.content, features="lxml")
text = ""
for val in soup.findAll("script"):
    if (re.search("file", str(val))) is not None:
        text = str(val)

result_mp4 = re.search("(?P<url>https:\/\/[^\s]+mp4)", text).group("url") # regex to get the text with url of the video - With ?P<url> create groups of urls

mp4_url = result_mp4.split('"')[0]
print("Download video from... " + mp4_url)

file_name = mp4_url.split("/")[len(mp4_url.split("/")) - 1].split("?")[0]
print("Storing video in... " + file_name)

answer = requests.get(mp4_url) # Download

with open(file_name, "wb") as f: 
    f.write(answer.content) # Save


# Alternative method
#urlretrieve(mp4_url, file_name)

print("Video Downloaded and Saved")