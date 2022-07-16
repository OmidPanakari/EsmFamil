class EsmFamil:
    def __init__(self, categories, playerCnt, turnCnt):
        self.categories = categories
        self.playerCnt = playerCnt
        self.turnCnt = turnCnt
        self.scores = [0]*self.playerCnt

    def getAnswers(self, roundChr):
        count = [{} for i in range(len(self.categories))]
        answers = [None] * self.playerCnt
        for i in range(self.playerCnt):
            answers[i] = input("Bazikone shomare " + str(i+1) + " javabhaye khod ra vare kon:(- bejaye hichi) ").split()
            for j in range(len(self.categories)):
                if answers[i][j] != "-" and answers[i][j][0] == roundChr:
                    if not answers[i][j] in count[j]:
                        count[j][answers[i][j]] = 0
                    count[j][answers[i][j]] += 1
        return (answers, count)

    def checkAnswers(self, answers, count, roundChr):
        for i in range(self.playerCnt):
            for j in range(len(self.categories)):
                if answers[i][j] != "-" and answers[i][j][0] == roundChr:
                    if count[j][answers[i][j]] > 1:
                        self.scores[i] += 5
                    else:
                        self.scores[i] += 10
            print("Emtiaze bazikone shomare " + str(i+1) + ": " + str(self.scores[i]))


    def playTurn(self, roundChr):
        for cat in self.categories:
            print(cat, end=" ")
        print()
        answers, count = self.getAnswers(roundChr)
        self.checkAnswers(answers, count, roundChr)
        

    def run(self):
        currPlayer = 0
        while self.turnCnt > 0:
            roundChr = input("Bazikone shomare " + str(currPlayer + 1) + " harfe in round ra entekhab konad: ")[0]
            self.playTurn(roundChr)
            self.turnCnt-=1
        mx = max(self.scores)
        for i in range(self.playerCnt):
            if self.scores[i] == mx:
                print("Bazikone shomare " + str(i+1) + " barande ast:)")
    



print("Be bazie EsmFamil khosh amadid :)")
categories = input("Categoryhaye bazi ra vared konid: ").split()
playerCnt = int(input("Tedade bazikonan ra vared konid: "))
turnCnt = int(input("Bazi chand dor bashad: "))
esmFamil = EsmFamil(categories, playerCnt, turnCnt)
esmFamil.run()