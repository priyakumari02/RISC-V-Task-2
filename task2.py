def list_of_integers_process(input_list):
    if len(input_list) % 10 != 0:
        raise ValueError("Input list size should be multiple of 10!!")
    
    output_list = [input_list[index] for index in range(len(input_list)) if (index+1) % 2 != 0 and (index+1) % 3 != 0]
    return output_list

def get_integer_list():
    while True:
        try:
            input_list = [int(x) for x in input("Input intgers seperated by space : ").split()]
            return input_list
        except ValueError:
            print("Enter valid list of Integers!!")

def main():
    try:
        input_list = get_integer_list()

        output_list = list_of_integers_process(input_list)

        print("List after removing items at positions which are multiples of 2 or 3:")
        print(output_list)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
