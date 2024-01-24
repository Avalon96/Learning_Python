astring = "Hello world!"
print("single quotes are ' '")

# String length
print(len(astring))

# First instance 
print(astring.index("o"))

print(astring.count("l"))

print(astring[3:7])
print(astring[3:-1])

# This prints the characters of string from 6 to 10 skipping one character.
# This is extended slice syntax. The general form is [start:stop:step].
print(astring[6:10:1])

# Reverse String
print(astring[::-1])

# Upper/Lower Case
print(astring.upper())
print(astring.lower())

# Boolean checker
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#Split with space
afewwords = astring.split(" ")