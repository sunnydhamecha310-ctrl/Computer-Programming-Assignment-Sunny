import random


def get_total(grade_list):

    return sum(grade_list)


def get_average(grade_list, total_sum):
    
    if not grade_list:
        return 0
    
    return total_sum / len(grade_list)

def main():
    grades = [] 
    
    
    
    while True:
        user_input = input("Please enter a grade or -1 to stop): ")

        if user_input == "-1":
            break

        try:
            grade = int(user_input)
            grades.append(grade)
        except ValueError:
            print("Please enter a valid whole number.")
            
    print("\nGrades:", grades)

    
    print("\nRemoving the Lowest Grade")
    if grades:
        
        lowest = min(grades)
        
        index = grades.index(lowest)
     
        grades.pop(index)
        print(grades)
    else:
        print("Grades list is empty.")

  
    print("\nRemoving a Random Grade")
    if grades:
        
        random_grade = random.choice(grades)
        
        grades.remove(random_grade)
      
        print(grades)
    else:
        print("Grades list is empty.")

  
    print("\nEdit a Grade")
    if grades:
        
        for i, grade in enumerate(grades, start=1):
            print(f"{i}. {grade}")

        while True:
            try:
               
                choice = int(input("Please enter the number of the grade you would like to change: "))
                
                if 1 <= choice <= len(grades):
                    break
                else:
                    print("That number is not right. Please try again.")
            except ValueError:
                 print("Please enter a whole number.")

        try:
            new_grade = int(input("Please enter the new grade: "))
         
            grades[choice - 1] = new_grade
            print("Grades after editing:", grades)
        except ValueError:
            print("Invalid grade entered. Grade not updated.")
    else:
        print("Grades list is empty. Cannot edit.")
        

    print("\nSorting and Reversing Grades")
    grades.sort()
    grades.reverse()
    print("Sorting and Reversing Grades:", grades)

   
    print("\nGetting Total and Average")
    
   
    total = get_total(grades) 
    print("Total:", total)
    
    average = get_average(grades, total)
    print("Average:", average)


    print("\nCompleted by, Shivang Dhamecha")

if __name__ == "__main__":
    main()
