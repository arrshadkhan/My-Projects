print("\n\n\n\tWelcome to Sentence Analysis :) ")
print("-----------------------------------------------\n")
Sentence = input("Enter the Sentence: ")
print("Entered Sentance:- ", Sentence)
print("\n-----------------------------------------------\n")

current_word = ""
total_words = 0
total_words_list = []
shortest_word = ""
longest_word = ""
total_character_withspace = 0
total_character_withspace_storedList = []
total_character_withoutspace = 0
total_character_withoutspace_list = []
total_upper_case = 0
total_upper_case_list = []
total_lower_case = 0
total_lower_case_list = []
special_character = 0
special_character_list = []
total_num = 0
total_num_list = []
total_space = 0
even_num = 0
even_num_list = []
odd_num = 0
odd_num_list = []
prime_num = 0
prime_num_list = []
non_prime = 0
non_prime_list = []
vowel = 0
vowel_list = []
consonent = 0
consonent_list = []

for i in Sentence:
    total_character_withspace_storedList.append(i)
    total_character_withspace += 1  # TOTAL WORDS

    if i != " ":
        total_character_withoutspace_list.append(i)
        total_character_withoutspace += 1  # TOTAL WORDS WITHOUT SPACE
    if i in " ":
        total_space += 1

    if i != " ":  # TOTAL WORDS COUNT
        current_word += i
    else:
        if current_word != "":
            total_words_list.append(current_word)
            total_words += 1
            current_word = ""
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        if i in "aeiouAEIOU":
            vowel_list.append(i)
            vowel += 1
        else:
            consonent_list.append(i)
            consonent += 1
    if i >= "a" and i <= "z":
        total_lower_case_list.append(i)
        total_lower_case += 1  # TOTAL LOWER CASE CH
    if i >= "A" and i <= "Z":
        total_upper_case_list.append(i)
        total_upper_case += 1  # TOTAL UPPER CASE CH
    if i in "!@#$%^&*()-+_=~?/\}|{:;><,.[]":  # SPECIAL CHARACTER
        special_character_list.append(i)
        special_character += 1
    if i in "0123456789":
        total_num_list.append(i)
        total_num += 1  # TOTAL NUMBERS IN SENTANCE
        num = int(i)  # EVEN ODD
        if num % 2 == 0:
            even_num_list.append(num)
            even_num += 1
        else:
            odd_num_list.append(num)
            odd_num += 1
        is_prime_no = True  # PRIME NON PRIME
        if num < 2:
            is_prime_no = False
        elif num == 2:
            is_prime_no = True
        elif num % 2 == 0:
            is_prime_no = False
        else:
            divisor = 3
            while divisor < num:
                if num % divisor == 0:
                    is_prime_no = False
                    break
                divisor = divisor + 2
        if is_prime_no:
            prime_num_list.append(num)
            prime_num += 1
        else:
            non_prime_list.append(num)
            non_prime += 1

# FOR LAST WORD COUNT
if current_word != "":
    total_words_list.append(current_word)
    total_words += 1

#FOR SHORT AND LONG WORD
if total_words > 0:
    shortest_word = total_words_list[0]
    longest_word = total_words_list[0]
    longest_len = 0
    for char in longest_word:
        longest_len += 1
    shortest_len = longest_len
    for word in total_words_list:
        word_len = 0
        for char in word:
            word_len += 1

        if word_len > longest_len:
            longest_word = word
            longest_len = word_len
        if word_len < shortest_len:
            shortest_word = word
            shortest_len = word_len

# SENTANCE TYPE
if Sentence:
    last_char = Sentence[-1]
    if last_char == "?":
        Sentence_type = "Question"
    elif last_char == "!":
        Sentence_type = "Exclamation"
    else:
        Sentence_type = "Statement"
else:
    Sentence_type='Empty Sentence'

print("\n============== ANALYSIS RESULTS ==============\n")

print('\nWORDS')
print(f"  Total words: {total_words}")
print(f"  Words: ", end=""); print(*total_words_list)
print(f"  Shortest:  {shortest_word}")
print(f"  Longest:  {longest_word}")
print(f"  Sentence Type:  {Sentence_type}")

print('\nLETTERS')
print(f"  Uppercase:  {total_upper_case}-> ",end='');print(*total_upper_case_list)
print(f"  Lowercase:  {total_lower_case}-> ",end='');print(*total_lower_case_list)
print(f"  Vowels:   {vowel}-> ",end='');print(*vowel_list)
print(f"  Consonents:  {consonent}-> ",end="");print(*consonent_list)

print("\nNUMBERS")
print(f"  Total:  {total_num}->  ",end='');print(*total_num_list)
print(f"  Even:   {even_num}->  ",end='');print(*even_num_list)
print(f"  Odd:    {odd_num}->  ",end='');print(*odd_num_list)
print(f"  Prime:  {prime_num}->  ",end='');print(*prime_num_list)
print(f"  Non-Prime: {non_prime}->  ",end='');print(*non_prime_list)

print('\nCHARACTER')
# print("Total Words:-  ",total_character_withspace_storedList) ALSO WORK
print(f"  Total: {total_character_withspace}->  {" ".join(total_character_withoutspace_list)}")
print(f"  Without Space: {total_character_withoutspace}-> ",end='');print(*total_character_withoutspace_list)
print(f"  Spaces: {total_space}")
print(f"  Special Characters: {special_character}-> ",end='');print(*special_character_list)

print('\n'+'=' * 50 )