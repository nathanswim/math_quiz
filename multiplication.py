from random import sample

"""print list of 12 times table"""

LHS_START = 1
LHS_END = 12
RHS_START = 1
RHS_END = 12
NUMBER_OF_QUESTIONS = 100

LHS_LIST = list(range(LHS_START, LHS_END+1))
RHS_LIST = list(range(RHS_START, RHS_END+1))

def ordered_question_list(lhs, rhs):
	"""take the lhs and rhs and produce a randomized list of questions"""
	result = []
	for l_n in lhs:
		for r_n in rhs:
			result.append(str(l_n) + ' x ' + str(r_n) + ' =')
	return result


def print_list(questions):
	"""Create html table"""
	for q_item in questions:
		print(q_item)
	return


question_list = ordered_question_list(LHS_LIST, RHS_LIST)

random_index = list(range(0,len(question_list)))
random_index = sample(random_index, len(random_index))

result = []

for i in range(0,NUMBER_OF_QUESTIONS):
	index = random_index[i]
	question = question_list[index]
	result.append(question)


def create_html(list_of_questions):
	result = "<!DOCTYPE html>\n" 
	result += "<html>\n" 
	result += "<head><title>Random List of Questions</title></head>\n"
	result += "<body>\n"
	result += "<table cellpadding=\"8\">\n" 
	number_of_rows = len(list_of_questions) // 4
	if len(list_of_questions) % 4 > 0:
		number_of_rows += 1

	for row_number in range(0,number_of_rows):
		index = row_number * 4
		cell_1 = ""
		cell_2 = ""
		cell_3 = ""
		cell_4 = ""
		if len(list_of_questions) > index:
			cell_1 = list_of_questions[index] 
		if len(list_of_questions) > index + 1:
			cell_2 = list_of_questions[index + 1] 
		if len(list_of_questions) > index + 2:
			cell_3 = list_of_questions[index + 2] 
		if len(list_of_questions) > index + 3:
			cell_4 = list_of_questions[index + 3] 
		result += "<tr>"
		result += "<td>" + cell_1 + "</td><td>______</td>"
		result += "<td>" + cell_2 + "</td><td>______</td>"
		result += "<td>" + cell_3 + "</td><td>______</td>"
		result += "<td>" + cell_4 + "</td><td>______</td>"
		result += "</tr>\n"
	result += "</table>\n</body>\n</html>\n"
	return result



print(create_html(result))



