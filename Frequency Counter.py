name = input("Enter the name: ")


def letter_counter(word):
    count = 0
    for i in word:
        if i.isspace() == True:
            pass
        else:
            count += 1
    return(count)


print(letter_counter(name))

counter = {}
for i in name.split():
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1
print(counter)
