#!/usr/bin/env python3
# coding: utf-8

"""
    みずぴー日記 「整数の漢数字表記」を真似して作ってみる
    http://d.hatena.ne.jp/mzp/20070814/jpnum
"""


class   Kansuji():
    """
        Kansuji クラス
        漢数字を扱う。
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
        return  self._number
    
    @number.setter
    def number(self,number):
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
        '''漢数字文字列'''
        if  self._kansuji   ==  '':
            self._kansuji   =   self._helper_large(self.number)
        return  self._kansuji

def number_to_kansuji(number):
    ks  =   Kansuji()
    ks.number   =   number
    return  ks.kansuji

if __name__ == '__main__':
    import sys
    
    #print(sys.argv[1])

    num =   int(sys.argv[1])
    
    print(number_to_kansuji(num))
    
    
    
