# my original idea made to work
def generate(upto):
  
  check = 1
  output = []

  while check <= upto:
    if check % 15 == 0: 
      output.append("FizzBuzz")
    elif check % 5 == 0:
      output.append("Buzz")
    elif check % 3 == 0:
      output.append("Fizz")
    else:
      output.append(str(check))
    check = check + 1
  return  ", ".join(output)

# mine and James
# def generate(upto):
#   nums = ""
#   num = 1
#   while num <= upto:
#     if num == 1:
#       nums = nums + str(num)
#     elif num % 3 == 0 and num % 5 == 0:
#       nums = nums + ', FizzBuzz'
#     elif num % 3 == 0:
#       nums = nums + ', Fizz'
#     elif num % 5 == 0:
#       nums = nums + ', Buzz'
#     else:
#       nums = nums + ', ' + str(num)
#     num = num + 1
#   return ''.join(nums)