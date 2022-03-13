user_sentence = input("Enter a sentence for repetition: ")
repeat_punishment = int(input("Enter the number of repetitions: "))
y = 0
with open('CompletedPunishment.txt', 'w') as x:
    while y < repeat_punishment:
        x.write(user_sentence + '\n')
        y += 1