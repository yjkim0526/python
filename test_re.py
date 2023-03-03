import re


patten = r'[ぁ-ゔァ-ヴー々〆〤一-龥]'
str1 = "こんにちは. 123 a hello pi コンビニエンスストア apc 001 "

# re.match (패턴, 대상문자) - 패턴에 해당하는 첫 문자 찾기
match1 = re.match(patten, str1)
print(">> match1 : ", match1)

## re.findall (패턴, 대상문자) - 패턴에 해당하는 문자 모두 찾기
find1 = re.findall(patten, str1)
print(">> find1 : ", find1)

## re.sub (패턴, 치환할문자, 대상문자)
sub1 = re.sub(patten, '', str1)
print(">> sub1 : ", sub1)

