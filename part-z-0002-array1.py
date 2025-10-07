import array as arr

year_array = arr.array("i", [2000, 1990, 2026])

#year_array.append("2025") # TypeError: 'str' object cannot be interpreted as an integer

year_array.append(2025)

print(year_array[3])
