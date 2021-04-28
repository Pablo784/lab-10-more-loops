maximum_stories = 100
usernum = input("On what floor of the building is your office?")
while int(usernum) > maximum_stories:
	usernum = input("You entered: " + str(usernum) + ". But there are only " + str(maximum_stories) + " floors in this building. Try again... ")
print("Congratulations! You work on floor: " + str(usernum))

# I was really struggling on figuring out how to put the code together so I consulted a classmate for help. 