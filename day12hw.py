try:
    name = input("Please enter your name: ").strip()
    feedback = input("Please enter your feedback: ").strip()

    if not name:
        raise ValueError("Error: Name cannot be empty.")
    if not feedback:
        raise ValueError("Error: Feedback cannot be empty.")

except ValueError as e:
    print(e)

else:
    print("\nThank you for your feedback!")
    print(f"Name: {name}")
    print(f"Feedback: {feedback}")

finally:
    print("\nProcess completed. Have a great day!")
