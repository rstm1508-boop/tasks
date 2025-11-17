# # Task 1
# numbers = input().split()
# for num_str in numbers:
#     count = int(num_str)
#     print('+' * count)

# # Task 2 
# ip = input().strip()
# parts = ip.split('.')
# if len(parts) != 4:
#     print("NO")
# else:
#     valid = True
#     for part in parts:
#         if not part:
#             valid = False
#             break
        
#         if not part.isdigit():
#             valid = False
#             break
        
#         num = int(part)
        
#         if num < 0 or num > 255:
#             valid = False
#             break
        
#         if len(part) > 1 and part[0] == '0':
#             valid = False
#             break
    
#     print("YES" if valid else "NO")

# # Task 3
# text = input()
# separator = input()
# result = separator.join(text)
# print(result)

# # Task 4
# text = input()
# numbers = text.split()
# numbers = [int(num) for num in numbers]
# ascending = sorted(numbers)
# descending = sorted(numbers, reverse=True)


# print("По возрастанию:", ascending)
# print("По убыванию:", descending)

# # Task 5
# text = input().strip()
# words = text.split()
# max_length = max([len(word) for word in words]) if words else 0
# print(max_length)

# # Task 7

# numbers = list(map(int, input().split()))

# count = 0
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             count += 1

# print(count)

# # Task 8
# a = int(input())
# b = int(input())

# max_sum = 0
# result_num = 0

# for num in range(a, b + 1):
#     divisor_sum = 0
#     for divisor in range(1, num + 1):
#         if num % divisor == 0:
#             divisor_sum += divisor
#     if divisor_sum >= max_sum:
#         max_sum = divisor_sum
#         result_num = num

# print(result_num, max_sum)
