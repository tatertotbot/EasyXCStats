def getCredentials():
    global email
    global password
    global userID

    #opens file and read content
    credentials = open('credentials.txt', 'r')
    content = credentials.readlines()

    #sets lines to variables
    email = content[0].strip('\n')
    password = content[1].strip('\n')
    userID = content[2].strip('\n')
