import re


spelled_out_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5", 
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "\d": None,
}


def extract_calibration_val(string):
    pattern = "|".join(spelled_out_digits)
    digits_mixed_types = re.findall(rf"(?=({pattern}))", string)
    digits_int_types = list(map(lambda x: x if x.isdigit() else spelled_out_digits[x], digits_mixed_types))
    first_and_last_digit = [digits_int_types[0], digits_int_types[-1]]
    return int("".join(first_and_last_digit))


def sum_calibration_values(calibration_documents: list[str]) -> int:
    return sum(map(extract_calibration_val, calibration_documents))


def main() -> None:
    with open("data/day1.txt") as f:
        calibration_documents = f.read().splitlines()
    result = sum_calibration_values(calibration_documents)
    print(f"The result is {result}.")


if __name__ == "__main__":
    main()