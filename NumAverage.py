def main():
    numbersfile = open(input("Enter text file:"),'r')

    total = 0
    numOfLines = 0
    line = numbersfile.readline()

    while line !="":
        numOfLines += 1
        total += int(line)
        line = numbersfile.readline()
    average = total / numOfLines

    print("The average is", average)


main()
