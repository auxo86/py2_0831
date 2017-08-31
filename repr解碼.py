new_string = '\xe5\xad\x97'
print str(new_string), repr(new_string)

# new_latin = new_string.decode('latin-1')
# print str(new_latin), repr(new_string)


new_utf8 = new_string.decode('utf-8')
print new_utf8, repr(new_utf8)
