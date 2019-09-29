# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:58:23 2019

@author: daloaiza
"""

import unittest
# unittest hace parte de la librería standard de Python y se basa en JUnit
 

class RomanNumeralTestCase(unittest.TestCase):
    """Tests para la clase roman_numeral_generator.py. """
 
    # Las funciones setUp y tearDown sirven para automatizar el proceso de
    # crear una instancia de la clase para cada test
    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testclass = RomanNumeralGenerator()
 
    def tearDown(self):
        unittest.TestCase.tearDown(self)
 
    # Primera prueba
    def test_one_arabic_1_receives_I_roman(self):
        """ Si recibe 1 return I? """
        result = self.testclass.generator(1)
        self.assertEqual(result, 'I')
    
    # Segunda prueba    
    def test_two_arabic_2_receives_II_roman(self):
        """ Si recibe 2 return II? """
        result = self.testclass.generator(2)
        self.assertEqual(result, 'II')

    # Tercera prueba
    def test_three_arabic_3_receives_III_roman(self):
        """ Si recibe 3 return III? """
        result = self.testclass.generator(3)
        self.assertEqual(result, 'III')

    # Cuarta prueba    
    def test_four_arabic_4_receives_IV_roman(self):
        """ Si recibe 4 return IV? """
        result = self.testclass.generator(4)
        self.assertEqual(result, 'IV')
        
    def test_five__arabic_5_receives_V_roman(self):
        """ Si recibe 5 return IV? """
        result = self.testclass.generator(5)
        self.assertEqual(result, 'V')
        
    def test_six_arabic_6_receives_VI_roman(self):
        """ Si recibe 6 return VI? """
        result = self.testclass.generator(6)
        self.assertEqual(result, 'VI')
        
    def test_seven_arabic_7_receives_VII_roman(self):
        """ Si recibe 7 return VII? """
        result = self.testclass.generator(7)
        self.assertEqual(result, 'VII')

    def test_eight_arabic_8_receives_VIII_roman(self):
        """ Si recibe 8 return VIII? """
        result = self.testclass.generator(8)
        self.assertEqual(result, 'VIII')

    def test_nine_arabic_9_receives_IX_roman(self):
        """ Si recibe 9 return IX? """
        result = self.testclass.generator(9)
        self.assertEqual(result, 'IX')

    def test_ten_arabic_10_receives_X_roman(self):
        """ Si recibe 10 return X? """
        result = self.testclass.generator(10)
        self.assertEqual(result, 'X')
        
    def test_eleven_arabic_11_receives_XI_roman(self):
        """ Si recibe 11 return XI? """
        result = self.testclass.generator(11)
        self.assertEqual(result, 'XI')
        
    def test_eighteen_arabic_18_receives_XVIII_roman(self):
        """ Si recibe 18 return XVIII? """
        result = self.testclass.generator(18)
        self.assertEqual(result, 'XVIII')

    # Quinta Prueba        
    def test_nineteen_arabic_19_receives_XIX_roman(self):
        """ Si recibe 19 return XIX? """
        result = self.testclass.generator(19)
        self.assertEqual(result, 'XIX')
        
    def test_twenty_arabic_20_receives_XX_roman(self):
        """ Si recibe 20 return XX? """
        result = self.testclass.generator(20)
        self.assertEqual(result, 'XX')
        
    def test_forty_arabic_40_receives_XL_roman(self):
        """ Si recibe 40 return XL? """
        result = self.testclass.generator(40)
        self.assertEqual(result, 'XL')

    def test_ninetynine_arabic_99_receives_XCIX_roman(self):
        """ Si recibe 99 return IC? """
        result = self.testclass.generator(99)
        self.assertEqual(result, 'XCIX')
 
    def test_onethousandninehundredninetynine_arabic_1999_receives_MCMXCIX_roman(self):
        """ Si recibe 1999 return IC? """
        result = self.testclass.generator(1999)
        self.assertEqual(result, 'MCMXCIX')
    
if __name__ == '__main__':
    unittest.main()
    
class RomanNumeralGenerator(object):
 
    def generator(self, arabic):
        roman = self.to_roman(arabic)
        return roman
    """
    # Función para pasar la primera prueba
    def to_roman(self, number):
        if(number == 1):
            return('I')

    # Función para pasar la segunda prueba
    def to_roman(self, number):
        if(number == 2):
            return('II')
        else:
            return('I')
    
    # Función para pasar la tercera prueba
    def to_roman(self, number):
    	roman_number = ""
    	while (number > 0):
    		roman_number += "I"
    		number -= 1
    	return roman_number
    
    # Función para pasar la cuarta prueba
    def to_roman(self, number):
        roman_number = ""
        arabic_remainder = number
        
        if (arabic_remainder == 9):
            roman_number = 'IX'
            arabic_remainder -= 9
 
        if (arabic_remainder == 4):
            roman_number = 'IV'
            arabic_remainder -= 4
 
        if (arabic_remainder >= 10):
            roman_number += 'X'
            arabic_remainder -= 10
        
        if (arabic_remainder >= 5):
            roman_number += 'V'
            arabic_remainder -= 5
        
        while (arabic_remainder > 0):
            roman_number += "I"
            arabic_remainder -= 1
            
        return roman_number
    """
    
    # Quinta prueba
    def to_roman(self, number):
        """ Convert an integer to a Roman numeral. """

        if not isinstance(number, type(1)):
            raise TypeError("esperaba un entero, pero recibió %s" % type(number))

        if not 0 < number < 4000:
            raise ValueError("El número debe estar ebtre 1 y 3999")
            
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        
        result = []
        roman_number = ""
        for i in range(len(ints)):
            count = int(number / ints[i])
            result.append(nums[i] * count)
            number -= ints[i] * count

        roman_number = ''.join(result)
        
        return roman_number
    
    
    
    
    
    
    