#########################################################################
#
#       Hello this program is the first program I will use to prove Git 
#       Im exiting for learn more about programming and this is one of 
#       the things I need to know how it works, to share and work on team
#
#       NUM OF VERSION --I DONT HAVE FUCKIN IDEA
#       so... here we go
#
#########################################################################

def getForm(nameFile: str):
    file = open(nameFile)
    return file.read()

text = getForm("heartForm.txt")

print(text)

