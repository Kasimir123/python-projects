original = input("What would you like to translate into pig latin?")
text = original.lower()
double_consonants = "ch th sp sl gr wh "

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
    
def pigltn_to_eng(text):
    words = text.split()
    english = ""
    
    for word in words:
        if len(word) == 1:
            english = english + word + " "
        elif word[-3:] == "way" and word[0] in "aeiou":
            word = word[0:-3]
            english = english + word + " "
        elif word[-3] not in "aeiou"  and word[0] in "aeiou" and word[-4:-2] not in double_consonants:
            word = word[-3] + word[0:-3]
            english = english + word + " "
        elif word[-4] not in "aeiou" and word[-3] not in "aeiou" and word[-4:-2] in double_consonants:
            word = word[-4] + word[-3] + word[0:-4]
            english = english + word + " "
            
    return english
        
print(eng_to_pigltn(text))

print(pigltn_to_eng(eng_to_pigltn(text)))