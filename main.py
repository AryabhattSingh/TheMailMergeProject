# Opening invites_name.txt file with read mode
# readlines() function will return a list. This list will contain each line(including new line
# character) as a list item
with open("Input/Names/invited_names.txt", mode="r") as file:
    names_list = file.readlines()

# For each name, we have to generate the invite email, hence the loop
for name in names_list:
    # Opening the file in read only mode
    with open("Input/Letters/starting_letter.txt", mode="r") as file:
        # All the text in the file read and stored in 'contents' variable
        contents = file.read()

    # Removing the '\n' from the current name in the loop iteration
    name = name.strip("\n")

    # Replacing the '[name]' from the starting_letter with actual name
    ready_to_send_mail = contents.replace("[name]",name)
    # Generating the file name for the current name in the loop iteration
    file_name = name + ".txt"

    # Opening the file_name in write mode. Write mode will create the file if it doesn't exist
    with open(f"Output/ReadyToSend/{file_name}", mode="w") as file:
        file.write(ready_to_send_mail)
