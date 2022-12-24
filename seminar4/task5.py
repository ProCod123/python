
def ratio(polynom):
    terms = polynom.split(' + ')
    term1 = terms[0].split('*x^')
    term2 = terms[1].split('*x')
    terms = term1 + list(term2[0])
    return list(map(int, terms))

with open("text1.txt", "r") as f1:
    text1 = f1.read()
with open("text2.txt", "r") as f2:
    text2 = f2.read()

p1 = ratio(text1)    
p2 = ratio(text2)

if p1[1] == p2[1]:
    result = f'{p1[0] + p2[0]}*x^{p1[1]} + {p1[2] + p2[2]}*x'
else:
    result = f'{p1[0]}*x^{p1[1]} + {p2[0]}*x^{p2[1]} + {p1[2] + p2[2]}*x'

print(result)

with open("text3.txt", "w") as f:
    f.write(result)


