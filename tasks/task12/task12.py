dict={"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
x=input()
if 'born' and 'when' in x:
    print('“Maybe did you mean “When was Plato born?”')
    z=input('yes or not:')
    if z=='yes':
        print(dict['born'])
    else:
        print("none")
    
elif 'born' and 'where'in x:
    print('“Maybe did you mean “Where was Plato born?”')
    y=input('yes or not:')
    if y=='yes':
        print(dict['country'])
    else:
        print('none')    
    