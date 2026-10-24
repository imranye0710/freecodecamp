import re

def wise_speak(sentence):
    if match := re.search(r"^(.*(?: have | must | are | will | can ))(.*?)([.!?])*$", sentence):
        start = match.group(2).split(" ")
        start = f"{start[0].capitalize()} {' '.join(start[1:])}"
        end = match.group(1).lower().strip() + match.group(3)
        return f"{start}, {end}"

    

print(wise_speak("You can do it!"))