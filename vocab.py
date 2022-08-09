# type: ignore
import random
from os import system
import sys
import platform
from datetime import datetime
from word_list import *

Lists = {
    "LIST 1": List1,
    "LIST 2": List2,
    "LIST 3": List3,
    "LIST 4": List4,
    "LIST 5": List5,
    "LIST 6": List6,
    "LIST 7": List7,
    "LIST 8": List8,
    "LIST 9": List9,
    "LIST 10": List10,
    "LIST 11": List11,
    "LIST 12": List12,
    "LIST 13": List13,
    "LIST 14": List14,
}

ListOfLists = list(Lists.keys())


def clear_output():
    my_os = platform.system()

    if my_os == "Windows":
        system("cls")
    elif my_os == "Darwin":
        system("clear")
    elif my_os == "Linux":
        system("clear")
    else:
        print("Unknown OS")


def WordMatch(user, select):
    return user.upper() == select.upper()


def Heading(heading):
    print("\n----------------------------------------------")
    print("\n        {}".format(heading))
    print("\n----------------------------------------------")
    print("\nPress Enter to continue or Q to quit at any time")


def FullRevision():
    clear_output()
    Heading("Full Revision")
    for ListNumber, List in Lists.items():
        print("\n----------------------------------------------")
        print("\n                     {}".format(ListNumber))
        print("\n----------------------------------------------\n")
        for meaning, synonyms in List.items():
            print("{} : Total words in this group is {}".format(meaning, len(synonyms)))
            key_pressed = input()
            if key_pressed.lower() == "q":
                clear_output()
                return
            else:
                for index in range(len(synonyms)):
                    print("{}. {}".format(str(index + 1), synonyms[index]))
                    key_pressed = input()
                    if key_pressed.lower() == "q":
                        clear_output()
                        return
                    else:
                        continue
    clear_output()


def RandomRevision():
    clear_output()
    Heading("Random Revision")
    random.seed()
    key_pressed = ""
    while key_pressed.lower() != "q":
        RandomList = Lists[random.choice(ListOfLists)]
        RandomMeaning = random.choice(list(RandomList.keys()))
        RandomSynonym = random.choice(list(RandomList[RandomMeaning]))
        Synonyms = RandomList[RandomMeaning]

        print("\nDo you know {} ?".format(RandomSynonym))
        key_pressed = input()
        if key_pressed.lower() == "q":
            clear_output()
            return
        else:
            print("\nMeaning:", RandomMeaning)
            key_pressed = input()
            if key_pressed.lower() == "q":
                clear_output()
                return
            else:
                print("Similar:\n")
                for index in range(len(list(Synonyms))):
                    print("{}. {}".format(str(index + 1), Synonyms[index]))
                    key_pressed = input()
                    if key_pressed.lower() == "q":
                        clear_output()
                        return
    clear_output()


def RevisionWithMeaningOnly():
    clear_output()
    Heading("Revision With Meaning Only")
    random.seed()
    key_pressed = ""
    while key_pressed.lower() != "q":
        RandomList = Lists[random.choice(ListOfLists)]
        RandomMeaning = random.choice(list(RandomList.keys()))
        RandomSynonym = random.choice(list(RandomList[RandomMeaning]))

        print("\nDo you know {} ?".format(RandomSynonym))
        key_pressed = input()
        if key_pressed.lower() == "q":
            clear_output()
            return
        else:
            print("\nMeaning: {}".format(RandomMeaning))
            key_pressed = input()
    clear_output()


def RevisionWithRandomGroup():
    clear_output()
    Heading("Revision With Random Group")
    random.seed()
    key_pressed = ""
    while key_pressed.lower() != "q":
        RandomList = Lists[random.choice(ListOfLists)]
        RandomMeaning = random.choice(list(RandomList.keys()))

        print("\nWhat words are associated with : {}".format(RandomMeaning))
        key_pressed = input()
        if key_pressed.lower() == "q":
            clear_output()
            return
        else:
            for index in range(len(list(RandomList[RandomMeaning]))):
                print("{}. {}".format(str(index + 1), RandomList[RandomMeaning][index]))
                key_pressed = input()
                if key_pressed.lower() == "q":
                    clear_output()
                    return
    clear_output()


