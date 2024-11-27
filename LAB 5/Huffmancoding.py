import heapq
from collections import defaultdict
import os

import PyPDF2
from docx import Document
from bs4 import BeautifulSoup


class Node:
    def __init__(self, character, frequency):
        self.ch = character
        self.freq = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def calculate_frequency(s):
    freq_map = defaultdict(int)
    for ch in s:
        freq_map[ch] += 1
    return freq_map


def build_huffman_tree(freq_map):
    pq = [Node(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(pq)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(pq, new_node)

    return pq[0]


def assign_codes(root, code, huffman_codes):
    if root is None:
        return
    if root.ch is not None:
        huffman_codes[root.ch] = code
    assign_codes(root.left, code + "0", huffman_codes)
    assign_codes(root.right, code + "1", huffman_codes)


def compress_string(s, huffman_codes):
    return "".join(huffman_codes[ch] for ch in s)


def calculate_compression_ratio(original, compressed):
    if len(compressed) == 0:
        return float("inf")
    original_size = len(original) * 8
    compressed_size = len(compressed)
    return original_size / compressed_size


def read_pdf(file_path):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = "".join(page.extract_text() or "" for page in reader.pages)
            return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def read_docx(file_path):
    try:
        doc = Document(file_path)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def read_html(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
            return soup.get_text(separator="\n")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def read_book(file_path):
    if file_path.endswith(".pdf"):
        return read_pdf(file_path)
    elif file_path.endswith(".docx"):
        return read_docx(file_path)
    elif file_path.endswith(".html"):
        return read_html(file_path)
    elif file_path.endswith(".txt"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
    else:
        print(f"Unsupported file format: {file_path}")
        return None


def main(file_paths):
    for file_path in file_paths:
        print(f"Reading book from: {file_path}")
        book_content = read_book(file_path)

        if book_content:
            freq_map = calculate_frequency(book_content)
            root = build_huffman_tree(freq_map)
            huffman_codes = {}
            assign_codes(root, "", huffman_codes)

            compressed_string = compress_string(book_content, huffman_codes)

            if compressed_string:
                compression_ratio = calculate_compression_ratio(
                    book_content, compressed_string
                )
                print(f"Original size: {len(book_content)} characters")
                print(f"Compressed size: {len(compressed_string)} bits")
                print(f"Compression Ratio: {compression_ratio:.2f}")
            else:
                print("Compression failed or resulted in an empty string.")


if __name__ == "__main__":
    positive_test_cases = [
        r"C:\Users\Krish\Downloads\Pdf_File.pdf",
        r"C:\Users\Krish\Downloads\Docx_File.docx",
        r"C:\Users\Krish\Downloads\Text_File.txt",
        r"C:\Users\Krish\Downloads\Html_file.html",
        r"C:\Users\Krish\Downloads\Html_file2.html",
    ]

    negative_test_cases = [
        r"C:\Users\Krish\Downloads\Image.jpg",
        r"C:\Users\Krish\Downloads\Doc.docx",
        r"C:\Users\Krish\Downloads\Zero_letter_File.pdf",
        r"C:\Users\Krish\Downloads\Single_Letter_File.txt",
        r"C:\Users\Krish\Downloads\Video_File.mp4",
    ]

    main(positive_test_cases)
    main(negative_test_cases)
