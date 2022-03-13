user_inputs = list(map(int, input("Enter two or more numbers: ").split()))
if len(user_inputs) < 2:
    print("YOU DID NOT ENTER AT LEAST TWO NUMBERS!")
else: 
    sum_total = 0
    for x in range(0, len(user_inputs)):
        sum_total += user_inputs[x]
    print("Total is: " + str(sum_total))