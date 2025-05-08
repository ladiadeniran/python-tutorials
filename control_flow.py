

def print_age(name: str, a: int, gender: str):
  if a < 18:
    print(f"{name} is a minor")
  elif a == 18:
    print(f"{name} is just about an adult")
  else:
    print(f"{name} is an adult")
    print(f"{name} is a {gender}")
  print("------------------------")


if __name__ == "__main__":
  print_age("ladi", 17, "male") # ladi is a minor
  print_age("ladi", 18, "male") # ladi is just about an adult
  print_age("ladi", 19, "male") # ladi is an adult, ladi is  a male
