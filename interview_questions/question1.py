
"""
# Function to remove duplicates from a string
(Note: Feel free to use python builtin functions)
"""

def remove_duplicates(s):
   # final_list = []
   # for str in s:
   #    if str not in final_list:
   #       final_list.append(str)
   # return final_list
   str = ""

   for i in s:
      if i not in str:
         str = str + i
   return str


if __name__ == '__main__':
    case1 = remove_duplicates('hello')
    print(case1)
    case1 == 'helo'
    case2 = remove_duplicates('icecream sandwitch is good good')
    print(case2)
    case2 == 'iceram sndwthgod'
    print('Success')
