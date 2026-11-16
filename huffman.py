
import heapq
import itertools

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

def huffman_encoding(characters, frequencies):
    counter = itertools.count()
    heap = []

    for char, freq in zip(characters, frequencies):
        heapq.heappush(heap, (freq, next(counter), Node(char, freq)))

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        parent = Node(None, freq1 + freq2)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, (parent.freq, next(counter), parent))

    codes = {}

    def generate_codes(node, code):
        if node.char is not None:
            codes[node.char] = code if code else "0"
            return

        generate_codes(node.left, code + "0")
        generate_codes(node.right, code + "1")

    generate_codes(heap[0][2], "")
    return codes

n = int(input("Enter number of characters: "))
characters = []
frequencies = []

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))
    characters.append(char)
    frequencies.append(freq)

if n <= 0 or len(set(characters)) != n or any(f <= 0 for f in frequencies):
    print("Enter unique characters and positive frequencies.")
else:
    codes = huffman_encoding(characters, frequencies)

    print("\nHuffman Codes:")
    print("Character\tFrequency\tCode")

    for char, freq in zip(characters, frequencies):
        print(char, "\t\t", freq, "\t\t", codes[char])
