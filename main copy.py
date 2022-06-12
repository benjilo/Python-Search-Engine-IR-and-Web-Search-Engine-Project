#Created by Benjamin
#Created on June 9, 2022 at 9:27 A.M.
import glob

#CurrentFile= open("Jan/aol.html")

#print(CurrentFile.read())
#print (glob.glob("Jan/*"))
ListofFiles= glob.glob("Jan/*.html")

PostHashMap= {"Docs": []}

for CurrentFileElement in ListofFiles:
    DirectoryName= CurrentFileElement[0:3]
    CurrentFileName= CurrentFileElement[4:]

    #print("Current File Name:", CurrentFileName)
    CurrentFile= open("./" + DirectoryName + "/" + CurrentFileName)
    PostHashMap["Docs"].append(CurrentFileName)

    FileContents= CurrentFile.read()

    #Configurations
    CurrentTagStatus= 0
    TagStatuses= {}
    Word= ""
    CurrentTags= []
    ReadableCharacterCountIndex= 0
    #print("The length of this document is: {}", len(FileContents))

    for Character in FileContents:
        #Dealing with opening tags
        #If a < sign is encountered.
        if (Character == '<'):
            CurrentTagStatus= 1
        elif (CurrentTagStatus == 1 and Character == '<' and Word == ""):
            CurrentTagStatus= 0
            ReadableCharacterCountIndex= ReadableCharacterCountIndex + 2
        elif (CurrentTagStatus == 1 and Character != '>' and Character != '<' and Character != '/' and
            (Character == ' ' or Character == '\n' or Character == '\t') and not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122)) and Word == ""):
            CurrentTagStatus= 0
            ReadableCharacterCountIndex= ReadableCharacterCountIndex + 2
        elif (CurrentTagStatus == 1 and Character != '>' and Character == '<' and Character != '/' and
            (Character != ' ' and Character != '\n' and Character != '\t') and not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122)) and Word != ""):
            CurrentTagStatus= 0
            ReadableCharacterCountIndex + len(Word) + 2
            PostHashMap[ReadableCharacterCountIndex - len(Word) - 1]= Word
            Word= ""
        elif (CurrentTagStatus == 1 and Character != '>' and Character != '<' and Character != '/' and
            (Character == ' ' or Character == '\n' or Character == '\t') and not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122)) and Word == ""):
            CurrentTagStatus= 0
            ReadableCharacterCountIndex= ReadableCharacterCountIndex + 2
        elif (CurrentTagStatus == 1 and Character != '>' and Character != '<' and Character != '/' and
            (Character != ' ' and Character != '\n' and Character != '\t') and
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            Word+= Character
        elif (CurrentTagStatus == 1 and Character != '>' and Character != '<' and Character != '/' and
            (Character == ' ' or Character == '\n' or Character == '\t') and not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122)) and Word != ""):
            CurrentTags.append(Word)
            TagStatuses[Word]= 1
            CurrentTagStatus= 2
            Word= ""
        elif (CurrentTagStatus == 1 and Character == '>' and Character != '<' and Character != '/' and
            (Character != ' ' and Character != '\n' and Character != '\t') and not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            TagStatuses[Word]= 3
            CurrentTags.append(Word)
            CurrentTagStatus= 3
            Word= ""
        elif (CurrentTagStatus == 2 and Character == '>' and Character != '<' and
            (Character != ' ' and Character != '\n' and Character != '\t') and not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            TagStatuses[Word]= 3
            CurrentTagStatus= 3
            Word= ""
        #Dealing with closing tags
        elif (CurrentTagStatus == 1 and Character == '/'):
            CurrentTagStatus= 4
        elif (CurrentTagStatus == 4 and Character != '>' and Character != '<' and
            (Character != ' ' and Character != '\n' and Character != '\t') and
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            Word+= Character
        elif (CurrentTagStatus == 4 and Character == '>' and Character != '<'):
            TagStatuses[Word]= 0
            if (Word in CurrentTags):
                CurrentTags.remove(Word)
            Word= ""
        #Dealing with text in between tags
        elif (len(CurrentTags) != 0 and TagStatuses[CurrentTags[len(CurrentTags) - 1]] == 3 and Character != '<' and
            Character != '>' and (Character != ' ' and Character != '\n' and Character != '\t') and
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            Word+= Character
            ReadableCharacterCountIndex+= 1
        elif (len(CurrentTags) != 0 and Word != "" and TagStatuses[CurrentTags[len(CurrentTags) - 1]] == 3 and Character != '<' and
            Character != '>' and (Character == ' ' or Character == '\n' or Character == '\t' or not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122)))):
            PostHashMap[ReadableCharacterCountIndex]= Word
            #print("Hash Map updated!")
            Word= ""
            ReadableCharacterCountIndex+= 1
        elif (len(CurrentTags) != 0 and Word == "" and TagStatuses[CurrentTags[len(CurrentTags) - 1]] == 3 and Character != '<' and
            Character != '>' and (Character == ' ' or Character == '\n' or Character == '\t') or not
            ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            ReadableCharacterCountIndex+= 1
        #Dealing with text outside of all tags
        elif (len(CurrentTags) == 0 and Character != '<' and Character != '>' and (Character != ' '
            and Character != '\n' and Character != '\t') and ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            Word+= Character
            ReadableCharacterCountIndex+= 1
        elif (Word != "" and len(CurrentTags) == 0 and Character != '<' and Character != '>' and (Character == ' '
            or Character == '\n' or Character == '\t') and not ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            PostHashMap[ReadableCharacterCountIndex - len(Word)]= Word
            Word= ""
            ReadableCharacterCountIndex+= 1
        elif (Word == "" and len(CurrentTags) == 0 and Character != '<' and Character != '>' and (Character == ' '
            or Character == '\n' or Character == '\t') and not ((ord(Character) >= 65 and ord(Character) <= 90) or (ord(Character) >= 97 and ord(Character) <= 122))):
            ReadableCharacterCountIndex+= 1
    if (Word != ""):
        PostHashMap[ReadableCharacterCountIndex - len(Word)]= Word
        Word= ""
    CurrentTags.clear()
    TagStatuses.clear()

OutputFile= open("Output.txt", "w")
for CurrentElementKey, CurrentElementValue in PostHashMap.items():
    #print(CurrentElementKey, CurrentElmentValue)
    #OutputFile.write(str(CurrentElement))
    print(f"{str(CurrentElementKey)}")
    print(f"{str(CurrentElementValue)}\n")
    OutputFile.write(f"{str(CurrentElementKey)}\n")
    OutputFile.write(f"{str(CurrentElementValue)}\n\n")