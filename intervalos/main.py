# Intervalos (https://dojopuzzles.com/problems/intervalos/)
#
# Este problema foi utilizado em 313 Dojo(s).
#
# Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
#
# Exemplo:
#
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
#
# Saída: [100-105], [110-111], [113-115], [150]


def intervals(numbers_list:list[int], next_element=0) -> str:
    """Recursive function that return a list of intervals 
    from a list of sorted numbers."""
    
    if not numbers_list:
        return "[]"
    else:
        if next_element == 0:
            numbers_list[0] = f"[{numbers_list[0]}]"
            return intervals(numbers_list, next_element=1)
        else:
            try:
                current_element = numbers_list.pop(next_element)
                element_ago_list = numbers_list[next_element-1][1:-1].split("-")
                
                first_element = int(element_ago_list[0])
                last_element = int(element_ago_list[-1])
                
                if current_element == last_element + 1:
                    new_element_ago = f"[{first_element}-{current_element}]"
                    numbers_list[next_element-1] = new_element_ago
                    return intervals(numbers_list, next_element=next_element)
                else:
                    numbers_list.insert(next_element, f"[{current_element}]")
                    return intervals(numbers_list, next_element=next_element+1)

            except IndexError:
                output = ", ".join(numbers_list)
                return output.__str__().replace("'", "")
