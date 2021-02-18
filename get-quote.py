import random

def primary():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 16
  rnd = random.randint(0,last)
  print("Print from quotes.txt")
  print(quotes[rnd], end='')
  print(" ")

  f = open("quotes_output.txt","a")
  f.write(quotes[rnd])
  f.close
  f = open("quotes_output.txt","r")
  print("Print from quotes_output.txt")
  print(f.read( ))
  f.close

if __name__== "__main__":
  primary()
