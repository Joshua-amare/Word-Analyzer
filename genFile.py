def genFile(name):
    return open(name, "w+")

def writeFile(f , content):
    f.write(content)
