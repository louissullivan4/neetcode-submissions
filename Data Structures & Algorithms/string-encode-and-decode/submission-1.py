class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word)) + '!' + str(word)
        return encoded_string;

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        index = 0
        while index < len(s):
            # 1. find the '!' that ends the digits
            delim = index
            while s[delim] != '!':
                delim += 1
            # 2. digits are between index and delim
            number_of_letters = int(s[index:delim])
            # 3. word starts right after '!'
            start_of_word_index = delim + 1
            end_of_word_index = start_of_word_index + number_of_letters
            decoded_strings.append(s[start_of_word_index:end_of_word_index])
            # 4. Move to next index after word grabbed
            index = end_of_word_index
        return decoded_strings