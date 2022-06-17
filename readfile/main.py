def read_file_content(filename):
    with open(filename) as f:
        contents = f.read()
        return contents


print(read_file_content('story.txt'))


# def count_words(words):
#     words = read_file_content('story.txt').split()
#     counts = dict()
#
#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#
#     return counts
#
#
# print(count_words('story.txt'))