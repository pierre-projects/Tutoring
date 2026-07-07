
import random
import time


# Sentences are grouped by difficulty.
SENTENCES = {
    "short": [
        "Python is fun.",
        "I like coding.",
        "Practice makes progress.",
        "Games are fun to build.",
    ],
    "medium": [
        "Python makes it easy to build fun projects.",
        "Typing quickly takes practice and patience.",
        "A good programmer learns by building projects.",
    ],
    "long": [
        "Learning how to type accurately can help you work faster and feel more confident on a computer.",
        "Building small projects is one of the best ways to practice programming concepts and improve your problem solving skills.",
        "A patient programmer breaks big problems into smaller steps and tests each part along the way.",
    ],
}


def calculate_wpm(word_count, time_taken):
    """
    Calculate words per minute.

    Formula:
    words typed / seconds taken * 60
    """
    if time_taken == 0:
        return 0

    return (word_count / time_taken) * 60


def count_correct_words(target_sentence, user_sentence):
    """
    Compare the target and typed sentence word by word.

    zip() pairs words together:
    target word 1 with typed word 1,
    target word 2 with typed word 2, etc.
    """
    target_words = target_sentence.split()
    user_words = user_sentence.split()

    correct_words = 0

    for target_word, user_word in zip(target_words, user_words):
        # lower() ignores capitalization differences.
        # strip() removes punctuation from the beginning/end of words.
        cleaned_target = target_word.lower().strip(".,!?")
        cleaned_user = user_word.lower().strip(".,!?")

        if cleaned_target == cleaned_user:
            correct_words += 1

    return correct_words


def calculate_accuracy(correct_words, total_words):
    """
    Calculate the percentage of target words typed correctly.
    """
    if total_words == 0:
        return 0

    return (correct_words / total_words) * 100


def choose_difficulty():
    """
    Ask the player to choose short, medium, or long sentences.

    The loop repeats until the player gives a valid choice.
    """
    while True:
        print("\nChoose a difficulty:")
        print("1. Short")
        print("2. Medium")
        print("3. Long")

        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            return "short"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "long"
        else:
            print("Please choose 1, 2, or 3.")


def show_mistakes(target_sentence, user_sentence):
    """
    Show the correct sentence and the player's typed sentence.

    This helps the player quickly see what they missed.
    """
    print("\n--- Compare Your Typing ---")
    print(f"Target: {target_sentence}")
    print(f"Typed:  {user_sentence}")

    if target_sentence.lower() == user_sentence.lower():
        print("Perfect match! Nice job.")
    else:
        print("Look for words that were missing, changed, or out of order.")


def run_typing_test(personal_best_wpm):
    """
    Run one round and return the updated personal best WPM.
    """
    difficulty = choose_difficulty()

    # random.choice() selects one sentence from the chosen difficulty list.
    sentence = random.choice(SENTENCES[difficulty])

    print("\n--- Typing Speed Test ---")
    print(f"Difficulty: {difficulty.title()}")
    print("\nType this sentence as accurately and quickly as you can:\n")
    print(sentence)

    input("\nPress Enter when you are ready...")

    print("\nStart typing now!")

    # Start the timer immediately before the player types.
    start_time = time.time()

    user_sentence = input("> ")

    # Stop the timer when they press Enter.
    end_time = time.time()

    time_taken = end_time - start_time

    target_word_count = len(sentence.split())
    typed_word_count = len(user_sentence.split())

    correct_words = count_correct_words(sentence, user_sentence)
    wpm = calculate_wpm(typed_word_count, time_taken)
    accuracy = calculate_accuracy(correct_words, target_word_count)

    print("\n--- Results ---")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {typed_word_count}")
    print(f"Correct words: {correct_words} out of {target_word_count}")
    print(f"Typing speed: {wpm:.1f} WPM")
    print(f"Accuracy: {accuracy:.1f}%")

    # Update the personal best only when the current WPM is higher.
    if wpm > personal_best_wpm:
        personal_best_wpm = wpm
        print("\nNew personal best!")
    else:
        print(f"\nPersonal best: {personal_best_wpm:.1f} WPM")

    show_mistakes(sentence, user_sentence)

    return personal_best_wpm


def main():
    """
    Main game loop.

    personal_best_wpm stays outside the loop so it is remembered
    throughout the current program session.
    """
    print("Welcome to the Typing Speed Test!")

    personal_best_wpm = 0

    while True:
        personal_best_wpm = run_typing_test(personal_best_wpm)

        play_again = input("\nWould you like to try again? (yes/no): ").lower()

        if play_again not in ("yes", "y"):
            print(f"\nYour final personal best was {personal_best_wpm:.1f} WPM.")
            print("Thanks for playing. Keep practicing!")
            break


if __name__ == "__main__":
    main()

