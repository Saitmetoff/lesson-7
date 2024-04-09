"""1"""

# my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# sorted_values = sorted(my_dict.values())
# print(sorted_values)


"""2"""

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# combined_dict = {**dic1, **dic2, **dic3}
# print(combined_dict)


"""3"""

# n = 15
# result_dict = {i: i**2 for i in range(1, n+1)}
# print(result_dict)

"""4"""

# my_dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# total_sum = sum(my_dict.values())
# print(total_sum)

"""5"""

# max_value = max(my_dict.values())
# print(max_value)


"""6"""

# min_value = min(my_dict.values())
# print(min_value)


"""7"""

# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'a': 300, 'b': 200, 'd': 400}
# combined_dict = {}
# for key in set(d1) | set(d2):
#     combined_dict[key] = d1.get(key, 0) + d2.get(key, 0)
# print(combined_dict)


"""8"""

# my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# unique_values = set()
# for d in my_list:
#     for value in d.values():
#         unique_values.add(value)
# print(unique_values)


"""9"""

# word = "assalom"
# char_count = {}
# for char in word:
#     char_count[char] = char_count.get(char, 0) + 1
# for char, count in char_count.items():
#     print(f"{char} {count} ta")

"""10"""

# text = "mexanizasiyalashtirilganmi"
# char_count = {}
# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1
# most_common_char = max(char_count, key=char_count.get)
# least_common_char = min(char_count, key=char_count.get)
# print(f"Eng ko'p ishlatilgan harf: {most_common_char}")
# print(f"Eng kam ishlatilgan harf: {least_common_char}")

"""11"""

krill_word = "салом"

transliteration_dict = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'j',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'x', 'ц': 'ts',
    'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu',
    'я': 'ya'
}

lotin_word = ''.join(transliteration_dict.get(char, char) for char in krill_word)
print(lotin_word)

"""12"""

lotin_word = "salom"

reverse_transliteration_dict = {v: k for k, v in transliteration_dict.items()}
krill_word = ''.join(reverse_transliteration_dict.get(char, char) for char in lotin_word)
print(krill_word)

