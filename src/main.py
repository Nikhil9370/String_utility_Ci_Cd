from string_utis import reverse_string , to_upper,to_lower,count_vowels

if __name__ == "__main__":
    sample = "Hello World"


    print("Original:", sample)
    print("Reversed:", reverse_string(sample))
    print("Upper:", to_upper(sample))
    print("Lower:", to_lower(sample))
    print("Vowels_count:", count_vowels(sample))