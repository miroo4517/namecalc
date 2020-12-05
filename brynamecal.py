from browser import document
from browser import html

document[""]

import os
import sys
import re

consonent_first = ord('ㄱ')
consonent_last = ord('ㅎ')
vowel_first = ord('ㅏ')
vowel_last = ord('ㅣ')
syllable_first = ord('가')
syllable_last = ord('힣')

list_initial = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
list_medial = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']
list_final = ['','ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']

def isHangul(text):
    #Check the Python Version
    pyVer3 =  sys.version_info >= (3, 0)

    if pyVer3 : # for Ver 3 or later
        encText = text
    else: # for Ver 2.x
        if type(text) is not unicode:
            encText = text.decode('utf-8')
        else:
            encText = text

    hanCount = len(re.findall(u'[\u3130-\u318F\uAC00-\uD7A3]+', encText))
    return hanCount > 0

def sep(syl):
    uind = ord(syl)

    if uind >= consonent_first and uind <= consonent_last:
        return syl, '', ''

    elif uind >= vowel_first and uind <= vowel_last:
        return '', syl, ''

    elif uind >= syllable_first and uind <= syllable_last:
        ind = ord(syl) - syllable_first
        ind_final = ind % len(list_final)
        ind_medial = (ind // len(list_final)) % len(list_medial)
        ind_initial = (ind // len(list_final)) // len(list_medial)

        return list_initial[ind_initial], list_medial[ind_medial], list_final[ind_final]

    else:   # Not a korean syllable
        return '', '', ''


if __name__ == '__main__':
    document[""].textContent = ""

    from itertools import zip_longest

    document <= 'Name Match Calc\n\nBy MiRoo(fb.me/miroonest)\n본 계산기는 namnyang님이 변환하신 github.com/ilhwanh/name-divination의 코드를 차용하였습니다.' + html.BR() + '-------------------------------' + html.BR()

    stroketype = int(input('선 하나 당 1로 계산하려면 1, 획 하나 당 1로 계산하려면(ㅈ=2, ㅊ=3, ㅃ=8, ㅆ=4) 2를, 획 하나 당 1로 계산하려면(ㅈ=3, ㅊ=4, ㅃ=5, ㅆ=3) 3을, 인터넷에 떠도는 이름점 계산법은 4를 입력하세요 : '))
    
    if stroketype == 1:
	    map_strokes = {
            '': 0, 
	        'ㄱ': 2, 'ㄲ': 4, 'ㄳ': 4, 'ㄴ': 2, 'ㄵ': 5, 'ㄶ': 5, 'ㄷ': 3, 'ㄸ': 6 ,'ㄹ': 5, 'ㄺ': 7, 'ㄻ': 9, 'ㄼ': 9, 'ㄽ': 7, 
	        'ㄾ': 9, 'ㄿ': 9, 'ㅀ': 8, 'ㅁ': 4, 'ㅂ': 4, 'ㅃ': 8, 'ㅄ': 6, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 3, 'ㅉ': 6 ,'ㅊ': 4, 
	        'ㅋ': 3, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3,
	        'ㅏ': 2, 'ㅐ': 3, 'ㅑ': 3, 'ㅒ': 4, 'ㅓ': 2, 'ㅔ': 3, 'ㅕ': 3, 'ㅖ': 4, 'ㅗ': 2, 'ㅘ': 4, 'ㅙ': 5, 'ㅚ': 3, 'ㅛ': 3, 
	        'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 5, 'ㅟ': 3, 'ㅠ': 3, 'ㅡ': 1, 'ㅢ': 2, 'ㅣ': 1
	    }
    elif stroketype == 2:
	    map_strokes = {
 	       '': 0, 
 	       'ㄱ': 1, 'ㄲ': 2, 'ㄳ': 3, 'ㄴ': 1, 'ㄵ': 3, 'ㄶ': 4, 'ㄷ': 2, 'ㄸ': 4 ,'ㄹ': 3, 'ㄺ': 4, 'ㄻ': 6, 'ㄼ': 7, 'ㄽ': 5, 
 	       'ㄾ': 7, 'ㄿ': 7, 'ㅀ': 6, 'ㅁ': 3, 'ㅂ': 4, 'ㅃ': 8, 'ㅄ': 6, 'ㅅ': 2, 'ㅆ': 4, 'ㅇ': 1, 'ㅈ': 2, 'ㅉ': 4 ,'ㅊ': 3, 
 	       'ㅋ': 2, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3,
 	       'ㅏ': 2, 'ㅐ': 3, 'ㅑ': 3, 'ㅒ': 4, 'ㅓ': 2, 'ㅔ': 3, 'ㅕ': 3, 'ㅖ': 4, 'ㅗ': 2, 'ㅘ': 4, 'ㅙ': 5, 'ㅚ': 3, 'ㅛ': 3, 
 	       'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 5, 'ㅟ': 3, 'ㅠ': 3, 'ㅡ': 1, 'ㅢ': 2, 'ㅣ': 1
	    }
    elif stroketype == 3:
	    map_strokes = {
	        '': 0, 
	        'ㄱ': 1, 'ㄲ': 2, 'ㄳ': 3, 'ㄴ': 1, 'ㄵ': 3, 'ㄶ': 4, 'ㄷ': 2, 'ㄸ': 4 ,'ㄹ': 3, 'ㄺ': 4, 'ㄻ': 6, 'ㄼ': 7, 'ㄽ': 5, 
	        'ㄾ': 7, 'ㄿ': 7, 'ㅀ': 6, 'ㅁ': 3, 'ㅂ': 4, 'ㅃ': 5, 'ㅄ': 6, 'ㅅ': 2, 'ㅆ': 3, 'ㅇ': 1, 'ㅈ': 3, 'ㅉ': 4 ,'ㅊ': 4, 
	        'ㅋ': 2, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 3,
	        'ㅏ': 2, 'ㅐ': 3, 'ㅑ': 3, 'ㅒ': 4, 'ㅓ': 2, 'ㅔ': 3, 'ㅕ': 3, 'ㅖ': 4, 'ㅗ': 2, 'ㅘ': 4, 'ㅙ': 5, 'ㅚ': 3, 'ㅛ': 3, 
	        'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 5, 'ㅟ': 3, 'ㅠ': 3, 'ㅡ': 1, 'ㅢ': 2, 'ㅣ': 1
	    }
    elif stroketype == 4:
	    map_strokes = {
	        '': 0, 
	        'ㄱ': 1, 'ㄲ': 2, 'ㄳ': 5, 'ㄴ': 2, 'ㄵ': 6, 'ㄶ': 6, 'ㄷ': 3, 'ㄸ': 6 ,'ㄹ': 1, 'ㄺ': 2, 'ㄻ': 4, 'ㄼ': 3, 'ㄽ': 5, 
	        'ㄾ': 5, 'ㄿ': 5, 'ㅀ': 5, 'ㅁ': 3, 'ㅂ': 2, 'ㅃ': 4, 'ㅄ': 6, 'ㅅ': 4, 'ㅆ': 8, 'ㅇ': 4, 'ㅈ': 4, 'ㅉ': 8 ,'ㅊ': 4, 
	        'ㅋ': 2, 'ㅌ': 4, 'ㅍ': 4, 'ㅎ': 4,
	        'ㅏ': 3, 'ㅐ': 4, 'ㅑ': 3, 'ㅒ': 5, 'ㅓ': 2, 'ㅔ': 2, 'ㅕ': 2, 'ㅖ': 4, 'ㅗ': 3, 'ㅘ': 6, 'ㅙ': 7, 'ㅚ': 4, 'ㅛ': 2, 
	        'ㅜ': 2, 'ㅝ': 4, 'ㅞ': 4, 'ㅟ': 3, 'ㅠ': 2, 'ㅡ': 1, 'ㅢ': 4, 'ㅣ': 1
	    }
    else:
	    document <= '값이 올바르지 않습니다' + html.BR();os._exit(1)

    name1 = input('첫번째 사람의 이름 : ')
    name2 = input('두번째 사람의 이름 : ')

    if abs(len(name1) - len(name2)) == 1:
        if len(name1) < len(name2):
            tmp = name1
            name1 = name2
            name2 = tmp

    if str(isHangul(name1)) == 'False' or abs(len(name1)) < 2 or abs(len(name1)) > 4 :
    document <= '값이 올바르지 않습니다' + html.BR();os._exit(1)

    if str(isHangul(name2)) == 'False' or abs(len(name2)) < 2 or abs(len(name2)) > 4 :
    document <= '값이 올바르지 않습니다' + html.BR();os._exit(1)

    sep1 = [sum([map_strokes[s] for s in sep(c)]) % 10 for c in name1]
    sep2 = [sum([map_strokes[s] for s in sep(c)]) % 10 for c in name2]

    score = [s for s in sum(zip_longest(sep1, sep2, fillvalue=None), ()) if s is not None]
    names = [s for s in sum(zip_longest(name1, name2, fillvalue=None), ()) if s is not None]

    document <= '  '.join(names) + html.BR()
    spaces = 1

    while True:
        document <= ' ' * spaces + '   '.join([str(s) for s in score]) + html.BR()

        if len(score) <= 2:
            break

        score_old = score
        score_new = []

        for i in range(len(score) - 1):
            score_new.append((score[i] + score[i + 1]) % 10)

        score = score_new
        spaces += 2

    document <= '-------------------------------' + html.BR()
    document <= '계산 결과: {}%'.format(score[0] * 10 + score[1])
    document <= html.BR() + '-------------------------------' + html.BR() + "다시 하시려면 로드를 다시 해주세요." + html.BR() + html.BR()