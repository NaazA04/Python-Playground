questions =[
    ["Which of the following is not a programming language?","Python","Java","windows","ruby"],

    ["Which protocol is used to send emails?","HTTP","SMTP","FTP","POP"],

    ["Which device is used to connect multiple devices in a network and forward data packets?","Modem","Router","Switch","Hub"],

    ["Which of the following is a NoSQL database?","MySQL","PostgreSQL","MongoDB","Oracle"],

    ["Which of the following is an open-source operating system?","Linux","macOS","Windows","iOS"],

    ["Which of the following is a type of malware?","Firewall","Trojan","VPN","Proxy"],

    ["Which tool is used to monitor network traffic?","Notepad++","Wireshark","SQL Server","Visual Studio"],

    [" What does the acronym CIA stand for in cybersecurity?","Central Intelligence Agency","Confidentiality, Integrity, Availability","Cyber Intelligence Analytics","Control, Integrity, Authentication"],

    ["A firewall is used to:","Encrypt data during transmission"," Filter incoming and outgoing traffic","Detect and remove malware","Analyze network packets"],

    ["A Denial of Service (DoS) attack:","Exploits a software vulnerability","Sends excessive traffic to overwhelm a system","Installs malicious software on a computer","Encrypts data to demand ransom"]

]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000, 1250000, 2500000, 5000000, 10000000]
money=0

for i in range(0,len(questions)):
    question= questions[i]
    print(f"\n\nQuestion for Rs.{levels[i]}")
    print(questions[i][0])
    print(f"a.  {question[1]}                  b.  {question[2]} ")
    print(f"c.  {question[3]}                 d.  {question[4]} ")
    reply=int(input("Enter your answer (1-4):"))
    
    if i==1:
        if reply== question[3]:
            print(f"Correct answer, You have won Rs.{levels[i]}")
            if(i== 4):
                money= 10000
            elif (i==9):
                money=320000
            elif(i==14):
                money=10000000
        else:
            print("OOPS, Wrong Answer!")
            break
    elif i==2:
        if reply== question[2]:
            print(f"Correct answer, You have won Rs.{levels[i]}")
            if(i== 4):
                money= 10000
            elif (i==9):
                money=320000
            elif(i==14):
                money=10000000
        else:
            print("OOPS, Wrong Answer!")
            break
    elif i==3:
        if reply== question[2]:
            print(f"Correct answer, You have won Rs.{levels[i]}")
            if(i== 4):
                money= 10000
            elif (i==9):
                money=320000
            elif(i==14):
                money=10000000
        else:
            print("OOPS, Wrong Answer!")
            break

print(f"Your take home money is {money}")