#Jogo de perguntas

play = input("Vamos jogar um quizz?")
print(play)

if play.lower() == 'sim':
    score = 0
    print("Okay, vamos começar!")
    pergunta1 = input("Quem descobriu o Brasil? ")
    if pergunta1.lower() == 'pedro alvares cabral':
        print("Correto!")
        score += 1
    else:
        print("Incorreto!")
    pergunta2 = int(input("Quantos estados há no Brasil? "))
    if pergunta2 == 26:
        print("Correto!")
        score += 1
    else:
        print("Incorreto!")
               
    print("Parabéns, você acertou " + str(score) + " pergunta(s) e teve uma pontuação de " + str((score / 2) * 100) + "%")
else:
    ("Sem problemas, até mais!")

