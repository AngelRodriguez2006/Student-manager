import os

archive = "carpeta.txt"

#This part of the code basically veryfies if the given archive exists and if it does it reads its content and 
#Appends all the content to the list called archive content, this happens everytime the code is runned
if os.path.exists(archive):
    with open(archive, "r", encoding="utf-8") as archive_info:
        archive_content = [lines.strip() for lines in archive_info.readlines()]
    size = os.path.getsize(archive)
        
else:
    print("Archive was not fount")

#Here we read the code to get its info, like how many characters it has, lines and words

with open(archive, "r", encoding="utf-8") as archive_info:
    characters = len(archive_info.read())
    archive_info.seek(0)
    lines = len(archive_info.readlines())
    archive_info.seek(0)
    words = archive_info.read()
    split_words = len(words.split())



#This function is the one in charge of displaying all of the data from the archive
def show_archive_data ():

    if os.path.getsize(archive) <= 0:
        print("The archive is empty")

    else:

    
     size_calculation = (f"{str(size)}-Bytes")

     print(f"Lines: {lines}")
     print(f"Characters: {characters}")
     print(f"Words: {split_words}")
     print(f"Size: {size_calculation}" )

#This one is in charge of looking for the word that is repeated the most in the text archive
def most_repeated_word ():
    if os.path.getsize(archive) <= 0:
        print("The archive is empty")
    
    else:

     repeated_words = []
     splitted_words = []

     for words in archive_content:
        splitted_words.extend(words.split())
        

     for word in splitted_words:

        count = splitted_words.count(word)

        repeated_words.append({"Word": word, "Times":count })

        most_repeated = max(repeated_words, key=lambda x: x["Times"] )

     print(f"Word: {most_repeated["Word"]}")
     print(f"Times: {most_repeated["Times"]}")

     

print("Loading menu")

while True:

    print("-Menu-")

    options = input("Option 1 = Show archive data, option 2 = Show most repeated word in archive, option 3 = exit. =")

    if options == "1":
        show_archive_data()
    elif options == "2":
        most_repeated_word()
    elif options == "3":
        print("Closing menu...")
        break
    
    

    

        
    
        

        
        
        

  






