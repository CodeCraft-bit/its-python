#esercizio_8.10


message_list:str = ["Ciao", "come", "stai"]

def show_messages(lista):
    for i in lista:
        print(i)

show_messages(message_list)

c_c=[]
def send_messages(sent):
    for i in sent:
        m_m = sent.pop()
        print(m_m)
        c_c.append(m_m)

send_messages(message_list)
print(message_list)
print(c_c)