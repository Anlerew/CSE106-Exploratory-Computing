word = input("Enter a word to be found: ")
file = open("PythonSummary.txt", "r")
string = file.read()
lowercased = string.lower()
print("The word occurs " + str(lowercased.count(word)) + " times")