# LaTeX template for Python listings enviroments

This template enables 

## How to use

Add the necessary packages from `template.tex` to your preamble. Those are specifically:

* `listings`
* `inconsolata`
* `xcolor`

Still in the preamble you must define colors for your listings environment. These are:

`\definecolor{codepurple}{rgb}{0.435,0.259,0.757}`

`\definecolor{codeblue}{rgb}{0,0.361,0.773}`

`\definecolor{codered}{rgb}{0.843,0.227,0.286}`

`\definecolor{codeorange}{rgb}{0.89,0.384,0.035}`

`\definecolor{codecomment}{rgb}{0.012,0.184,0.384}`

`\definecolor{codecommentsingle}{rgb}{0.416,0.451,0.490}`

Then you need to define a language such that we can achieve the intended syntax highlighting. 
You can define more than one language, but the template contains just this one, "fredcode":

```
\lstdefinelanguage{fredcode}{
    basicstyle=\ttfamily\footnotesize,
    morecomment = [s][\color{codecomment}]{"""}{"""},
    morecomment = [s][\color{codecomment}]{'}{'},
    morecomment = [s][\color{codecomment}]{"}{"},
    morecomment = [l][\color{codecommentsingle}]{\#},
    keywordstyle = [2]{\color{codepurple}},
    morekeywords = [2]{print,range,abs,len,append,open,list,map,split,readlines,sort,round,zip,yield},
    keywordstyle = [3]{\color{codepurple}},
    morekeywords = [3]{fit,predict,score,accuracy_score,__init__,inv,dot}, % this should contain the invocation of functions or methods
    keywordstyle = [4]{\color{codered}},
    morekeywords = [4]{from,import,def,class,for,while,return,if,elif,else,continue,and,or,as},
    keywordstyle = [5]{\color{codeblue}},
    morekeywords = [5]{in,not, False, True, None},
    keywordstyle = [6]{\color{codeorange}},
    morekeywords = [6]{ValueError,HML,Linear,T,X,LinearRegression},  % this should contain any oject name beginning with uppercase letter
    alsoletter = {**,==,>=,<=,=,+,-,/,\%,*,*=,+=,-=,/,//,=,!=,1,2,3,4,5,6,7,8,9},
    keywordstyle = [7]{\color{codeblue}},
    morekeywords = [7]{**,==,=,+,-,/,\%,*,*=,+=,-=,/=,!=,1,2,3,4,5,6,7,8,9},
    lineskip = 4pt
}
```
Remember that this definition is specific to the code snippets in template.tex. In particular you want to adjust the lists for morekeywords 3 and 6. These can be added somewhat automatically as described below.

## Automated language config

You can have the `listings_config.py` write the preamble for you. Just open the script and set the filename variable to point to the appropriate python file and run it. It will print the language definition to the console and you can then just copy/paste it to your LaTeX preamble.

**Attention** - running `listings_config.py` on your on own python script will only identify invocations of methods and functions if these are defined in the same script. This means that if you import a library such as numpy and you invoke methods from it then those methods should be added manually to the morekeywords 3 list in the language definition.
