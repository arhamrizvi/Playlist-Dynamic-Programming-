array = []
#word = []

def readFile(name):
    file = open(name)
    file = file.read()
    var = file.splitlines()

    for line in range(len(var)):
        if line%2 != 0:
            word = var[line].split(' ')

    for i in range(len(word)):
        word[i] = int(word[i])
        array.append(word[i])
    return array


print(readFile('songs.txt'))



user = int(input("Enter trip length: "))

#array = [10, 3, 5, 7, 2]
# array = [2,3,7,8,10]

n = len(array)



try:
    #Creates a list containing 6 rows, each of 12 columns, all set to False
    Matrix = [[False for x in range(user + 1)] for y in range(n + 1)]

    for i in range(n + 1):  # first column filled with True
        Matrix[i][0] = True

    for i in range(1, n + 1):  # n=5
        for j in range(1, user + 1):  # user=11
            if j - array[i - 1] < 0:  # if less than 0
                # make the current value equal to the value above it
                Matrix[i][j] = Matrix[i - 1][j]
            if j - array[i - 1] >= 0:  # if greater than or equal to 0
                # make the current value equal to either the the value above it or the value which you get when you subtract it from the main array
                #if it's False and False, it'll remain False (as False or False = False)
                #if it's True and False, it'll become True (as True or False = True)
                Matrix[i][j] = Matrix[i - 1][j] or Matrix[i - 1][j - array[i - 1]]

    back = []
    ID = []

    i = n
    j = user
    while i != -1 and j != 0:
        if Matrix[i][j] == True:
            i -= 1
        else:
            back.append(array[i])
            ID.append(i + 1)
            j = j - array[i]

    new = []
    dur = []
    for i in range(len(ID) - 1, -1, -1):
        new.append(ID[i])
        dur.append(back[i])

    for i in range(len(ID)):
        print("ID: " + str(new[i]) + " Duration: " + str(dur[i]))

except:
    print("Bad luck Alice")
