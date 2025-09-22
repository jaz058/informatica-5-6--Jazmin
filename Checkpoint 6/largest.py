def main():
    list_length = int(input("List length: "))
    number_list = []

    for number in range(list_length):
        list_element = int(input("Enter element: "))
        number_list.append(list_element)

    print(number_list)

    large_num =max(number_list)
    print("The largest number is:" ,large_num)

    file= open("largest.txt","a")
    file.write(f"{number_list}\n")
    file.close()


main()