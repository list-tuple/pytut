"""
string operations

#strip  => strips the character before and after the string
#upper  => converts the existing string to upper case
#lower  => converts the existing string to lower case
#title  => convert the existing string to title case
#isalpha => checks the string contains only alphabets
#isdigit  =>check the string contains ony numbers
#lstrip  => strips only left side
#rstrip => strips only right side
#startswith
#endwith

"""
>>> s1="123"
>>> s1.isalpha()
False
>>> s1.upper()
'123'
>>> s1="Today is saturday"
>>> s1
'Today is saturday'
>>> s1.upper()
'TODAY IS SATURDAY'
>>> s1.title()
'Today Is Saturday'
>>> s2="THIS IS JULY MONTH"
>>> s1
'Today is saturday'

>>> s2
'THIS IS JULY MONTH'
>>> s1.isalpha()
False
>>> s3="JULY"

>>> s3.isalpha()
True
>>> s3.isdigit()
False
>>> s4="2022"
>>> s4.isdigit()
True
>>> s5="_JULY_"
>>> s5.strip("_")
'JULY'
>>> s4
'2022'
>>> s4.strip("_")
'2022'
>>> s4.strip("2")
'0'
>>> s5
'_JULY_'
>>> s5.lstrip("_")
'JULY_'
>>> s5.rstrip("_")
'_JULY'

>>> s5
'_JULY_'
>>> s5.startswith("_")
True
>>> s5.startswith("a")
False
>>> s5.endswith("x")
False
>>> s5.endswith("_")
True
