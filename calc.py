def calculate(a: str, b: str, sign: str) -> str:
    try:
        a: float = float(a)
        b: float = float(b)
        res: float = 0.0
        match sign:
            case "+":
                res = a + b
            case "-":
                res = a - b
            case "*":
                res = a * b
            case "/":
                res = a / b
            case "^":
                res = a ** b
        return str(res)
    except ZeroDivisionError:
        return "find division zero"
    except ValueError:
        return "wrong input (maby + - * / )"


def preparation(example_input: str) -> list[str]:
    if len(example_input) == 0:
        return ["empty input"]
    list_example: list = []
    tmp: str = ""
    sign = ""
    for i in example_input:
        if i.isdigit():
            tmp += i
        else:
            list_example.append(tmp)
            tmp = ""
        if i in "()+-/*^":
            list_example.append(sign + i)
    list_example.append(tmp)
    while "" in list_example:
        list_example.remove("")
    return list_example


def get_res(input_list: list[str]) -> list[str]:
    if input_list[0] in "-+":
        input_list[1] = str(-int(input_list[1]))
        input_list.pop(0)
    while "^" in input_list:
        index = input_list.index("^")
        input_list[index - 1] = (calculate(input_list[index - 1], input_list[index + 1], input_list[index]))
        input_list.pop(index)
        input_list.pop(index)
    while "*" in input_list or "/" in input_list:
        for i in range(0, len(input_list) - 2, 2):
            if len(input_list) - 2 <= i:
                break
            if input_list[i + 2] == "-":
                input_list[i + 2] = "-" + input_list[i + 3]
                input_list.pop(i + 3)
            if input_list[i + 1] in "*/":
                input_list[i] = str(calculate(input_list[i], input_list[i + 2], input_list[i + 1]))
                input_list.pop(i + 1)
                input_list.pop(i + 1)
    while "+" in input_list or "-" in input_list:
        input_list[0] = (calculate(input_list[0], input_list[2], input_list[1]))
        input_list.pop(1)
        input_list.pop(1)

    return input_list


def remove_other(input_for_remove: list[str] | str) -> list[str]:
    while "(" in input_for_remove:
        if isinstance(input_for_remove, str):
            return [input_for_remove]
        try:
            first: int = len(input_for_remove) - 1 - input_for_remove[::-1].index("(")
            second: int = input_for_remove[first:].index(")") + first
        except ValueError:
            return ["'(' or ')' not found"]
        start: list = input_for_remove[: first]
        end: list = input_for_remove[second + 1:]
        tmp: list = input_for_remove[first + 1: second]
        if tmp[0] == "-":
            tmp[1] = str(-int(tmp[1]))
            tmp.pop(0)

        xxx = get_res(tmp)
        input_for_remove.clear()
        input_for_remove.extend(start)
        input_for_remove.extend(xxx)
        input_for_remove.extend(end)

    return get_res(input_for_remove)


#
n = ["( 100 - 5 ) / ( 65 + 3 )"]
for x in n:
    example = x.replace(" ", "")
    prepare = preparation(example)
    print(example, "=", eval(x.replace("^", "**")), "eval")
    print(example, "=", remove_other(prepare)[0], "my")