#!/usr/bin/env python3
# coding: utf-8

"""
    みずぴー日記 「整数の漢数字表記」を真似して作ってみる
    http://d.hatena.ne.jp/mzp/20070814/jpnum
"""




if __name__ == '__main__':
    import sys
    from Kansuji import Kansuji
    
    num =   int(sys.argv[1])
    
    ks  =   Kansuji()
    ks.number   =   num
    
    print(ks.kansuji)
    
    
    
