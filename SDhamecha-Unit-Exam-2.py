import random

def create_new_employee(employees, ids, names):
    
    
    while True:
        employee_name = input("Please Enter Name: ").strip()
        
       
        all_existing_names_lower = [name.lower() for name in names]
        
        if employee_name.lower() in all_existing_names_lower:
            print("Name exists.")
        else:
            names.append(employee_name)
            break

    # Get ID 
    while True:
        employee_id = random.randint(1, 500)
        
        if employee_id not in ids:
            ids.append(employee_id)
            break
     
    new_employee_record = {
         
        'name': employee_name,
        'id': employee_id
    }
    
    employees.append(new_employee_record)
    print(f"ID: {employee_id}.")
    
    return new_employee_record

    

def display_employee_info(employee_record):
    
    output_message = (
        f"Employee: {employee_record['name']}, ID: {employee_record['id']}"
    )
    return output_message
    

def main():
    
    
    print("===================================")
    print("Organization Employee Log")
    print("===================================")
    
    
    employees = []
    used_IDS = []
    used_Name = []

    
    while True:
        
        try:
            num_to_add = int(input("\nHow many employess are you adding?: "))
            if num_to_add >= 0:
                break
            else:
                print("Must be 0 or more.")
        except ValueError:
            print("Invalid input.")

    
    for i in range(num_to_add):
        
        
        create_new_employee(employees,  used_IDS,  used_Name)

    
   
    if not employees:
        print("No employee added.")
    else:
        print("Created User Information:")
        
        for employee in employees:
            log_entry = display_employee_info(employee)
            print(log_entry)
            
            
    

    print("\n===================================")
    print("Completed by Shivang Dhamecha")
    print("===================================")

if __name__ == "__main__":
    main()
