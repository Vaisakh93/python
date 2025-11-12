
paragraph = """  Python is an easy to learn, powerful programming language.
It has efficient high-level data structures and a simple approach to object-oriented programming.
This Python course helps beginners master the basics and build projects.  """

length = len(paragraph)
print("Length of paragraph:", length)

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview (first 50 chars):", paragraph[:50])

updated_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacing:\n", updated_paragraph)

lower_paragraph = updated_paragraph.lower()
print("\nLowercase version:\n", lower_paragraph)

trimmed_paragraph = lower_paragraph.strip()

words = trimmed_paragraph.split()
print("\nWords list:\n", words)

if "course" in words:
    print("\nThe word 'course' is found in the paragraph.")
else:
    print("\nThe word 'course' is not found in the paragraph.")

message = "The course description is {} characters long and has {} words.".format(len(trimmed_paragraph), len(words))
print("\n" + message)
