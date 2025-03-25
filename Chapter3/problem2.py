#Program to fill in a letter template given below with name and date.
letter='''
Dear <|Name|>,
You are selected!
Date: <|Date|>'''
print(letter.replace("<|Name|>","Koshish").replace("<|Date|>","12-12-2020"))