class HuffNode:
    def __init__(self, key, freq=0):
        self.key = key
        self.freq = freq
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + ':' + str(self.freq)

class Huffman:
    def __init__(self):
        self.root = None

    def buildTree(self, q):
        while len(q) > 1:
            q1 = q.dequeue()
            q2 = q.dequeue()
            node = HuffNode(None, q1.freq + q2.freq)
            node.left = q1
            node.right = q2
            q.enqueue(node)
        self.root = q.dequeue()

    def printTree(self):
        self.preOrderTrav(self.root)

    def preOrderTrav(self, subtree):
        if subtree is not None:
            print(subtree)
            self.preOrderTrav(subtree.left)
            self.preOrderTrav(subtree.right)

    def printCode(self):
        code = ''
        filename = "huff_code.txt"
        with open(filename, 'w') as f:
            self.recPrintCode(self.root, code, f)

    def recPrintCode(self, subtree, code, file):
        if subtree is not None:
            if subtree.left is None:
                file.write(subtree.key + ':' + code + "\n")
                return
            self.recPrintCode(subtree.left, code+'0', file)
            self.recPrintCode(subtree.right, code+'1', file)

    def rebuild(self):
        def buildrec(node, key, code):
            if len(code) == 0:
                node.key = key
            else:
                if code[0] == '0':
                    if node.left is None:
                        node.left = HuffNode(None)
                    node = node.left
                if code[0] == '1':
                    if node.right is None:
                        node.right = HuffNode(None)
                    node = node.right
                buildrec(node, key, code[1:])
        filename = "huff_code.txt"
        code = list()
        h = Huffman()
        h.root = HuffNode(None)
        with open(filename) as f:
            codes = f.readlines()
        for c in codes:
            key = c[0]
            code = c[2:-1]
            buildrec(h.root, key, code)
        return h

    def encodeASCII(self, filename):
        def recWriteCode(subtree, code):
            if subtree is not None:
                if subtree.left is None:
                    map[subtree.key] = code
                    return
                recWriteCode(subtree.left, code+'0')
                recWriteCode(subtree.right, code+'1')
        with open(filename) as rf:
            text = rf.read()
            q = PQ()
            d = dict()
            for t in text:
                o = text.count(t)
                d[t] = o
            for key in d:
                q.enqueue(HuffNode(key, int(d[key])))
            self.buildTree(q)
            code = ''
            map = dict()
            recWriteCode(self.root, code)
            with open('encrypt.txt', 'w') as wf:
                wf.write(str(map))
                wf.write('\n')
                for l in text:
                    wf.write(map[l])

    def reproduceASCII(self, filename):
        original = ""
        with open(filename) as f:
            dic = eval(f.readline()[:-1])
            text = f.readline()
            while len(text) > 0:
                letter = text[0]
                text = text[1:]
                while len(letter) >= 1:
                    want_break = False
                    for key in dic:
                        if dic[key] == letter:
                            original += key
                            want_break = True
                            break
                    if want_break:
                        break
                    letter += text[0]
                    text = text[1:]
        with open("original_text.txt", 'w') as wf:
            wf.write(original)

    def compress(self):
        total_b_text = ""
        with open("encrypt.txt") as f:
            f.readline()
            b_text = f.readline()
            last_byte_chr = len(b_text) % 8
            if last_byte_chr == 0:
                last_byte_chr = 8
            need0 = 8 - last_byte_chr
            rest_bytes = b_text[:-last_byte_chr]
            bi = bin(last_byte_chr)[2:]
            while len(bi) != 8:
                bi = '0' + bi
            last_byte = '0'*need0 + b_text[len(b_text)-last_byte_chr:]
            total_b_text = rest_bytes + bi + last_byte
        dec_data = [int(total_b_text[x:x+8], 2) for x in range(0, len(total_b_text), 8)]
        with open('compress.txt', 'wb') as bf:
            bf.write(bytes(dec_data))

    def decompress(self):
        with open('compress.txt', 'rb') as bf:
            byte_text = bf.read()
            print(byte_text)
            print(list(byte_text))

class PQ:
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def dequeue(self):
        assert len(self) > 0, 'empty Q'
        return self.items.pop(0)

    def enqueue(self, item):
        i = 0
        while i < len(self) and self.items[i].freq <= item.freq:
            i += 1
        self.items.insert(i, item)


if __name__ == '__main__':
    h = Huffman()
    q = PQ()
    q.enqueue(HuffNode('a', 45))
    q.enqueue(HuffNode('b', 13))
    q.enqueue(HuffNode('c', 12))
    q.enqueue(HuffNode('d', 16))
    q.enqueue(HuffNode('e', 9))
    q.enqueue(HuffNode('f', 5))
    h.buildTree(q)
    h.printTree()
    print('--------------------')
    # h.printCode()
    p = h.rebuild()
    p.printTree()
    p.encodeASCII('mesg.txt')
    p.reproduceASCII('encrypt.txt')
