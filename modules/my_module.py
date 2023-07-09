import re


def figure_out_names(text: str):
    if not text:
        return
    names = {}
    for line in text.splitlines():
        first_word = re.search(r'^(\w.+?): ', line)
        if first_word:
            grp = first_word.group(1)
            names.setdefault(grp, 0)
            names[grp] += 1

    character_name = text.rsplit('\n')[-1].strip(': ')
    sorted_names = [k for k, v in sorted(names.items(), key=lambda x: -x[1])][:2]
    author_name = sorted_names[0] if sorted_names[0] != character_name else sorted_names[1]
    return character_name, author_name



def print_reply(question: str,
                reply: str,
                print_question: bool = True,
                only_last_question: bool = True):
    character_name, author_name = figure_out_names(question)
    question_start = question[question.find(f'{character_name}: '):].splitlines()  # skip context
    if only_last_question:
        question = f'{author_name}: ' + question.rsplit(f'{author_name}: ')[-1]
    question_start_lines = min(len(question_start) - question.count('\n'), 10)
    if question_start_lines:
        question_start = '\n'.join(question_start[:question_start_lines])
    else:
        question_start = ''
    if print_question:
        output = (f'\n--- Question start ---\n{question_start}'
                  f'\n--- End ---\n{question}{reply}\n' 
                  f'\n')
    else:
        output = f'\n\n{reply}\n{"+" * 140}\n'
    print(output)
