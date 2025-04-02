def temp_again():
    temperatures = []
    
    while True:
        input_temp = input("Enter a temperature (e.g., 36.5C) or press Enter to finish: ")
        
        if input_temp.strip() == "":
            break
        
        try:
            temp_value = float(input_temp)
            temperatures.append(temp_value)
        except ValueError:
            print("Invalid input! Please enter a valid temperature (e.g., 36.5C).")
    
    if len(temperatures) == 0:
        print("No valid temperatures entered.")
        return
    
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    
    print(f"Maximum Temperature: {max_temp:.2f}°C")
    print(f"Minimum Temperature: {min_temp:.2f}°C")
    print(f"Mean Temperature: {mean_temp:.2f}°C")

# Call the function
temp_again()
