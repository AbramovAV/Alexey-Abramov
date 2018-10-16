import heapq


class Tree():
    def __init__(self,left,right):
        self.left = left
        self.right = right
    def walk(self,codes,acc):
        if type(self.left)==str:
            codes[self.left] = acc+"0" or "0"
        if type(self.right)==str:
            codes[self.right] = acc+"1" or "1"
        if type(self.left)==Tree:
            self.left.walk(codes,acc+"0")
        if type(self.right)==Tree:
            self.right.walk(codes,acc+"1")
    

def HuffmanCoder(string):
    chars = {}
    for char in string:
        if char not in chars.keys():
            chars[char]=1
        else:
            chars[char]+=1
    items = [(freq,0,char) for char,freq in chars.items()]
    heapq.heapify(items)
    codes = {}
    count = 0
    while len(items)>1:
        left = heapq.heappop(items)
        right = heapq.heappop(items)
        count+=1
        element = (left[0]+right[0],count,Tree(left[2],right[2]))
        heapq.heappush(items,element)
    HuffmanTree = items[0][2]
    if len(chars.keys())>1:
        HuffmanTree.walk(codes,"")
    else:
        codes[string[0]] = "0"
    encoded_string = "".join(codes[char] for char in string)
    print(len(codes.keys()),len(encoded_string))
    print("\n".join("{0}: {1}".format(char,code) for char,code in codes.items()))
    print(encoded_string)
if __name__=='__main__':
    string=input()
    HuffmanCoder(string)