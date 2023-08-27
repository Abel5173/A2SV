num_cases = int(input())

for _ in range(num_cases):
    cuts, sentence = input().split()
    cuts = int(cuts)  
    if cuts == 0:
        print(sentence)
        continue
    elif len(sentence) < 4:
        print(sentence)
        continue
    rotated_sentence = sentence[::-1]
    remaining_length = len(rotated_sentence) * 3 // 4
    remaining_part = rotated_sentence[:remaining_length]
    final_output = remaining_part[::-1]

    print(final_output)
