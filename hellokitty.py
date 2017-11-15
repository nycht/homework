>>> y='Hello Kitty Hello Hello Kitty Kitty Hello Kitty'
>>> re.findall('(?:Hello ){2}(?:Kitty ){2}', y)
['Hello Hello Kitty Kitty ']
