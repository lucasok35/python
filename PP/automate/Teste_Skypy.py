from skpy import Skype

#Conectando a conta Skype
sk = Skype('lhsilva-premierpet@outlook.com', 'Lhts1994')

sk.user #Eu
sk.contacts #Meus contatos
sk.chats #Minhas conversas

ch = sk.chats.create(["joe.4", "daisy.5"]) #Novo grupo de conversa
ch = sk.contacts["joe.4"].chat #Conversa 1 a 1

ch.sendMsg('Olá vamos conversar?') #Mensagem simples
ch.sendFile(open("song.mp3", "rb"), "song.mp3") #Upload de arquivo
ch.sendcontact(sk.contacts["daisy.5"]) #Compartilhando contato

ch.getMsgs() #Recuperando mensagens recentes
