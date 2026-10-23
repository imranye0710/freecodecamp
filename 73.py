def wise_speak(sentence):
    words = ["have", "must", "are", "will", "can"]
    sentence = sentence.split(" ")
    for i, w1 in enumerate(sentence):
        for w2 in words:
            if w1 == w2:
                rsent = sentence[i + 2:]
                rsent.insert(0, sentence[i + 1].capitalize())
                sentence = sentence[0: i + 1]

    return(f"{' '.join(rsent).strip('.')}, {' '.join(sentence).lower()}.")

    

print(wise_speak("You must speak wisely!"))