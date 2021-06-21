# Get read file
readFile = open("removespace.txt", "r", encoding="utf8")

# Get write file
# Will append instead of overriding content
writeFile = open("removespace(new).txt", "a", encoding="utf8")
writeFile.write(readFile.read().replace(' ', '').replace('\n\n', '\n'))
