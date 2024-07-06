def generate_booklet_pages(num_pages_per_booklet, num_booklets):
    if num_pages_per_booklet * num_booklets != 100:
        raise ValueError("Total number of pages must equal 100 for 5 booklets with 20 pages each.")

    booklet_sequence = []
    for booklet_num in range(num_booklets):
        start_page = booklet_num * num_pages_per_booklet + 1
        for i in range(num_pages_per_booklet // 2):
            front_page = start_page + num_pages_per_booklet - 1 - i
            back_page = start_page + i
            booklet_sequence.append((front_page, back_page))

    return booklet_sequence

# Example usage:
num_pages_per_booklet = 20
num_booklets = 5
sequence = generate_booklet_pages(num_pages_per_booklet, num_booklets)
print(sequence)








# a pokud je číslo vetší jak původní počet stran, tak \newpage