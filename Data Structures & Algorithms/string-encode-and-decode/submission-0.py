class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''

        for word in strs:
            encoded_str += str(len(word)) + "#" + word
        return encoded_str

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0
        while i < len(s):
            num_index = s.find('#',i)
            if num_index == -1:
                raise ValueError("Invalid encoded string")
            else:
                num = int(s[i:num_index])
                # print(num)
                word = s[num_index+1: num+num_index+1]
                # print(word)
                res.append(word)
                i = num+num_index + 1
            
        return res
