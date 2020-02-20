# Looping through items in a list using a "for loop"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# Defined the list at line 2 (magicians)
# At line 3 we define a for loop. This tells python to pull a name from the list magicians and associate with the variable "magician"
# At line 4 we print the variable "magician" which repeats for each item in the list "magicians"
# You can use any name you want for the temporary variable, however choosing a meaningful name will help reading the code

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a neat trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# You can write as many lines of code within the for loop
# Every indented line following the line "for magician in magicians:" is considered inside the loop
print("Thank you, everyone. That was a great show!")