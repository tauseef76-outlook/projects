def arithmetic_arranger(numbers, solve=False):

    start = True
    space_btwn = "    "
    line1 = line2 = line3 = line4 = ""

    for items in numbers:
        firstNum, oper, secNum = items.split(" ")
        firstNum = firstNum.strip()
        secNum = secNum.strip()
        oper = oper.strip()

        if len(numbers) > 5:
            return ("Error: Too many problems.")

        if oper not in ["+", "-"]:
            return("Error: Operator must be '+' or '-'.")
        if (firstNum.isdigit() == False or secNum.isdigit() == False):
            return("Error: Numbers must only contain digits.")
        if (len(firstNum) > 4 or len(secNum) > 4):
            return("Error: Numbers cannot be more than four digits.")

        maxlen = max(len(firstNum), len(secNum))

        if(start):
            line1 += firstNum.rjust(maxlen+2)
            line2 += oper+" "+secNum.rjust(maxlen-1)
            line3 += "-"*(maxlen+2)
            no1 = int(firstNum)
            no2 = int(secNum)
            res = 0
            if(oper == "+"):
                res = no1+no2
            else:
                res = no1-no2
            
            line4 += str(res).rjust(maxlen+2)
            start = False
        else:
            line1 +=firstNum.rjust(maxlen+6)
            line2 +=oper.rjust(5)+" "+secNum.rjust(maxlen-1)
            line3 +=space_btwn+ "-"*(maxlen+2)
            no1 = int(firstNum)
            no2 = int(secNum)
            res = 0
            if(oper == "+"):
                res = no1+no2
            else:
                res = no1-no2
            line4 += space_btwn+str(res).rjust(maxlen+2)
            
    print(line1,"\n",line2,"\n"+line3+"\n"+line4)


if __name__ == "__main__":
    numbers = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
    (arithmetic_arranger(numbers))
