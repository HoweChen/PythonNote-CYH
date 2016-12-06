import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        question = 'What language did you first learn to speak?\n'
        self.survey = AnonymousSurvey(question)
        self.answers = ['English', 'Chinese', 'Spanish']

    def test_store_single_response(self):
        self.survey.store_response(self.answers[0])
        self.assertIn('English', self.survey.response)

    def test_store_multiple_response(self):

        for answer in self.answers:
            self.survey.store_response(answer)
            # self.assertIn(item, survey.response)

        for answer in self.answers:
            self.assertIn(answer, self.survey.response)

unittest.main()
