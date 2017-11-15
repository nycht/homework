y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adf.com'
import re
re.findall('\w+@(qq|163|126|adf).com', y)
re.findall('\w+@(?:qq|163|126|adf).com', y)

