from utils.date_string_parse import DateStringParser


print "====TEST SLASH FORMAT===="
print "Test Case 1"
DateStringParser.parse("12/12/98")
print "Test Case 2"
DateStringParser.parse("12/12/2014")
print "Test Case 3"
DateStringParser.parse("12/12/20")
print "Test Case 4"
DateStringParser.parse("12/12/50")
print "Test Case 5"
DateStringParser.parse("12/12/60")
print "Test Case 6"
DateStringParser.parse("12/12/70")
print "Test Case 7"
DateStringParser.parse("12/12/80")
print "Test Case 8"
DateStringParser.parse("12/12/90")
print "Test Case 9"
DateStringParser.parse("12/12/99")
print "Test Case 10"
DateStringParser.parse("12/12/992")
print "Test Case 11"
DateStringParser.parse("122/12/992")
print "Test Case 12"
DateStringParser.parse("12/122/99")
print "Test Case 13"
DateStringParser.parse("121312312")
print "Test Case 14"
DateStringParser.parse("efefd")
print "Test Case 15"
DateStringParser.parse("1989/29/24")

print "====TEST DASH FORMAT===="
print "Test Case 1"
DateStringParser.parse("12-12-98")
print "Test Case 2"
DateStringParser.parse("12-12-2014")
print "Test Case 3"
DateStringParser.parse("12-12-20")
print "Test Case 4"
DateStringParser.parse("12-12-50")
print "Test Case 5"
DateStringParser.parse("12-12-60")
print "Test Case 6"
DateStringParser.parse("12-12-70")
print "Test Case 7"
DateStringParser.parse("12-12-80")
print "Test Case 8"
DateStringParser.parse("12-12-90")
print "Test Case 9"
DateStringParser.parse("12-12-99")
print "Test Case 10"
DateStringParser.parse("12-12-992")
print "Test Case 11"
DateStringParser.parse("122-12-992")
print "Test Case 12"
DateStringParser.parse("12-122-99")
print "Test Case 13"
DateStringParser.parse("121312312")
print "Test Case 14"
DateStringParser.parse("efefd")
print "Test Case 15"
DateStringParser.parse("1989-29-24")