# Write file
f = open('data.txt', 'w')
f.write("Hi, I am Supraja Writing this file, "
        "This content was written using Python.\n Welcome to file handling!")
f.close()
print("Successfully created 'data.txt' and wrote content to it.")

# Read file
f = open('data.txt', 'r')
data = f.read()
print(data)
f.close()