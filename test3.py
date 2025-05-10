# Welcome message
print("Welcome To Pattern Generator And Number Analyer!")

# Infinite loop for menu
while True:
     # Display menu options
    print("\n")
    print("Select an option:")
    print("1. Generate pattern")
    print("2. Analyze a range of numbers")
    print("3. Exit")

     # Take user input for menu choice
    choice = input("enter your choice:")

    match choice:
      # Option 1: Display Pattern according user choose 
      # 1.right angled tringle 
      # 2.pyramid 
      # 3.Left angled tringle 

        case "1":
            
            
            print("Choose a pattern type:")
            print("1. Right angled Tringle")
            print("2. pyramid")
            print("3. Left angled Tringle")

            pattern_choice = input("enter your choice:")
 
            match pattern_choice:

             case "1":
                rows = int(input("Enter number of rows for pattern:"))
                print("\n")
                print("pattern:")
               
                for i in range(1,rows+1):
                 print("*  " * i)
              
             case "2":
                rows = int(input("Enter number of rows for pattern:"))
                print("\n")
                print("pattern:")
                

                for i in range(1,rows + 1):
                  print(" " * (rows - i) + "* "*i)
                  
                  
             case "3":
                rows = int(input("Enter number of rows for the pattern: "))
                print("\nPattern:")

                for i in range(1, rows + 1):
                    print(" " * (rows - i), end="")
                    print("*" * i)

                  
                  
                
      # Option 2:display even and odd number
      #display sum
  
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
    
     # Option 3: exit message
        case "3":
              print("Exiting Program.GoodBye!") 
              break
        
     # Invalid input
        case _:
            print("Invalid choice. Please enter a valid option.")
              


             



             
