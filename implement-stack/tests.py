from option2 import IntStack
import unittest

class TestIntStack(unittest.TestCase):
    
    def setUp(self):
        self.stack = IntStack() 
    
    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0) 
        
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 3)
        
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2) 

    def test_peek(self):
        self.stack.push(1)
        self.stack.push(2)
        
        self.assertEqual(self.stack.peek(), 2) 
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)  
        
        self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()

if __name__ == "__main__":
    unittest.main()