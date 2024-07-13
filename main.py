#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/Users/macintosh/Desktop/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()
    
names = [name.strip() for name in names]
    
print(names)

with open('/Users/macintosh/Desktop/Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r') as file: # Automatically closes a file
    template = file.read()
    
search_text = '[name]'

for name in names:
    new_letter = template.replace(search_text, name)
    output_path = f'/Users/macintosh/Desktop/Mail Merge Project Start/Output/ReadyToSend/letter_to_{name}.txt'
    print(new_letter)
    with open(output_path,'w') as file:
        file.write(new_letter)
    