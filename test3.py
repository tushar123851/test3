print("Welcome To Pattern Generator And Number Analyer!")

while True:
    print("Select an option:")
    print("1. Generate pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

    choice = input("enter your choice:")

    match choice:
        case "1":
            
            
            print("Choose a pattern type:")
            print("1. Right angled Tringle")
            print("2. pyramid")
            print("3. Left angled Tringle")

            pattern_choice = input("enter your choice:")

            match pattern_choice:

             case "1":
                  break
             case "2":
                    break
             case "3":
                    break
             case "4":
                   print("exit")
             
        case "2":
              sum = 0
              start_range = int(input("Enter the start of range:"))

              end_range = int(input("Enter the end of range:"))

              for number in range(start_range,end_range):
                   if number % 2 == 0:
                        print(f"Number is {number} Even")
                   else:
                        print(f"Number is {number} Odd")
                   sum +=number
              
              print(f"Sum of all numbers from {start_range} to {end_range}:{sum}")
    

        case "3":
              print("Exiting Program.GoodBye!") 
              break

        case _:
            print("Invalid choice. Please enter a valid option.")
              


             
