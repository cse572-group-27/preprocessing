import json

# Replace 3NHTGeZoLLIfoHnlwtOu6w with the json file name you want to open
with open("3NHTGeZoLLIfoHnlwtOu6w.json","r") as file:
    jsonData = json.load(file)

# Example how to get first line of transcript/show structure
ex = jsonData['results'][0]['alternatives'][0]['transcript']

# Final transcript string
final_transcript = ""

for result in jsonData["results"]:
    for alternative in result["alternatives"]:
        if "transcript" in alternative:
            final_transcript += alternative["transcript"] + " "

# Write transcript text to a .txt file
with open('final_transcript.txt', 'w') as file:
    file.write(final_transcript)
