import mysql.connector
import random, datetime, time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1111",
  database="industrial_control_system"
)
mycursor = mydb.cursor()

def Menu():
    print("SIMULATOR MESIN")
    print("1. Memasukkan data simulasi motor berulang")
    print("2. Memasukkan data simulasi hvac berulang")
    print("3. Memasukkan data simulasi pompa berulang")
    print("4. Memasukkan data simulasi motor, hvac, pompa bersamaan secara berulang")
    print("---------------------")
    print("5. Exit Program")
    print()
    choice = int(input("Enter here: "))

    if(choice==1):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(50,70)
            status = "ON"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mydb.commit()
            print(mycursor.rowcount, "record kondisi motor dimasukkan.")

    if(choice==2):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(50,70)
            status = "ON"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mydb.commit()
            print(mycursor.rowcount, "record kondisi hvac dimasukkan.")

    if(choice==3):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(50,70)
            status = "ON"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mydb.commit()
            print(mycursor.rowcount, "record kondisi pompa dimasukkan.")

    if(choice==4):
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature1 = random.randint(50,70)
            temperature2 = random.randint(50,70)
            temperature3 = random.randint(50,70)
            status = "ON"
            
            mycursor = mydb.cursor()
            mycursor.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature1))
            mycursor.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature2))
            mycursor.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature3))
            mydb.commit()
            print(mycursor.rowcount, "record kondisi motor, hvac, pompa dimasukkan.")          

    if(choice==5):
        exit()

    lagi=input("\nTry again (Y/y) ? ")
    if lagi.lower() == "y" :
        Menu ()
    else :
        print("Program has done")


Menu()


