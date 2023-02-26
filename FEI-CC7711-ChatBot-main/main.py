from chatbot import ChatBot
myChatBot = ChatBot()

#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o mode
myChatBot.createModel()


print("Bem vindo ao Chatbot da disciplina de TCC")


pergunta = input("O que deseja saber sobre o TCC?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")
i=0

while (intencao[0]['intent']!="despedida"):
    if(intencao[0]['intent']=="TCC_Entrega"):
        pergunta = input("Qual você gostaria de saber mais sobre: monografia ou o programa?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        if((intencao[0]['intent']!="despedida")):
            print(resposta + "   [" + intencao[0]['intent'] + "]")
    if(intencao[0]['intent']=="TCC_monografia" and i==0):
        pergunta = input("Você gostaria de saber mais sobre o programa?\n")
        if(pergunta == "sim"):
            resposta, intencao = myChatBot.chatbot_response("programa")
            i+=1
            if((intencao[0]['intent']!="despedida")):
                print(resposta + "   [" + intencao[0]['intent'] + "]")
    if(intencao[0]['intent']=="TCC_Programa" and i==0):
        pergunta = input("Você gostaria de saber mais sobre o monografia?\n")
        if(pergunta == "sim"):
            resposta, intencao = myChatBot.chatbot_response("monografia")
            i+=1
            if((intencao[0]['intent']!="despedida")):
                print(resposta + "   [" + intencao[0]['intent'] + "]")
    if(intencao[0]['intent']=="TCC_Orientador"):
        resposta, intencao = myChatBot.chatbot_response("para que serve o professor de TCC?")
        print("Então para que serve o professor de TCC?")
        print(resposta + "   [" + intencao[0]['intent'] + "]")
    else:
        pergunta = input("posso lhe ajudar com algo a mais?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")
        i=0

print("Foi um prazer atendê-lo")
