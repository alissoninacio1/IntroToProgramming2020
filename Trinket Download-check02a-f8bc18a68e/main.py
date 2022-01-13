def prompt_user():
  num_checked = -1
  
  while num_checked < 0:
    positive_num = int(input("Enter a positive number: ")) #converting in int directly
    num_checked = positive_num 
    if num_checked < 0:
      print("Invalid entry. The number must be positive.")
  print() #only to get a new blank line
  return num_checked

def compute_sum(x, y, z):
  return (x + y + z)


def main():
  a_num = prompt_user()
  b_num = prompt_user()
  c_num = prompt_user()
  soma = compute_sum(a_num, b_num, c_num)
  print("The sum is: {}".format(soma))


if __name__ == "__main__":
  main()