SITEMAP = './sitemap.md'


def parse(lines, level=0) -> list:
    tree: list = []
    while lines:
        line: str = lines[0]
        line = line.rstrip(' \n')
        current_level: float = (len(line) - len(line.lstrip())) / 4
        if current_level.is_integer():
            current_level: int = int(current_level)
        else:
            raise ValueError(f'Error in sitemap line "{line}": Indentations must be multiples of 4 spaces')
        if current_level == level:
            lines.pop(0)
            node = [line.strip()]
            children = parse(lines, level + 1)
            if children:
                node.extend(children)
                tree.append(node)
            else:
                tree.append(node)
        else:
            break
    return tree


def do_parse(lines) -> list:
    tree = parse(lines)
    return tree[0]


with open(SITEMAP, 'r') as file:
    my_lines: list = file.readlines()
my_tree: list = do_parse(my_lines)
print(my_tree)
