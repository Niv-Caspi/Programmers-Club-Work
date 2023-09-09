""""
משימה: כתוב תוכנית פייתון שלוקחת מספר עשרוני כקלט, ממירה אותו לייצוג הבינארי שלו
 ולאחר מכן מיישמת את שיטת המשלים לשתיים כדי להחזיר את הייצוג הבינארי 

דרישות
התוכנית צריכה לקבל מספר עשרוני חיובי כקלט מהמשתמש
יישם את הקוד הדרוש להמרת המספר העשרוני לייצוג הבינארי שלו
החל את שיטת ההשלמה של השניים כדי לקבל את הייצוג הבינארי השלילי
הדפס את הייצוג הבינארי השלילי של המספר העשרוני הקלט
"""


def twos_complement(bin_num):
    bin_num = bin(int(bin_num)).replace("0b", "00")
    reversed_num = ""
    for ch in bin_num:
        if ch =="0":
            reversed_num += "1"
        if ch =="1":
            reversed_num += "0"    

    one = ""
    for i in range(1, len(bin_num)):
        one += "0"
    one += "1"

    sum = bin(int(reversed_num, 2) + int(one, 2))
    return int(sum.replace("0b", "00"))

def main():
    inp = input("Enter A Number: ")
    
    print("Dec: -", inp ,", Bin:" ,twos_complement(inp))

if __name__ == "__main__":
    main()