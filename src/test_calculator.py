import unittest 
import calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calculator.add(10, 5), 15)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)
        
    def test_sub(self):
        self.assertEqual(calculator.sub(10, 5), 5)
        self.assertEqual(calculator.sub(-1, 1), -2)
        self.assertEqual(calculator.sub(0, 0), 0)
        
    def test_multiply(self):
        self.assertEqual(calculator.multiply(10, 5), 50)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(0, 100), 0)
        
    def test_div(self):
        self.assertEqual(calculator.div(10, 5), 2.0)
        self.assertEqual(calculator.div(-10, 5), -2.0)
        self.assertEqual(calculator.div(0, 5), 0)
        self.assertEqual(calculator.div(5, 0), "Cannot divide by 0")
        
if __name__ == '__main__':
    unittest.main()