import re


def extract_calibration_val(string: str) -> int:
    digits = re.findall(r'\d', string)
    first_and_last_digit = [digits[0], digits[-1]]
    return int("".join(first_and_last_digit))


def sum_calibration_values(calibration_document: list[str]) -> int:
    return sum(extract_calibration_val(d) for d in calibration_document)


def main() -> None:
    with open("data/day1.txt") as f:
        calibration_documents = f.read().splitlines()

    result = sum_calibration_values(calibration_documents)
    print(f"The result is {result}.")


if __name__ == "__main__":
    main()