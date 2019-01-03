from PyInquirer import prompt
import uuid, random

uid = lambda: 'a'+''.join(str(uuid.uuid4()).split("-"))

class Quizzly(object):
	def __init__(self, name):
		u = uid()
		exec("import quizzes.%s as %s" % (name, u))
		self.questions = locals()[u].questions
	def do_question(self, question):
		ans = prompt([{
				'type':'input',
				'name':'ans',
				'message':question['question'],
			}])
		return ans['ans'] in question['answers']
	def run(self):
		score = 0
		qs = self.questions

		while not qs == []:
			q = random.choice(qs)
			res = self.do_question(q)
			if res:
				score += 1
			else:
				score += 0
			print("You were:","correct" if res else "wrong")
			print("The list of correct answers were:",', '.join(q['answers'])) if not res else None
			qs.remove(q)

		return score

if __name__ == "__main__":
	qname = input("Quiz name: ")
	quiz = Quizzly(qname)
	score = quiz.run()
	print("\n\nYour final score is:",score)