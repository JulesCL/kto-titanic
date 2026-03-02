import unittest

LETTER_COUNT_THRESHOLD = 7


def names(first_names: list[str]) -> int:
    names_above_threshold = 0
    for first_name in first_names:
        if len(first_name) > LETTER_COUNT_THRESHOLD:
            names_above_threshold += 1
            print(f"{first_name} est un prénom avec un nombre de lettres supérieur à {LETTER_COUNT_THRESHOLD}")
        else:
            print(f"{first_name} est un prénom avec un nombre de lettres inférieur ou égal à {LETTER_COUNT_THRESHOLD}")
    return names_above_threshold


class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(first_names=prenoms)
        self.assertEqual(more_than_seven, 4)


if __name__ == "__main__":
    unittest.main()