WordTosplit = input("Enter your input")

def split_input(user_input: str):
    for char in user_input:
        if user_input.isdigit():
            [int(user_input) for user_input in str(user_input)]
        if user_input.isalpha():
            [str(user_input)]

for c in WordTosplit:
    numb = 0
    char = 0
    if c.isalpha():
        numb += 1
    if c.isdigit():
        char += 1
def mixed_data(user_input):

if char > 0 and numb > 0:
    print(WordTosplit)
def char_only(WordTosplit):
    if char > 0 and numb == 0:
        print(WordTosplit)
def numb_only(WordTosplit):
if numb > 0 and char == 0:
    print(f"you need to walk {WordTosplit} steps")


