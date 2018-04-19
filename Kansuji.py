#!/usr/bin/env python3
# coding: utf-8

class   Kansuji():
    """
        Kansuji クラス
        漢数字を扱う。
        
        >>> from Kansuji import Kansuji
        >>> ks = Kansuji()
        
        >>> ks.number = 12345
        >>> ks.kansuji
        '一万二千三百四十五'

        >>> ks.number = 1234567890123456
        >>> ks.kansuji
        '千二百三十四兆五千六百七十八億九千十二万三千四百五十六'

        >>> ks.number = 0
        >>> ks.kansuji
        '零'

        >>> ks.number = -1
        Traceback (most recent call last):
            ...
        AssertionError: number must be >= 0, but number = -1

        >>> ks.number = '10'
        Traceback (most recent call last):
            ...
        AssertionError: number expects int class, but <class 'str'>
    """

    _digits_chinese  =   {
            '1': '一',
            '2': '二',
            '3': '三',
            '4': '四',
            '5': '五',
            '6': '六',
            '7': '七',
            '8': '八',
            '9': '九',
    }
    
    _units_large =   [
        { 'CHAR': '兆', 'UNIT': 10000 ** 3, },
        { 'CHAR': '億', 'UNIT': 10000 ** 2, },
        { 'CHAR': '万', 'UNIT': 10000 ** 1, },
        { 'CHAR': '',   'UNIT': 10000 ** 0, },
    ]
    
    _units_small =   [
        { 'CHAR': '千', 'UNIT': 10 ** 3, },
        { 'CHAR': '百', 'UNIT': 10 ** 2, },
        { 'CHAR': '十', 'UNIT': 10 ** 1, },
        { 'CHAR': '',   'UNIT': 10 ** 0, },
    ]

    def __init__(self):
        self._kansuji   =   ''
    
    @property
    def number(self):
        """
            数値(int)
        """
        return  self._number
    
    @number.setter
    def number(self,number):

        assert isinstance(number, int), "number expects int class, but {type}".format(type=type(number))
        assert number >= 0, "number must be >= 0, but number = {number}".format(number=number)

        self._number    =   number
        return  self
    
    def _helper_large(self,number):
        """
            _helper_large
        """
        if  number == 0:
            return  ''
        
        for unit    in  self._units_large:
            if  number  <   unit['UNIT']:
                continue
    
            upper   =   self._helper_small( number // unit['UNIT'] )
            
            lower   =   self._helper_large( number %  unit['UNIT'] )
            unit_char   =   unit['CHAR']
            
            return  '{upper}{unit_char}{lower}'.format(
                    upper=upper, unit_char=unit_char, lower=lower )
        
        raise   ValueError("number='{number}' is invalid.".format( number=number ))
    
    def _helper_small(self,number):
        """
            _helper_small
        """
        if  number == 0:
            return  ''
        
        for unit    in  self._units_small:
            if  number  <   unit['UNIT']:
                continue
    
            upper   =   self._digits_chinese[ str(number // unit['UNIT']) ]
            
            # 「十」,「百」,「千」の前の「一」は省略する
            if  upper   ==  '一'    and unit['CHAR'] !=  '':
                upper   =   ''
            
            lower   =   self._helper_small( number % unit['UNIT'] )
            unit_char   =   unit['CHAR']
            
            return  '{upper}{unit_char}{lower}'.format(
                    upper=upper, unit_char=unit_char, lower=lower )
        
        raise   ValueError("number='{number}' is invalid.".format( number=number ))
    
    @property
    def kansuji(self):
        '''漢数字文字列(ReadOnly)'''
        self._kansuji   =   self._helper_large(self.number) if self.number > 0 else '零'
        return  self._kansuji

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
    
