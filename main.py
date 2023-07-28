def is_very_long(a):
  return len(a) > 10



def has_digit(a):
  return any(flag.isdigit() for flag in a)
def has_letters(a):
 return any(flag.isalpha() for flag in a) 
def has_upper_letters(a):
  return any(flag.isupper() for flag in a)
def has_lower_letters(a):
  return any(flag.islower() for flag in a)
def has_symbols(a):
  return any(not (flag.isdigit() or flag.isalpha())for flag in a)


def main():
  
  a=input()
  score=0
  combacks=[has_upper_letters,is_very_long,has_digit,has_letters,has_lower_letters,has_symbols]
  for comback in combacks:
    if comback(a):
      score=score+2
  print(score)

if __name__ == "__main__":
	main()