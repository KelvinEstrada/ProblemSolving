# Given an encoded string as example: 3[a]2[b] where the number indicates the number
# of decoding to be performed on the following string. Return the decoded string.
# 3[a]2[b] must return aaabb
# 2[abc]3[cd]ef must return abcabccdcdcdef
def decodeString(s):
  nums = []
  chars = []
  temp = ""
  decoded = ""
  i = 0

  while i < len(s):
    if s[i].isdigit():
      number = 0
      while s[i].isdigit():
        number = number * 10 + int(s[i])
        i += 1
      nums.append(number)
    
    if s[i].isalpha() or s[i] == "[":
      chars.append(s[i])

    if s[i] == "]":
      if len(nums) > 0:
        n = nums.pop()
      while chars[-1] != "[":
        temp = chars.pop() + temp
      chars.pop()
      temp *= n
      
      for letter in temp:
        chars.append(letter)
      temp = ""
    i += 1

  while len(chars) != 0:
    decoded = chars.pop() + decoded
  return decoded 
