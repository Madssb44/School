quiz = {
    "Welcome message": {"Part 1": "Welcome to the Old School Runescape quiz!",
                        "Part 2": "The questions will get harder and harder as you go on"
                        },
    "questions": {"question 1": "What is the name of the you spawn into after tutorial island?\n1 = Varrock\n2 = Lumbridge\n3 = Falador\n",
                  "question 2": "How many skills are there in osrs?\n1 = 18\n2 = 23\n3 = 25\n",
                  "question 3": "In which city is the grandexchange?\n1 = Rimmington\n2 = Lumbridge\n3 = Varrock\n",
                  "question 4": "How many inventroy stots do you have?\n1 = 24\n2 = 28\n3 = 32\n",
                  "question 5": "Who do you have to deafeat to earn your firecape?\n1 = Jad\n2 = Zulrah\n3 = Yama\n",
                  "question 6": "The game updates in ticks with each tick being how long?\n1 = 0.6 sec\n2 = 1 sec\n3 = 2.5 sec\n",
                  "question 7": "Whats half of 99?\n1 = 44.5\n2 = 92\n3 = 98\n",
                  "question 8": "What is the heighest combat level in the game?\n1 = 126\n2 = 702\n3 = 1563\n",
                  "question 9": "Who is the the first person to earn the legendary infernocape?\n1 = Woox\n2 = Gnomemonkey\n3 = Odablock\n",
                  "question 10": "When desert tresture 2 was released a fishing spot was found in stranglewood which holds one of the rarest drop in the game what is the drop rate?\n1 = 1/100,000\n2 = 1/ 250,000\n3 = 1/500,000\n"
                  },
    "correct answers": {"question 1": "2",
                        "question 2": "2",
                        "question 3": "3",
                        "question 4": "2",
                        "question 5": "1",
                        "question 6": "1",
                        "question 7": "2",
                        "question 8": "3",
                        "question 9": "1",
                        "question 10": "3"
                        },
    "points": 0,
    "Ending message": {"Total points": "The final tally of your points is! ",
                       "10 points": "I think its time for you to touch some grass...",
                       "More than 5 points": "Seems like you know the game quite well! im glad to hear that!",
                       "More than 2 points": "looks like its about time you start playing!",
                       "0 points": "Really... nothing... shame on you..."
                       }
}
for part in quiz["Welcome message"]:
    print(quiz["Welcome message"][part])
for question in quiz["questions"]:
    answer = input(quiz["questions"][question] + "\n")
    if answer == quiz["correct answers"][question]:
        quiz["points"] += 1
        print("Correct!")
    else:
        print("Wrong")
for part in quiz["Ending message"]:
    if part == "Total points":
        print(quiz["Ending message"][part] + str(quiz["points"]) + " points in total!")
    elif part == "10 points" and quiz["points"] == 10:
        print(quiz["Ending message"][part])
        exit()
    elif part == "More than 5 points" and quiz["points"] > 5:
        print(quiz["Ending message"][part])
        exit()
    elif part == "More than 2 points" and quiz["points"] > 2:
        print(quiz["Ending message"][part])
        exit()
    elif part == "0 points" and quiz["points"] == 0:
        print(quiz["Ending message"][part])
        exit()
