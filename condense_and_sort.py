# Given a list of repeated values, condense the list and sort the values by their
# frequency in the list. 
def condense_and_sort_list(lst):
  
  dic = {}
  for key in lst:
    if key not in dic:
      dic[key] = 1
    else:
      dic[key] += 1
  
  sortedList = sorted(sorted(dic.items()), key=lambda x:x[1], reverse=True)
  results = []
  for key,value in sortedList:
    results.append(key)
  return results