def FindGroupUsingWord():
    clear_output()
    Heading("Find Group Using Word")
    match = 0
    word = str(input("\nEnter Word : ")).lower()
    for ListNumber, List in Lists.items():
        for meaning, synonyms in List.items():
            for index in range(len(synonyms)):
                if word == synonyms[index].lower():
                    match = 1
                    print("\nGroup Name : {}".format(meaning))
                    print("\nList Number : {}".format(ListNumber))
                    choice = input("\nDo you want to list all the synonyms? (Y/N) : ")
                    if choice == "Y" or choice == "y":
                        for index in range(len(synonyms)):
                            print("\n{}. {}".format(str(index + 1), synonyms[index]))
                        input()
                        clear_output()
                        return
                    else:
                        clear_output()
                        return
                else:
                    continue
    if match == 0:
        print("\nWord not found")
        input()
        clear_output()


def MCQTest():
    clear_output()
    Heading("MCQ Test")
    random.seed()
    Types = ["SynonymToMeaning", "MeaningToSynonym"]
    Options = []
    score = 0
    count = 0
    NoOfQuestions = input("\nHow many words do you want to revise in the test : ")
    while True:
        if NoOfQuestions.isnumeric():
            NoOfQuestions = int(NoOfQuestions)
            break
        else:
            print("Invalid choice! Enter numerical input.")
            NoOfQuestions = input("\nHow many words do you want to revise in the test : ")
    print()
    for i in range(NoOfQuestions):
        print("-------------------------------------")
        RandomType = random.choice(Types)
        if RandomType == "SynonymToMeaning":
            for j in range(3):
                Options.append(random.choice(list(Lists[random.choice(ListOfLists)])))
            RandomList = Lists[random.choice(ListOfLists)]
            RandomMeaning = random.choice(list(RandomList.keys()))
            RandomSynonym = random.choice(list(RandomList[RandomMeaning]))
            Options.append(RandomMeaning)
            random.shuffle(Options)
            print("\nWhat is the meaning of {}?".format(RandomSynonym))
            for option in Options:
                print("\n{}. {}".format(str(Options.index(option) + 1), option))

            answer = input("\nAnswer: ")
            while True:
                if answer.isnumeric():
                    if int(answer) in [1, 2, 3, 4]:
                        answer = int(answer)
                        break
                    else:
                        print("Valid options are 1, 2, 3 & 4. Enter again")
                        answer = input("\nAnswer: ")
                else:
                    print("Invalid choice! Enter numerical input.")
                    answer = input("\nAnswer: ")

            if answer == Options.index(RandomMeaning) + 1:
                print("\nCorrect ✅")
                score += 1
            else:
                print("\nIncorrect ❌")
                print(
                    "\nThe correct answer is ({}) {}".format(
                        Options.index(RandomMeaning) + 1, RandomMeaning
                    )
                )
            Options.clear()
            count += 1

            print("\n\n-------------------------------------\n")
            print("          Score: {} / {}".format(score, count))
            print("\n-------------------------------------")
            print()
            input()
            clear_output()
        else:
            for j in range(3):
                RandomList = Lists[random.choice(ListOfLists)]
                RandomMeaning = random.choice(list(RandomList.keys()))
                RandomSynonym = random.choice(list(RandomList[RandomMeaning]))
                Options.append(RandomSynonym)
            RandomList = Lists[random.choice(ListOfLists)]
            RandomMeaning = random.choice(list(RandomList.keys()))
            RandomSynonym = random.choice(list(RandomList[RandomMeaning]))

            Options.append(RandomSynonym)
            random.shuffle(Options)
            print('\nWhat word descibes "{}"?'.format(RandomMeaning))
            for option in Options:
                print("\n{}. {}".format(str(Options.index(option) + 1), option))

            answer = input("\nAnswer: ")
            while True:
                if answer.isnumeric():
                    if int(answer) in [1, 2, 3, 4]:
                        answer = int(answer)
                        break
                    else:
                        print("Valid options are 1, 2, 3 & 4. Enter again")
                        answer = input("\nAnswer: ")
                else:
                    print("Invalid choice! Enter numerical input.")
                    answer = input("\nAnswer: ")

            if answer == Options.index(RandomSynonym) + 1:
                print("\nCorrect ✅")
                score += 1
            else:
                print("\nIncorrect ❌")
                print(
                    "\nThe correct answer is ({}) {}".format(
                        Options.index(RandomSynonym) + 1, RandomSynonym
                    )
                )
            Options.clear()
            count += 1

            print("\n\n-------------------------------------\n")
            print("          Score: {} / {}".format(score, count))
            print("\n-------------------------------------")
            print()
            input()
            clear_output()
    if score >= count / 2:
        print("\n-------------------------------------\n")
        print("        Final Score: {} / {}".format(score, count))
        print("\n      You passed the test 🤩")
        print("\n-------------------------------------\n")
        input()
        clear_output()
    else:
        print("\n-------------------------------------\n")
        print("        Final Score: {} / {}".format(score, count))
        print("\n     You scored less than 50% 😢")
        print("\n       Try retaking the test 😊")
        print("\n-------------------------------------\n")
        input()
        clear_output()


