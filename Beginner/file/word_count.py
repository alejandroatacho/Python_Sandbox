word_count = {}

with open("placeholder/text.txt", "r") as f:

    def function_1():
        counter = 0
        for line in f:
            words = line.split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
            counter += 1
        print(f"There are {counter} lines.")
        print(f"There are {len(word_count)} unique words in total in this file.")
        
    function_1()
