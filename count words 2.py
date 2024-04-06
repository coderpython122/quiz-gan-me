def counter(a): 
  if not a.strip():#if word has no  whitespace return 0
     return 0
  d=a.strip()# replace single white space to empty space
  return len(a)


def main(): #main function 
    q=input("enter the words:")# get the input 
    o=counter(q)# to get the function like replace or len by declaring a variable as o  
    print("there are ",o,"in the given sentence")



if __name__ == "__main__":
    main()