from equation import Equation
from operation import Operation

def create_html(list_of_questions):
    """Create html table"""
    result = "<!DOCTYPE html>\n" 
    result += "<html>\n" 
    result += "<head>\n"
    result += "<title>Random List of Questions</title>\n"
    result += "<style>"
    result += "td#q {"
    result += "    vertical-align: middle;"
    result += "}"
    result += "td#a {"
    result += "    border: 1px solid black;"
    result += "    width: 50px;"
    result += "}"
    result += ""
    result += "</style>"
    result += "</head>\n"
    result += "<body>\n"
    result += '<table style="font-size: x-large">\n'
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
            cell_1 = getEquationAsString(list_of_questions[index])
        if len(list_of_questions) > index + 1:
            cell_2 = getEquationAsString(list_of_questions[index + 1])
        if len(list_of_questions) > index + 2:
            cell_3 = getEquationAsString(list_of_questions[index + 2]) 
        if len(list_of_questions) > index + 3:
            cell_4 = getEquationAsString(list_of_questions[index + 3]) 
        result += '<tr>'
        result += '<td id="q">' + cell_1 + '</td><td id="a"/><td>&nbsp;</td>'
        result += '<td id="q">' + cell_2 + '</td><td id="a"/><td>&nbsp;</td>'
        result += '<td id="q">' + cell_3 + '</td><td id="a"/><td>&nbsp;</td>'
        result += '<td id="q">' + cell_4 + '</td><td id="a"/><td>&nbsp;</td>'
        result += '</tr>\n'
    result += "</table>\n</body>\n</html>\n"
    return result

def getEquationAsString(eq):
    q = eq or Operation.empty()
    return q.to_s()

