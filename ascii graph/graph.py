# UPDATED CODE 2
# Note:- The output graph may not display properly if the sum of the
#        input value exceeds the width limit of python console.


#
#         By - C S JITHEASH           #


def sumArr(arr):                            # Determine the total sum of the input
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum


def findPeak(arr, length):                  # To find peak value and it's index
    sum = 0
    global positivePeak
    positivePeak = 0
    global negativePeak
    negativePeak = 0
    tempsum = 0
    global peakIndex
    peakIndex = 0
    for i in range(0, length):
        if i % 2 == 0:
            sum += arr[i]
            tempsum += arr[i]
        else:
            sum -= arr[i]
            tempsum += arr[i]
        if sum > positivePeak:
            peakIndex = tempsum
            positivePeak = sum
        if sum < negativePeak:
            negativePeak = sum
    return positivePeak


def createMatrix(peakNum, inputSum):                        # Generate a 2-d matrix with blank space as value
    global tempPeak
    tempPeak = peakNum + abs(negativePeak)
    matrix = [[" "]*inputSum for i in range(tempPeak + 3)]
    return matrix


def printMatrix(matrix, peakNum, inputSum):                 # Print matrix
    for i in range(0, peakNum + 3):
        for j in range(0, inputSum):
            print(matrix[i][j], end="")
        print("")


def addChars(matrix, inputArr, length, peakNum):            # Add characters to the appropriate indexes
    linearCounter = 0                                       # To manage horizontal index (X-axis)
    positionCounter = peakNum + 2                           # To manage vertical index (Y-axis)
    flag = 1
    for i in range(0, length):
        if i % 2 == 0:
            for j in range(0, inputArr[i]):
                matrix[positionCounter][linearCounter] = '/'    # Even indexes of inputArr[]
                if positionCounter == 3 and flag == 1:
                    linearCounter += 1
                    flag = 0
                linearCounter += 1
                positionCounter -= 1
            positionCounter += 1
        else:
            for k in range(0, inputArr[i]):
                matrix[positionCounter][linearCounter] = '\\'   # Odd indexes of inputArr[]
                linearCounter += 1
                positionCounter += 1
            positionCounter -= 1
    matrix[0][peakIndex-1] = ' o'
    matrix[1][peakIndex-1] = '/|\\'
    matrix[2][peakIndex-1] = '< >'


inputString = input()                                   # Store input as string
inputArr = list(map(int, inputString.split(' ')))       # Convert string input to array
length = len(inputArr)                                  # Array length
inputSum = sumArr(inputArr) + 1                         # Sum of inputs to determine width of graph
peakNum = findPeak(inputArr, length)                    # Find the peak point in the graph
matrix = createMatrix(peakNum, inputSum)                # Generate blank matrix

addChars(matrix, inputArr, length, peakNum)             # Add characters to the matrix
printMatrix(matrix, tempPeak, inputSum)                  # Print matrix
