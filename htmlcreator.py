from equation import Equation
from operation import Operation

def create_html(list_of_questions):
    """Create html table"""
    result = "<!DOCTYPE html>\n" 
    result += "<html>\n" 
    result += "<head>\n"
    result += "<title>Random List of Questions</title>\n"
    result += "<style>\n"
    result += "td#l, td#r {\n"
    result += "    vertical-align: middle;\n"
    result += "    text-align: center;\n"
    result += "    width: 25px;\n"
    result += "}\n"
    result += "td#o, td#q {\n"
    result += "    vertical-align: middle;\n"
    result += "    text-align: center;\n"
    result += "    width: 15px;\n"
    result += "}\n"
    result += "td#a {\n"
    result += "    border: 1px solid black;\n"
    result += "    width: 50px;\n"
    result += "}\n"
    result += "</style>\n"
    result += "</head>\n"
    result += "<body>\n"
    result += "<p>\n"
    result += "Name: _______________________________ Date: _______________ Time: _______________\n"
    result += "</p>\n"
    result += '<table style="font-size: x-large">\n'
    number_of_rows = len(list_of_questions) // 4
    if len(list_of_questions) % 4 > 0:
        number_of_rows += 1

    for row_number in range(0,number_of_rows):
        result += '<tr>'
        for col_number in range(0, 4):
            index = row_number * 4 + col_number
            equation = list_of_questions[index]
            result += '<td id="l">' + equation.LHS() + '</td><td id="o">' + equation.Operation().op + '</td><td id="r">' + equation.RHS() + '</td><td id="q">=</td><td id="a"/><td id="s">&nbsp;</td>'
        result += '</tr>\n'
    result += "</table>\n</body>\n</html>\n"
    return result

def getEquationAsString(eq):
    q = eq or Operation.empty()
    return q.to_s()


