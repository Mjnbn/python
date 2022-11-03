persian_numbers = '۱۲۳۴۵۶۷۸۹۰'
english_numbers = '1234567890'
arabic_numbers = '١٢٣٤٥٦٧٨٩٠'

string = input()

persion_trans = string.maketrans(persian_numbers, english_numbers)


arabic_trans = string.maketrans(arabic_numbers, english_numbers)

x = (string.translate(persion_trans)).translate(arabic_trans)
print(x)