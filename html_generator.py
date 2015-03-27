def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

LESSON_8 = [ ['Lists', 'Lists are sequences of data which contain an assignment statement and corresponding list of elements. Lists can contain numbers, strings or a combination of both.'],
             ['Nested Lists', 'Lists can can contain other lists. Like characters in strings, list elements are indexed starting from 0.'],
             ['Mutation and Aliasing', 'Unlike strings, which are immutable, lists can be mutated.'],
             ['List Operations', 'The append operation adds a new element to the list. This operation is limited to one list element. The += operation appends any number of elements to the list. The + operation does not mutuate the list but will concatenate the two. The len operation, written as len(<list>), will give the number of elements in the list.'],
             ['Index Methods', '<list>.index(<value>) will return the first occurence of the value in the list. If the value does not occur, the python interpreter will return error. <value>in<list> and <value>not in<list> are boolean values and will tell us whether or not the value is in the list.'],
             ['For Loop', 'When we write "for<name>in<list>", <name> means each element in <list>.'] ]

print make_HTML_for_many_concepts(LESSON_8)

