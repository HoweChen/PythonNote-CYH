class AnonymousSurvey():

    def __init__(self, question):
        self.question = question
        self.response = []

    def show_question(self):
        print(self.question)

    def store_response(self, response):
        self.response.append(response)

    def show_response(self):
        for item in self.response:
            print(item)
