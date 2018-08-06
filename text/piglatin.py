original = input("What would you like to translate into pig latin?")
text = original.lower()

def eng_to_pigltn(text):
    words = text.split()
    pig_latin = ""
    
    for word in words:
        if len(word) == 1:
           pig_latin = pig_latin + word + " " 
        elif word[0] in "aeiou":
            word = word + "way"
            pig_latin = pig_latin + word + " " 
        elif word[0] not in "aeiou" and word[1] in "aeiou":
            word = word[1:] + word[0] + "ay"
            pig_latin = pig_latin + word + " " 
        elif word[0] not in "aeiou" and word[1] not in "aeiou":
            word = word[2:] + word[0:2] + "ay"
            pig_latin = pig_latin + word + " " 
        
    
    return pig_latin
        
print(eng_to_pigltn(text))
