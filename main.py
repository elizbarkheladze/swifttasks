# N1
# def isPaindrom(text):
#     tolower = text.lower();
#     if tolower == tolower[::-1]:
#         return True
#     else:
#        return False
#
# print(isPaindrom("Radar"))
#N2
# def minSplit(amount):
#     change = [1,5,10,20,50]
#     size = 5
#     result = []
#     k = size - 1
#     while (k >= 0):
#         while amount >= change[k]:
#             amount -= change[k]
#             result.append(change[k])
#         k -= 1
#     return len(result)
#N3
# print(minSplit(320))
# def notContains(array):
#     array.sort()
#     minimum = 0
#     for i in range(0,len(array)-1):
#         if array[i] > 0:
#             minimum = array[i] - 1
#             break
#     if minimum == 0:
#         return "there is no minimal number"
#     else:
#         return minimum
#
# print(notContains([5,2,3,145,5,4,2,5,7,61]))
#
#N4
# def isProperly(text):
#     char1 = '('
#     char2 = ")"
#     char1count = 0
#     char2count = 0
#     for char in text:
#         if char == char1:
#             char1count += 1
#         elif char == char2:
#             char2count += 1
#
#     if text[0] == ')' or text[-1] == '(':
#         return False
#     elif char1count == char2count:
#         return True
#     else:
#         return False
# print(isProperly("()(asdasdasd))("))

#N5
# def countVariants(stearsCount):
#     if (stearsCount == 1 or stearsCount == 0):
#         return 1
#     elif (stearsCount == 2):
#         return 2
#     else:
#         return countVariants(stearsCount-2)+countVariants(stearsCount-1)
# print(countVariants(4))
#მეექვსე ამოცანის პირობა ვერ გავიგე