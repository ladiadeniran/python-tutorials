import numpy as np

def play_with_np(a = [[1,2,3], [4,5,6]]):
  x = np.array(a, np.int32)
  print(type(x))
  print(x.shape)
  print(x.dtype)


if __name__ == "__main__":
  array1 = input("Enter a list of numbers separated by commas: ")
  array2 = input("Enter another list of numbers separated by commas: ")
  array3 = input("Enter another list of numbers separated by commas: ")
  play_with_np([array1.split(","), array2.split(","), array3.split(",")])
  # play_with_np()
