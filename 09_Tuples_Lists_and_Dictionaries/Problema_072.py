school_list = ["P.E.", "Math", "Biology", "Physics", "Social studies", "Chemistry"]
print(school_list)
subject = str(input("Which of this you want to get rid of?\n"))
school_list.remove(subject)
print("There you have it.")
print(school_list)