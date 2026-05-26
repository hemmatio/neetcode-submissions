class Solution:

    def encode(self, strs: List[str]) -> str:
        # the first n characters, are integers, separated by commas.
        # the first occurrence of '#' indicates that this section has ended.
        # this section contains the lengths of each string.
        str_lengths = [len(s) for s in strs]
        str_lengths_code = ','.join([str(l) for l in str_lengths]) + ','
        # print(f"strlenghtscode is {str_lengths_code} and its length is {len(str_lengths_code)}")
        
        encoded_string = f"{str_lengths_code}#{''.join(strs)}"
        # print(f"encoded string: {encoded_string}")
        return encoded_string

    def decode(self, s: str) -> List[str]:
        str_lengths_code, joinedstr = s.split("#", 1)
        # print(f"strlengthscode: {str_lengths_code}, joinedstr: {joinedstr}")
        str_lengths = [int(s) for s in str_lengths_code.split(',') if s]
        # print(f"str lengths: {str_lengths}")
        result = []
        idx = 0
        for length in str_lengths:
            result.append(joinedstr[idx:idx+length])
            idx += length

        return result

