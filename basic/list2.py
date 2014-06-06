#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  if len(nums) >= 2:
    count = 0
    returnlist = [nums[0]]
    for i in range(1,len(nums)):
      if nums[i] != nums[i-1]:
        returnlist.append(nums[i])
      else:
        continue
    return returnlist
  else:
    return nums;
  
def remove_adjacent_solution(nums):
  returnlist = []
  for num in nums:
    if len(returnlist) == 0 or num != returnlist[-1]:
      returnlist.append(num)
  return returnlist
  
# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  # +++your code here+++
  index1 = 0
  index2 = 0
  returnlist = []
  while index1 < len(list1) and index2 < len(list2):
      if list1[index1] < list2[index2]:
        returnlist.append(list1[index1])
        index1 += 1
      else:
        returnlist.append(list2[index2])
        index2 +=1
  if index1 == len(list1):
    returnlist += list2[index2:]
  if index2 == len(list2):
    returnlist += list1[index1:]
  return returnlist
  
def linear_merge_solution(list1, list2):
  returnlist = []
  while len(list1) and len(list2):
    if list1[0] < list2[0]:
      returnlist.append(list1.pop(0))
    else:
      returnlist.append(list2.pop(0))
      
  returnlist.extend(list1)
  returnlist.extend(list2)
  return returnlist

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'remove_adjacent'
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print 'remove_adjacent_solution'
  test(remove_adjacent_solution([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent_solution([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent_solution([]), [])  

  print
  print 'linear_merge'
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])

  print
  print 'linear_merge_solution'
  test(linear_merge_solution(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge_solution(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge_solution(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
