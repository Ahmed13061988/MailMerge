# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
invites = []
with open("Input/Names/invited_names.txt") as name:
    for person in name:
        names.append(person.replace('\n', ' '))

print(names)


with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
    for name in names:
        invite = content.replace('[name]', name)
        invites.append(invite)

for invite in invites:
    with open(f"Output/ReadyToSend/example.txt", mode="w") as file:
        final = file.write(invite)


