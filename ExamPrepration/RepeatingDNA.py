def repeating_DNA(sequence):
    repeating_sequence=[]

    for i in range(len(sequence-10)):
        current_sequence=sequence[i:i+10]

        for j in range(i+1, i+11):
            next_sequence=sequence[j:j+10]
            if next_sequence==current_sequence and current_sequence not in repeating_sequence:
                repeating_sequence.append(current_sequence)
                break

    return repeating_sequence
# todo 80/100 3:05 има друг вариант



