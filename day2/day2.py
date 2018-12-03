from collections import Counter

def create_checksum(id_list):
    two_letter_occurences = 0
    three_letter_occurences = 0

    for id_string in id_list:
        duplicates = Counter(list(id_string))
        duplicates_counts = set(duplicates.values())
        if 2 in duplicates_counts:
            two_letter_occurences += 1
        if 3 in duplicates_counts:
            three_letter_occurences += 1

    return two_letter_occurences * three_letter_occurences

def test1():
    box_id_list = [
        'abcdef',
        'bababc',
        'abbcde',
        'abcccd',
        'aabcdd',
        'abcdee',
        'ababab'
    ]
    assert create_checksum(box_id_list) == 12


def find_common_box(box_id_list):
    for box_id in box_id_list:
        for other_box_id in box_id_list[box_id_list.index(box_id):]:
            diffenece_count = 0 
            similar_letters = []
            if len(box_id) != len(other_box_id):
                break
            for index in range(len(box_id)):
                if box_id[index] != other_box_id[index]:
                    diffenece_count += 1
                else:
                    similar_letters.append(box_id[index])
                if diffenece_count > 1:
                    break
            if diffenece_count == 1:
                return "".join(similar_letters)
    

def test2():
    box_id_list = [
        'abcde',
        'fghij',
        'klmno',
        'pqrst',
        'fguij',
        'axcye',
        'wvxyz'
    ]
    assert find_common_box(box_id_list) == 'fgij'

with open('day2input.txt') as f:
    box_id_list = [box_id.rstrip('\n') for box_id in f.readlines()]
    
#star 1
test1()
print(create_checksum(box_id_list))

#star 2
test2()
print(find_common_box(box_id_list))