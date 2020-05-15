import random

word_dict = {
    "area": "the extent of a two-dimensional surface within a boundary",
    "analysis": "abstract separation of a whole into its constituent parts",
    "approach": "move towards",
    "assessment": "the act of judging a person or situation or event",
    "assume": "take to be the case or to be true",
    "authority": "the power or right to give orders or make decisions",
    "available": "obtainable or accessible and ready for use or service",
    "benefit": "something that aids or promotes well-being",
    "concept": "an abstract or general idea inferred from specific instances",
    "consistent": "the same throughout in structure or composition",
    "constitutional": "existing as an essential characteristic",
    "context": "the set of facts or circumstances that surround a situation",
    "contract": "a binding agreement that is enforceable by law",
    "create": "bring into existence",
    "data": "a collection of facts from which conclusions may be drawn",
    "definition": "a concise explanation of the meaning of a word or phrase",
    "derived": "formed or developed from something else; not original",
    "distribution": "the act of spreading or apportioning",
    "economic": "of or relating to production and management of wealth",
    "environment": "the totality of surrounding conditions",
    "established": "brought about or set up or accepted",
    "estimate": "judge tentatively",
    "evidence": "knowledge on which to base belief",
    "export": "sell or transfer abroad",
    "factor": "anything that contributes causally to a result",
    "financial": "involving fiscal matters",
    "formula": "a group of symbols that make a mathematical statement",
    "function": "what something is used for",
    "identified": "having the identity known or established",
    "income": "the financial gain accruing over a given period of time",
    "indicate": "designate a place, direction, person, or thing",
    "individual": "being or characteristic of a single thing or person",
    "interpretation": "the act of expressing something in an artistic performance",
    "involved": "connected by participation or association or use",
    "issue": "some situation or event that is thought about",
    "labour": "productive work (especially physical work done for wages)",
    "legal": "established by or founded upon law or official rules",
    "legislation": "the act of making or enacting laws",
    "major": "greater in scope or effect",
    "method": "a way of doing something, especially a systematic way",
    "occur": "come to pass",
    "percent": "a proportion in relation to a whole",
    "period": "an amount of time",
    "policy": "a plan of action adopted by an individual or social group",
    "principle": "a basic generalization that is accepted as true",
    "procedure": "a particular course of action intended to achieve a result",
    "process": "a particular course of action intended to achieve a result",
    "required": "necessary by rule",
    "research": "a seeking for knowledge",
    "response": "the speech act of continuing a conversational exchange",
    "role": "the actions and activities assigned to a person or group",
    "section": "one of several parts or pieces that fit with others",
    "sector": "a particular aspect of life or activity",
    "significant": "rich in implication",
    "similar": "having the same or nearly the same characteristics",
    "source": "the place where something begins",
    "specific": "stated explicitly or in detail",
    "structure": "a complex entity made of many parts",
    "theory": "a belief that can guide behavior",
    "variable": "something that is likely to change"
}

word_list = [
    "area", "analysis", "approach", "assessment", "assume", "authority", "available", "benefit", "concept", "consistent", "constitutional", "context", "contract", "create", "data", "definition", "derived", "distribution", "economic", "environment", "established", "estimate", "evidence", "export", "factor", "financial", "formula", "function", "identified", "income", "indicate", "individual", "interpretation", "involved", "issue", "labour", "legal", "legislation", "major", "method", "occur", "percent", "period", "policy", "principle", "procedure", "process", "required", "research", "response", "role", "section", "sector", "significant", "similar", "source", "specific", "structure", "theory", "variable"
]


def pick_random_word(word_list):
    index = random.randrange(0, len(word_list))
    word = word_list[index]
    return word


def get_hint(word):
    for k, v in word_dict.items():
        if k == word:
            return word_dict[k]


def generate_partial_word(word):
    _a, _b = random.randrange(0, len(word)-1), random.randrange(0, len(word)-1)
    lst = []
    missing_lst = []
    for inx in range(len(word)):
        if inx == _a:
            missing_lst.append(word[inx])
            lst.append('_')
        elif inx == _b:
            missing_lst.append(word[inx])
            lst.append('_')
        else:
            lst.append(word[inx])
    return lst, missing_lst


def play_game():
    attempt = 0
    random_word = pick_random_word(word_list)
    partial_word, missing_lst = generate_partial_word(random_word)
    print(''.join(partial_word))

    while(True):
        inp = input(
            "Enter a letter & index. Format: (letter, index) \n").split(',')
        guess_letter = inp[0]
        guess_index = int(inp[1])
        attempt += 1
        if guess_index > len(random_word):
            print("Index out of range!\n")
            guess_index = input("Enter index again.\n")

        if (guess_letter in missing_lst) and (partial_word.count('_') >= 1):
            if partial_word[guess_index] == '_':
                partial_word[guess_index] = guess_letter
                if ''.join(partial_word) == random_word:
                    print("Great you have guessed it right! Attempts taken: ", attempt)
                    break
                else:
                    print('Progress so far: ', ''.join(partial_word))
                    print('\n')
            else:
                print("You are closes. Keep up!\n")
        else:
            print("Try harder!\n")
            if attempt > 3 and attempt <= 5:
                if input("Press 'h' for hint\n") == 'h':
                    print(get_hint(random_word))
            elif attempt > 5:
                if input("Type 'quit' to reveal the answer\n") == 'quit':
                    print("Answer is: ", random_word)
                    break
            else:
                continue


if __name__ == "__main__":
    play_game()
