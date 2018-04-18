#!/usr/bin/env python3
# coding: utf-8

"""
    みずぴー日記 「整数の漢数字表記」を真似して作ってみる
    http://d.hatena.ne.jp/mzp/20070814/jpnum
"""

digits_chinese  =   {
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


units_large =   [
    { 'CHAR': '兆', 'UNIT': 10000 ** 3, },
    { 'CHAR': '億', 'UNIT': 10000 ** 2, },
    { 'CHAR': '万', 'UNIT': 10000 ** 1, },
    { 'CHAR': '',   'UNIT': 10000 ** 0, },
]

units_small =   [
    { 'CHAR': '千', 'UNIT': 10 ** 3, },
    { 'CHAR': '百', 'UNIT': 10 ** 2, },
    { 'CHAR': '十', 'UNIT': 10 ** 1, },
    { 'CHAR': '',   'UNIT': 10 ** 0, },
]

def helper_large(number):
    """
        helper_large
    """
    if  number == 0:
        return  ''
    
    for unit in units_large:
        if  number  <   unit['UNIT']:
            continue

        upper   =   helper_small( number // unit['UNIT'] )
        
        lower   =   helper_large( number %  unit['UNIT'] )
        unit_char   =   unit['CHAR']
        
        return  '{upper}{unit_char}{lower}'.format(
                upper=upper, unit_char=unit_char, lower=lower )
    
    raise   ValueError("number='{number}' is invalid.".format( number=number ))

def helper_small(number):
    """
        helper_small
    """
    if  number == 0:
        return  ''
    
    for unit in units_small:
        if  number  <   unit['UNIT']:
            continue

        upper   =   digits_chinese[ str(number // unit['UNIT']) ]
        
        # 「十」,「百」,「千」の前の「一」は省略する
        if  upper   ==  '一'    and unit['CHAR'] !=  '':
            upper   =   ''
        
        lower   =   helper_small( number % unit['UNIT'] )
        unit_char   =   unit['CHAR']
        
        return  '{upper}{unit_char}{lower}'.format(
                upper=upper, unit_char=unit_char, lower=lower )
    
    raise   ValueError("number='{number}' is invalid.".format( number=number ))

if __name__ == '__main__':
    import sys
    
    print(sys.argv[1])

    num =   int(sys.argv[1])
    
    print(helper_large(num))
    
    
    
