# Get valid input for the height
while True:
  try:
    height = int(input("Height: "))
    if height > 0:
      break
    else:
      print("Please enter a positive integer.")
  except ValueError:
    print("Invalid input. Please enter an integer.")

# Loop to print the pyramid
for row in range(height):
  spaces = height - 1 - row
  hashes = row + 1
  print(" " * spaces + "#" * hashes)
