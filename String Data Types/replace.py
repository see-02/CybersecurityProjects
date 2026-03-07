#Task 2:
# Follow these steps:
#   ● Create a new Python file in this folder called replace.py.
#   ● Save the sentence: “The!quick!brown!fox!jumps!over!the!lazy!dog.” as a
#   single string.
#   ○ Reprint this sentence as “The quick brown fox jumps over the lazy
#   dog.” using the replace() function to replace every exclamation
#   mark “!” with a blank space.
#   ○ Reprint that sentence as: “THE QUICK BROWN FOX JUMPS OVER
#   THE LAZY DOG.” using the upper() function.
#   ○ Reprint the sentence in reverse.
#*****************************************************************************

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# Process sentence without !
new_sentence = sentence.replace("!"," ")
print(new_sentence)

# Reprint sentence in all caps
print(new_sentence.upper())

# Reprint sentence in reverse
print(new_sentence[-1::-1])
