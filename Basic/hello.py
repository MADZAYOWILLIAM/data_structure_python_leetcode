"""STRING MERGING"""
class Solution:
    """Merge two strings by alternating characters from each."""
    def mergeAlternately(slef,first_word:str,second_word:str):
        merged_output=[]
        min_len_word=min(len(first_word),len(second_word))

        for i  in range(min_len_word):
            merged_output.append(first_word[i])
            merged_output.append(second_word[i])

        if len(first_word)>len(second_word):
            merged_output.append(first_word[min_len_word:])
        elif len(second_word)>len(first_word):
            merged_output.append(second_word[min_len_word:])

        return ''.join(merged_output)

        

