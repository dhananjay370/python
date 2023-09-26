import mysql.connector
from mysql.connector import Error


class OpenAcc:
    __accnm = 1001
    __usernm = None
    __acctype = None
    __bal = None
    __phoneno = None
    __branch = 'Gadge Nagar'
    __city = 'Amravati'

    def __init__(self, un, at, pn, b):
        self.__usernm = un
        self.__bal = b
        self.__acctype = at
        self.__phoneno = pn

    def openAcc(self):
        try:
            con = mysql.connector.connect(
                host='localhost', user='root', password='password', database='ac')
            c = con.cursor()
            qf = f"select account_no from accounts;"
            c.execute(qf)
            ano = c.fetchall()
            l = len(ano)
            self.__accnm = int(ano[l-1][0]) + 1
            q1 = f"insert into accounts values({self.__accnm}, \"{self.__usernm}\", \"{self.__acctype}\",{self.__bal});"
            q2 = f"insert into userdata values({self.__accnm},NULL,{self.__phoneno},\"{self.__branch}\",\"{self.__city}\");"

            c.execute(q1)
            c.execute(q2)

            con.commit()

            print(
                f"Account created successfully \nYour Account Number is : {self.__accnm} \nThanks for choosing us{self.__usernm}")

        except Error as e:
            print(f"Error is : {e}")
