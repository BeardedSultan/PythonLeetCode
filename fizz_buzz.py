#NAIVE_SOLUTION#
'''
class Solution:
    def fizzBuzz(self, n):
        output = []

        for i in range(1, n + 1):

            divby3 = (i % 3 == 0)
            divby5 = (i % 5 == 0)

            if divby3 and divby5:
                output.append("FizzBuzz")
            elif divby3:
                output.append("Fizz")
            elif divby5:
                output.append("Buzz")
            else:
                output.append(str(i))

        for string in output:
            print(string)
        return output
'''
'''
#STRING_CONCATENATION_SOLUTION#
class Solution:
    def fizzBuzz(self, n):
        output = []

        for i in range(1, n + 1):

            outputstr = ""
            divby3 = (i % 3 == 0)
            divby5 = (i % 5 == 0)

            if divby3:
                outputstr += "Fizz"
            if divby5:
                outputstr += "Buzz"
            if outputstr == "":
                outputstr += str(i)
            
            output.append(outputstr)

        for string in output:
            print(string)
        return output
'''

#MAP_SOLUTION(DICTIONARY)#
class Solution:
    def fizzBuzz(self, n):
        output = []
        map = { 3 : 'Fizz', 5 : 'Buzz' }

        for i in range(1, n + 1):
            outputstr = ""

            for key in map.keys():
                if i % key == 0:
                    outputstr += map[key]
                    
            if outputstr == "":
                outputstr += str(i)
            
            output.append(outputstr)

        for string in output:
            print(string)
        return output