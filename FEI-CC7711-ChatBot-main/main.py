from chatbot import ChatBot
myChatBot = ChatBot()

#apenas carregar um modelo pronto
#myChatBot.loadModel()

#criar o mode
myChatBot.createModel()


print("Bem vindo ao Chatbot")


pergunta = input("O que deseja saber sobre o TCC?\n")
resposta, intencao = myChatBot.chatbot_response(pergunta)
print(resposta + "   ["+intencao[0]['intent']+"]")

while (intencao[0]['intent']!="despedida"):
    if(intencao[0]['intent']=="TCC_Entrega"):
        pergunta = input("Gostaria de saber mais sobre a entrega?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")
    if(intencao[0]['intent']=="TCC_Orientador"):
        resposta, intencao = myChatBot.chatbot_response("para que serve o professor de TCC?")
        print("Então para que serve o professor de TCC?")
        print(resposta + "   [" + intencao[0]['intent'] + "]")

    else:
        pergunta = input("posso lhe ajudar com algo a mais?\n")
        resposta, intencao = myChatBot.chatbot_response(pergunta)
        print(resposta + "   [" + intencao[0]['intent'] + "]")

print("Foi um prazer atendê-lo")
