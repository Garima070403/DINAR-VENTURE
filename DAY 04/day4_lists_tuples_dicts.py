# Day 4 – Lists, Tuples, and Dictionaries
# Name: Garima Raj
# ID: DV06PY00010
# College: GEC Patan, GTU

#  LISTS PRACTICE
# List of my favorite programming languages
languages = ["Python", "C", "Java"]

print("Favorite Languages:", languages)

# Add a new language
languages.append("HTML")
print("After adding a language:", languages)

# Remove one language
languages.remove("Java")
print("After removing a language:", languages)

# Print number of languages
print("Total languages I like:", len(languages))


#  TUPLES PRACTICE
# Tuple of my dream travel cities (immutable)
travel_cities = ("Paris", "Tokyo", "Dubai", "New York")

# Print first and last city
print("\nFirst city I want to visit:", travel_cities[0])
print("Last city on my list:", travel_cities[-1])

# NOTE: Tuples are immutable, so we cannot modify them

# DICTIONARIES PRACTICE
# Dictionary about my favorite book
my_book = {
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "genre": "Fiction",
    "year": 1988
}

# Print author's name
print("\nBook Author:", my_book["author"])

# Add a key for pages
my_book["pages"] = 208

# Update the genre
my_book["genre"] = "Motivational Fiction"

# Print full book info
print("Updated Book Info:", my_book)
