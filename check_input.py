def get_int(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is an integer.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    The valid positive integer input.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be an integer.")
  return val


def get_positive_int(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is a positive (>= 0) integer.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    The valid integer input.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= 0:
        valid = True
      else:
        print("Invalid input - should not be negative.")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val  


def get_int_range(prompt, low, high):
  """Repeatedly takes in and validates user's input to ensure that it is an integer within the specified range.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
    low: lower bound of range (inclusive)
    high: upper bound of range (inclusive)
  Returns:
    The valid integer input within the specified range.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = int(input(prompt))
      if val >= low and val <= high:
        valid = True
      else:
        print("Invalid input - should be within range " + str(low) + "-" + str(high) + ".")
    except ValueError:
      print("Invalid input - should be an integer.")
  return val


def get_float(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is a float.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    The valid floating point input.
  """
  val = 0
  valid = False
  while not valid:
    try:
      val = float(input(prompt))
      valid = True
    except ValueError:
      print("Invalid input - should be a decimal value.")
  return val


def get_yes_no(prompt):
  """Repeatedly takes in and validates user's input to ensure that it is a yes or a no answer.
  Args:
    prompt: string to display to the user to prompt them to enter an input.
  Returns:
    True if yes, False if no.
  """
  valid = False
  while not valid:
    val = input(prompt)
    if val == "YES" or val == "Yes" or val == "yes" or val == "Y" or val == "y":
      return True
    elif val == "NO" or val == "No" or val == "no" or val == "N" or val == "n":
      return False
    else:
      print("Invalid input - should be a 'Yes' or 'No'.")
