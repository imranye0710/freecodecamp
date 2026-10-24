import re

def wise_speak(sentence):
    if match := re.search(r"^(.*(?:have | must | are | will | can))(.*?)([!?])*$", sentence):
        print(match.group(1))
        print(match.group(2))
        print(match.group(3))
        start = match.group(2).split(" ")
        start = start[0].capitalize() + ' '.join(start[1:])
        print(start)

    

print(wise_speak("You must speak wisely!"))