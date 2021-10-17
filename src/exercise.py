def main():
    #write your code below this line
    file_name = input("File?")
    lower = int(input("Lower bound?"))
    upper = int(input("Upper bound?"))
    count = 0
    try:
        f = open(file_name, "r")
        data = f.read().splitlines()
        for num in data:
            if (int(num) >= lower) and (int(num) <= upper):
                count += 1
        print("Numbers: " + str(count))
    except:
        print("Error")
if __name__ == '__main__':
    main()
