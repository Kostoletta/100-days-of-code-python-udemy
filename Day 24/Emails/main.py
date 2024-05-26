# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt", mode="r") as og:
    starting_letter = og.read()

with open("Input/Names/invited_names.txt", mode="r") as f_names:
    names = f_names.readlines()

for name in names:
    with open(f"Output/ReadyToSend/{name.strip().replace(' ', '_')}.txt", mode="w") as f_letter:
        f_letter.write(starting_letter.replace("[name]", f"{name.strip()}"))
