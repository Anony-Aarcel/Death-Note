def process_temperatures(temp_list):
    """
    Process a list of temperatures and return the maximum, minimum, and mean temperatures.

    Args:
        temp_list (list): A list of temperature strings (e.g., "36.5C", "37.2C", etc.)

    Returns:
        dict: A dictionary containing the maximum, minimum, and mean temperatures.
    """

    # Remove the 'C' suffix from each temperature string and convert to float
    temperatures = [float(temp.replace('C', '')) for temp in temp_list]

    # Calculate the maximum, minimum, and mean temperatures
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)

    # Return the results as a dictionary with rounded values
    return {
        'max': round(max_temp, 2),
        'min': round(min_temp, 2),
        'mean': round(mean_temp, 2)
    }


# Example usage
system_temperatures = ["36.5C", "37.2C", "35.8C", "39.0C", "38.4C"]
result = process_temperatures(system_temperatures)

# Print the results
print(f"Maximum Temperature: {result['max']}°C")
print(f"Minimum Temperature: {result['min']}°C")
print(f"Mean Temperature: {result['mean']}°C")
