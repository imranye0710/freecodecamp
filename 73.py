import re

def wise_speak(sentence):
    if match := re.search(r"^(.*(?:have | must | are | will | can))(.*?)([!?])*$", sentence):
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        start = match.group(2).split(" ")
        start = f"{start[0].capitalize()} {' '.join(start[1:])}"
        end = match.group(1).lower() + match.group(3)
        print(f"{start}, {end}")

    

print(wise_speak("You must speak wisely!"))