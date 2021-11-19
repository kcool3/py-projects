last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print(gradebook)
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
gradebook[-1][-1] = 98
print(gradebook)
gradebook.remove(gradebook[2])
gradebook.append(["poetry", "Pass"])
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)