# Imports math module in order to use math functions required in the solution
import math

# Display the menu for the user to choose between investment and bond
print("\t\t\t____________________________________________________________________________________")
print("\n\t\t\tinvestment  -  to calculate the amount of interest you'll earn on your investment")
print("\t\t\tbond        -  to calculate the amount you'll have to pay on a home loan\n")
print("\t\t\t____________________________________________________________________________________")

# Error handling for user input
while True:

    # Asks the user input and convert it to lowercase for case-insensitivity
    # And strip, in case there are spaces before and/or after string input
    user_input = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower().strip()
    
    if user_input.isalpha():
        
        # Check if the user chose 'investment'
        if user_input == "investment":
            
            # Error handling for principal amount input
            while True:
                
                try:
                    
                    principal_amount = float(input("\nPlease enter the amount you wish to invest(£): "))
                    break

                except Exception:
                    print("Please enter a valid numerical input!")
                    continue
            
            # Error handling for interest rate input
            while True:
                
                try:
                    
                    interest_rate = float(input("\nPlease enter what the interest rate you would like(%): ")) / 100
                    break

                except Exception:
                    print("Please enter a valid numerical input!")
                    continue

            # Error handling for years input
            while True:
                
                try:
                    
                    years = math.trunc(float(input("\nPlease enter number of years you wish to invest: ")))
                    break

                except Exception:
                    print("Please enter a valid numerical input!")
                    continue
            
            # Error handling for interest type value
            while True:
                
                # Asks interest input and convert it to lowercase for case-insensitivity
                # And strip, in case there are spaces before and/or after string input
                interest = input("\nPlease enter which interest type you would prefer('simple' or 'compound'): ").lower().strip()

                if interest.isalpha():
                
                    # Calculate and display results for simple interest
                    if interest == "simple":
                        tot_with_interest = round(principal_amount * (1 + interest_rate * years), 2)
                        print(f"\nYou will receive £{tot_with_interest} after {years} years at the simple interest rate of {interest_rate * 100: .2f}%\n")
                        exit()

                    # Calculate and display results for compound interest
                    elif interest == "compound":
                        tot_with_interest = round(principal_amount * math.pow((1 + interest_rate), years), 2)
                        print(f"\nYou will receive £{tot_with_interest} after {years} years at the compound interest rate of {interest_rate * 100: .2f}%\n")
                        exit()
                    
                    # Outputs if input is not satisfied
                    else:
                        print("\nPlease choose an interest type between 'simple' and 'compound'!")
                
                # Outputs if input is not satisfied
                else:
                    print("\nPlease choose an interest type between 'simple' and 'compound'!")

        
        # Check if the user chose 'bond'        
        elif user_input == "bond":
            
            # Error handling for home value input
            while True:
                 
                try:
                      
                    home_value = float(input("\nPlease enter the current value of your home(£): "))
                    break

                except Exception:
                    print("Please enter a valid numerical input!")
                    continue

            # Error handling for interest rate input
            while True:
                 
                try:
                        
                    interest_rate = float(input("\nPlease enter what the interest rate you would like(%): ")) / 100
                    break

                except Exception:
                    print("Please enter a valid numerical input!")
                    continue
            
            # Error handling for months input
            while True:
                 
                try:
                      
                    months = math.trunc(float(input("\nPlease enter number of months you wish to repay the bond: ")))
                    break

                except Exception:
                    print("Please enter a valid numerical input!")
                    continue

            # Calculate monthly interest rate and total repayment
            monthly_interest_rate = interest_rate / 12
            tot_repayment = round((monthly_interest_rate * home_value) / (1 - (1 + monthly_interest_rate) ** (- months)), 2)

            # Display the result of the bond calculation
            print(f"\nYou will have to repay £{tot_repayment} per month in {months} months with an interest rate of {interest_rate * 100: .2f}%\n")
            exit()

        # Outputs if input is not satisfied
        else:
            print("\nPlease choose between 'investment' or 'bond'!")
    
    # Outputs if input is not satisfied
    else:
        print("\nPlease choose between 'investment' or 'bond'!")
