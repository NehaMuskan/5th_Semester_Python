def number_to_words(number):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    return " ".join(words[int(i)] for i in str(number))
    
number=int(input())
print(number_to_words(number))