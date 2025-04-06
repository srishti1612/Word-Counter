# Word Counter Program

# Function to count words in the input text
def count_words(text):
    # Split text by whitespace and filter out empty strings
    words = text.strip().split()
    return len(words)

def main():
    print("Welcome to the Word Counter Program!")

    # Get input from the user
    text = input("Please enter a sentence or paragraph: ").strip()

    # Error handling for empty input
    if not text:
        print("Error: No text provided. Please enter some text.")
        return

    # Count the words and display the result
    word_count = count_words(text)
    print(f"\nThe number of words in your input is: {word_count}")

if __name__ == "__main__":
    main()
