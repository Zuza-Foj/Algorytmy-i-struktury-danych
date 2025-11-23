import re

TAG_PAIRS = {
    '</p>': '<p>',
    '</div>': '<div>',
    '</a>': '<a>',
    '</h1>': '<h1>',
    '</h2>': '<h2>',
    '</h3>': '<h3>',
    '</li>': '<li>',
    '</ul>': '<ul>',
    '<ol>': '</ol>',
    '</tbody>': '<tbody>',
    '</tr>': '<tr>',
    '</td>': '<td>',
    '</thead>': '<thead>',
    '</table>': '<table>',
    '</body>': '<body>',
    '</html>': '<html>'}

VOID_TAGS = ['<br>', '<hr>', '<img>', '<input>', '<meta>', '<link>']

def get_tags(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            #return html_content
    except FileNotFoundError:
        return f"Błąd: Plik nie został znaleziony pod ścieżką: {file_path}"

    tags =  re.findall(r'<[/]?[a-zA-Z]+[^>]*>', html_content)
    clean_tags = []
    for tag in tags:
        if tag.startswith('</'):
            tag_name = tag.strip('<>').split()[0]
            clean_name = tag_name.replace('/', '')
            clean_tags.append('</' + clean_name + '>')
        elif tag.endswith('/>'):
            tag_name = tag.strip('<>').replace('/', '').split()[0]
            clean_tags.append('<' + tag_name + '>')
        else:
            tag_name = tag.strip('<>').split()[0]
            clean_tags.append('<' + tag_name + '>')
    return clean_tags

def check_html(file_path):
    tags = get_tags(file_path)
    stack = []
    for tag in tags:
        if tag in VOID_TAGS:
            continue

        if tag.startswith('</'):
            if len(stack) == 0:
                return f'BŁĄD: Tag zamykający **{tag}** bez odpowiadającego mu tagu otwierającego.'

            expected_opening_tag = '<' + tag[2:-1] + '>'
            top_of_stack = stack[-1]
            if top_of_stack == expected_opening_tag:
                stack.pop()
            else:
                return f'BŁĄD: Znaleziony znacznik zamykający **{tag}** nie pasuje do ostatniego znacznika otwierającego.'

        else:
            stack.append(tag)

    if len(stack) == 0:
        return f'SUKCES: Wszystkie znaczniki są prawidłowo zamknięte!'
    else:
        return f'BŁĄD: Składnia jest niepoprawna, na stosie pozostały niezamknięte znaczniki.'

if __name__ == '__main__':
    file_path_to_test = 'authors.html'
    test = check_html(file_path_to_test)
    print(test)
