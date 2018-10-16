from equation import Equation
from operation import Operation

def create_html(list_of_questions):
	"""Create html table"""
	result = "<!DOCTYPE html>\n" 
	result += "<html>\n" 
	result += "<head><title>Random List of Questions</title></head>\n"
	result += "<body>\n"
	result += "<table cellpadding=\"6\">\n" 
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
		result += "<td>" + cell_1.to_s() + "</td><td>______</td><td>&nbsp;</td>"
		result += "<td>" + cell_2.to_s() + "</td><td>______</td><td>&nbsp;</td>"
		result += "<td>" + cell_3.to_s() + "</td><td>______</td><td>&nbsp;</td>"
		result += "<td>" + cell_4.to_s() + "</td><td>______</td><td>&nbsp;</td>"
		result += "</tr>\n"
	result += "</table>\n</body>\n</html>\n"
	return result
