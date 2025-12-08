def get_user_string(message):
    return input(message)

def check_for_substring(main_s, sub_s):
    print("\nsearching for substring within the main string content, please wait!")
    
    start_index = main_s.find(sub_s)
    
    if start_index != -1:
        print(f"'{sub_s}' was found in the main string at index {start_index}.")
        return start_index
    else:
        print("substring was not found.")
        return -1

def handle_replacement(original_s, sub_s):
    print("\ninitiating the string replacement process!")
    
    while True:
        answer = input(f"do you want to replace '{sub_s}' with something else (y/n)? ").lower()
        
        if answer == "n":
            print("\nno replacement made.")
            return original_s
        
        elif answer == "y":
            new_sub_s = get_user_string("enter the replacement string: ")
            updated_s = original_s.replace(sub_s, new_sub_s)
            
            print(f"new string: {updated_s}")
            return updated_s
        
        else:
            print("invalid entry. please type 'y' or 'n'.")

def main():
    print("welcome to the string replacement tool!")
    
    main_string = get_user_string("enter the string to search through: ")
    sub_string = get_user_string("enter the string to search for: ")
    
    index_result = check_for_substring(main_string, sub_string)
    
    if index_result != -1:
        handle_replacement(main_string, sub_string)
    
    print("\nthank you for using our program!")

if __name__ == "__main__":
    main()
    
    print("completed by Shivang Dhamecha")