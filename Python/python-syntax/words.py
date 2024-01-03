def print_upper_words(words):
    """Print each word on a separate line, but all UPPERCASED

    for ex: print_upper_words(["Basketball", "is", "the", "greatest", 
    "sport", "known", "to", "man"])
    BASKETBALL
    IS
    THE 
    GREATEST
    SPORT
    KNOWN
    TO
    MAN
    """

    for word in words: 
        print(word.upper())


def print_upper_words_e(words):
    """Print each word on a separate line in all CAPS but only if it
    starts with either "E" or "e"
    """
    for word in words: 
        if word.startswith("E") or word.startswith("e"):
            print(word.upper())


def print_upper_words_starts_with(words, must_start_with):
    """Print each word on a separate line in all CAPS but you can pass
    in a set of letters and have it only print words that start with
    one of those letters 
    
    for ex: # this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
    """
    for word in words: 
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
