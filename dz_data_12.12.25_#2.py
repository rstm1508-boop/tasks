def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


import unittest


class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        # Проверяем обработку пустой строки
        self.assertEqual(count_vowels(''), 0)
        
    def test_no_vowels(self):
        # Проверяем случай, когда строка не содержит гласных
        self.assertEqual(count_vowels('bcdfghjklmnpqrstvwxyz'), 0)
        
    def test_mixed_case(self):
        # Проверяем правильность подсчета при смешанном регистре
        self.assertEqual(count_vowels('Hello World'), 3)
        
    def test_all_uppercase(self):
        # Проверяем работу с заглавными буквами
        self.assertEqual(count_vowels('AARDVARK'), 3)
        
    def test_lowercase(self):
        # Проверяем работу со строчными буквами
        self.assertEqual(count_vowels('banana'), 3)
        
    def test_special_characters(self):
        # Проверяем игнорирование специальных символов
        self.assertEqual(count_vowels('@#$%^&*()'), 0)
        
if __name__ == '__main__':
    unittest.main()