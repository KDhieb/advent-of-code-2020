# F = lower half of rows  B = upper half of rows
# L = lower half of columns  R = upper half of columns

class AirplaneSeats:
    seat_array = []
    seat_id_dict = {}

    def parse_file(self, file_name):
        read_file = open(file_name, 'r').read()
        self.seat_array = read_file.split()

    def calculate_seat_ids(self):
        for code in self.seat_array:
            row_range = [0, 127]
            col_range = [0, 7]
            row = 0
            col = 0

            for letter in code:
                low = row_range[0]
                top = row_range[1]
                left = col_range[0]
                right = col_range[1]

                if letter == "F":
                    row, row_range = self.keep_lower_half_row(low, row, row_range, top)
                elif letter == "B":
                    row, row_range = self.keep_upper_half_row(low, row, row_range, top)
                elif letter == "L":
                    col, col_range = self.keep_lower_half_column(col, col_range, left, right)
                elif letter == "R":
                    col, col_range = self.keep_upper_half_column(col, col_range, left, right)
            self.seat_id_dict[code] = row * 8 + col

    @staticmethod
    def keep_upper_half_column(col, col_range, left, right):
        if right - left == 1:
            col = col_range[1]
        else:
            new_left = round((right - left) / 2) + left
            col_range = [new_left, right]
        return col, col_range

    @staticmethod
    def keep_lower_half_column(col, col_range, left, right):
        if right - left == 1:
            col = col_range[0]
        else:
            new_right = int(((right - left) / 2) + left)
            col_range = [left, new_right]
        return col, col_range

    @staticmethod
    def keep_upper_half_row(low, row, row_range, top):
        if top - low == 1:
            row = row_range[1]
        else:
            new_low = round(((top - low) / 2) + low)
            row_range = [new_low, top]
        return row, row_range

    @staticmethod
    def keep_lower_half_row(low, row, row_range, top):
        if top - low == 1:
            row = row_range[0]
        else:
            new_top = int(((top - low) / 2) + low)
            row_range = [low, new_top]
        return row, row_range

    def find_highest_id(self):
        ids = self.seat_id_dict.values()
        sorted_ids = sorted(ids)
        return sorted_ids[-1]

    def find_my_seat_num(self):
        values = self.seat_id_dict.values()
        sorted_values = sorted(values)
        index = 0
        for num in sorted_values:
            try:
                if num + 2 == sorted_values[index + 1]:
                    return num + 1
                index += 1
            except IndexError:
                print("List Exceeded")


if __name__ == '__main__':
    ac = AirplaneSeats()
    ac.parse_file("data/day5.txt")
    ac.calculate_seat_ids()

    print("Part 1:")
    print(f"The highest seat id is: {ac.find_highest_id()}")
    print("\nPart 2:")
    print(f"My seat number is: {ac.find_my_seat_num()}")
