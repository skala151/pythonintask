+import random
 + 
 +WORDS = ("человек","религия","замок","монстр","бабочка","сосна","ежик","ролики","танец","улитка","романтика")
 + 
 +word = random.choice(WORDS)
 + 
 +correct = word
 + 
 +i_dont_know = "Я не знаю"
 +hint = word[0] + word[1] + word[2]
 + 
 +jumble = ""
 +while word:
 +    position = random.randrange(len(word))
 +    jumble += word[position]
 +    word = word[:position] + word[(position + 1):]
 + 
 +scores = 10
 + 
 +print(
 +    """
 +                                    
 +                                   Добро пожаловать в игру «Анаграммы»!
 +                         Нужно переставить буквы, чтобы получить осмысленное слово.
 +                                Если вам нужна помощь, введите: «Я не знаю».
 +            Но помните, что если вы не используете подсказку, количество набранных баллов будет больше.
 +                             (Чтобы выйти, нажмите Enter, не вводя его версию.)
 +    """
 +)
 +print("Это анаграма: ", jumble)
 +guess = input("\nПопробуйте угадать исходное слово: ")
 +while guess != "" and guess != correct:
 +    if guess != correct and not guess == i_dont_know:
 +        print("К сожалению, вы ошибаетесь.")
 +    if guess == i_dont_know:
 +        scores -= 5
 +        print("\nПодсказка! Первые три буквы этого слова^", hint)
 +    guess = input("Попробуйте угадать исходное слово: ")
 +    if guess == correct:
 +        print("Да, точно! Вы угадали!\n")
 + 
 +if scores < 0:
 +    scores = 0
 +print("Спасибо за игру! Ваш счет: ", scores)
 +input("\n\nНажмите Enter, чтобы выйти.")
