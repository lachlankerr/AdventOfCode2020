import day01
import day02

if __name__ == "__main__":
    #print(f"Day 01 part 1: {day01.part_one(day01.read_input())}")
    #print(f"Day 01 part 2: {day01.part_two(day01.read_input())}")
    print(f"Day 02 part 1: {day02.regex_lines(day02.read_input(), day02.is_password_valid_part_one)}")
    print(f"Day 02 part 2: {day02.regex_lines(day02.read_input(), day02.is_password_valid_part_two)}")