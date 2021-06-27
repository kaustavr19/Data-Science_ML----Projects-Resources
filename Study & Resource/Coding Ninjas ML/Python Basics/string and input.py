#strings
a = "This is a string"
print(a)

#typical string properties
print(len(a))
print(type(a))
print(a[0])
#strings are immutable
#a[0] = 2   INVALID
a = "def"  #valid as we aren't changing the string
b = "abc"
c = a+b
print(c)
#d = a+2     INVALID

#no characters
print(type('2'))

#few functions for strings

a = "   Abc  "
print(a.upper())
print(a)
print(a.lower())
print(a.strip())
a = a.strip()
print(a.isalpha())

#user input
a = input()
print(a)

#input() return a str
a = int(input())
print(a)
print(type(a))


