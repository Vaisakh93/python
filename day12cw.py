def mini_library_system():
    try:
        title = input("Enter the book title: ")

        if not all(char.isalpha() or char.isspace() for char in title):
            raise ValueError("Error: The book title must contain only alphabets and spaces.")

        year = input("Enter the publication year (e.g., 1999, 2002): ")

        if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
            raise ValueError("Error: The publication year must be a 4-digit number starting with '19' or '20'.")

        print("\nBook accepted!")
        print(f"Title: {title}")
        print(f"Year: {year}")

    except ValueError as e:
        print(e)


mini_library_system()
