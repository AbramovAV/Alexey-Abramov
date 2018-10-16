def HuffmanDecoder(string,codes,l):
    decoded_string = ""
    current_code = ""
    for i in range(l):
        current_code +=string[i]
        if current_code in codes.keys():
            decoded_string+=codes[current_code]
            current_code = ""
    print(decoded_string)

if __name__=='__main__':
    from copy import copy
    k,l=list(map(int,input().split(" ")))
    codes = {}
    for _ in range(k):
        char,code = input().split(": ")
        codes[code] = char
    string = input()
    HuffmanDecoder(string,copy(codes),l) 