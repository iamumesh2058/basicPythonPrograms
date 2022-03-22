my_list = [i for i in range(20)]
print(my_list)

def binary_search(my_list, l, r, key):
  m = int((l+r)/2)
  flag = 0
  if key == my_list[m]:
    flag = key
  elif key < my_list[m]:
    return binary_search(my_list, l, m-1, key)
  else:
    return binary_search(my_list, m+1, r, key)
  return flag


key = int(input("Enter a element to be searched : "))
flag = binary_search(my_list, 0, len(my_list), key)
if flag == 0:
  print("Item not found.")
else:
  print(f"Item found in location {flag+1}")