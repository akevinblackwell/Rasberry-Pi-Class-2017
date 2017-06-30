fullname = raw_input("Enter Your Full Name ")

firstspace = fullname.find(" ",0)

firstname = fullname[0:firstspace]
#print("fname "+firstname)

secondspace = fullname.find(" ", firstspace+1)
middlename = fullname[firstspace+1:secondspace]

#print("mname "+middlename)

lastname = fullname[secondspace+1:]
#print("lname "+lastname)

initials = firstname[:1]
print("initials "+firstname[:1]+ middlename[:1]+ lastname[:1])

