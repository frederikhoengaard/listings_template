import re

filename = 'example.py' # path to your file here!


script_specific_identifiers = set()
capital_identifiers = set()
infile = open(filename,'r')
for line in infile.readlines():
    # functions
    functions = re.findall("def \w\w+\(",line)
    if functions:
        for item in functions:
            script_specific_identifiers.add(item.split()[-1][:-1])
    # capitals
    capitals = re.findall("[A-Z]_*\w*",line)
    if capitals:
        for item in capitals:
            if not item in ['False','True','None']:
                capital_identifiers.add(item)

out = []

out.append(r"\definecolor{codepurple}{rgb}{0.435,0.259,0.757}")
out.append(r"\definecolor{codeblue}{rgb}{0,0.361,0.773}")
out.append(r"\definecolor{codered}{rgb}{0.843,0.227,0.286}")
out.append(r"\definecolor{codeorange}{rgb}{0.89,0.384,0.035}")
out.append(r"\definecolor{codecomment}{rgb}{0.012,0.184,0.384}")
out.append(r"\definecolor{codecommentsingle}{rgb}{0.416,0.451,0.490}")
out.append("\n")
out.append(r"\lstdefinelanguage{fredcode}{")
out.append(r"    basicstyle=\ttfamily\footnotesize,")
out.append(r'    morecomment = [s][\color{codecomment}]{"""}{"""},')
out.append(r"    morecomment = [s][\color{codecomment}]{'}{'},")
out.append(r'    morecomment = [s][\color{codecomment}]{"}{"},')
out.append(r"    morecomment = [l][\color{codecommentsingle}]{\#},")
out.append(r"    keywordstyle = [2]{\color{codepurple}},")
out.append(r"    morekeywords = [2]{print,range,abs,len,append,open,list,map,split,readlines,sort,round,as},")
out.append(r"    keywordstyle = [3]{\color{codepurple}},")
out.append(r"    morekeywords = [3]{" + ','.join(list(script_specific_identifiers)) + r'},')
out.append(r"    keywordstyle = [4]{\color{codered}},")
out.append(r"    morekeywords = [4]{from,import,def,class,for,while,return,if,elif,else,continue,and,or},")
out.append(r"    keywordstyle = [5]{\color{codeblue}},")
out.append(r"    morekeywords = [5]{in,not},")
out.append(r"    keywordstyle = [6]{\color{codeorange}},")
out.append(r"    morekeywords = [6]{" + ','.join(list(capital_identifiers)) + r'},')
out.append(r"    alsoletter = {**,==,>=,<=,=,->,+,-,/,\%,*,*=,+=,-=,/,//,=,!=,0,1,2,3,4,5,6,7,8,9},")
out.append(r"    keywordstyle = [7]{\color{codeblue}},")
out.append(r"    morekeywords = [7]{**,==,=,->,+,-,/,\%,*,*=,+=,-=,/=,!=,0,1,2,3,4,5,6,7,8,9},")
out.append(r"    lineskip = 4pt")
out.append(r'}')

print('\n'.join(out))
