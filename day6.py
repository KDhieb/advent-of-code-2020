

class CustomsDeclarations:

    def __init__(self, filename):
        file = open(filename, 'r')
        self.text = file.read()
        self.groups = self.text.split("\n\n")

    def split_and_count_unique_answers(self):
        count = 0
        for group in self.groups:
            people = group.split("\n")
            answer_string = ""
            for person_answers in people:
                answer_string += person_answers
            answers = []
            for char in answer_string:
                if char not in answers:
                    answers.append(char)
                    count += 1
        print(f"Part 1: {count}")

    def split_and_count_everyone_yes(self):
        count = 0
        for group in self.groups:
            people = group.split("\n")
            num_of_people = len(people)
            answers = {}
            for person in people:
                for char in person:
                    if char not in answers.keys():
                        answers[char] = 1
                    else:
                        answers[char] += 1
            for answer_count in answers.values():
                if answer_count == num_of_people:
                    count += 1
        print(f"Part 2: {count}")


if __name__ == '__main__':
    cd = CustomsDeclarations("data/day6.txt")
    cd.split_and_count_unique_answers()
    cd.split_and_count_everyone_yes()