def WrittenTest():
    clear_output()
    Heading("Written Test")
    random.seed()
    score = 0
    count = 0
    NoOfQuestions = input("\nHow many words do you want to revise in the test : ")
    while True:
        if NoOfQuestions.isnumeric():
            NoOfQuestions = int(NoOfQuestions)
            break
        else:
            print("Invalid choice! Enter numerical input.")
            NoOfQuestions = input("\nHow many words do you want to revise in the test : ")
    print()
    for i in range(NoOfQuestions):
        print("-------------------------------------")
        RandomList = Lists[random.choice(ListOfLists)]
        RandomMeaning = random.choice(list(RandomList.keys()))
        Synonyms = list(RandomList[RandomMeaning])
        Synonyms = [word.lower() for word in Synonyms]
        print("\nEnter any word associated with : {}".format(RandomMeaning))
        answer = input("\nAnswer: ")
        if answer.lower() in Synonyms:
            print("\nCorrect ✅")
            score += 1
            count += 1
            print("\n\n-------------------------------------\n")
            print("          Score: {} / {}".format(score, count))
            print("\n-------------------------------------")
            print()
            choice = input("\nDo you want to list all the synonyms? (Y/N) : ")
            if choice == "Y" or choice == "y":
                for index in range(len(Synonyms)):
                    print("\n{}. {}".format(str(index + 1), Synonyms[index]))
                input()
                clear_output()
            else:
                clear_output()
        else:
            print("\nIncorrect ❌")
            count += 1
            print("\n\n-------------------------------------\n")
            print("          Score: {} / {}".format(score, count))
            print("\n-------------------------------------")
            print()
            choice = input("\nDo you want to list all the synonyms? (Y/N) : ")
            if choice == "Y" or choice == "y":
                for index in range(len(Synonyms)):
                    print("\n{}. {}".format(str(index + 1), Synonyms[index]))
                input()
                clear_output()
            else:
                clear_output()

    if score >= count / 2:
        print("\n-------------------------------------\n")
        print("        Final Score: {} / {}".format(score, count))
        print("\n      You passed the test 🤩")
        print("\n-------------------------------------\n")
        input()
        clear_output()
    else:
        print("\n-------------------------------------\n")
        print("        Final Score: {} / {}".format(score, count))
        print("\n     You scored less than 50% 😢")
        print("\n       Try retaking the test 😊")
        print("\n-------------------------------------\n")
        input()
        clear_output()


def printMenu():
    print("------------------------------------")
    print("Please enter a number: ")
    print("1. Full Revision")
    print("2. Random Revision")
    print("3. Revision With Meaning Only")
    print("4. Revision With Random Group")
    print("5. Find Group Using Word")
    print("6. MCQ Test")
    print("7. Written Test")
    print("8. Exit")
    print("------------------------------------")
    print()


def main():
    print("\nWelcome to the GRE World!")

    while True:
        print("\nTell me what would you like to do")
        print()
        printMenu()
        choice = input("Enter your choice: ")

        if choice.isnumeric():
            choice = int(choice)
            if choice == 1:
                FullRevision()
            elif choice == 2:
                RandomRevision()
            elif choice == 3:
                RevisionWithMeaningOnly()
            elif choice == 4:
                RevisionWithRandomGroup()
            elif choice == 5:
                FindGroupUsingWord()
            elif choice == 6:
                MCQTest()
            elif choice == 7:
                WrittenTest()
            elif choice == 8:
                clear_output()
                sys.exit()
            else:
                print("\nInvalid Choice! Press Enter to continue.")
                input()
                clear_output()
        else:
            print("\nInvalid Choice! Press Enter to continue.")
            input()
            clear_output()
            continue


if __name__ == "__main__":
    main()
