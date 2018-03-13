my_function = lambda a,b,c : a + b

print(my_function(1,2,3))


people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda person: "{} {}".format(person.split()[0],person.split()[-1]))(person))

#option 2
#list(map(split_title_and_name, people)) == list(map(???))


for person in people:
    print(split_title_and_name(person) == (lambda person: person.split()[0] + " " + person.split()[-1])(person))

# list(map(split_title_and_name(person), people)) == list(map(lambda person: person.split()[0] + " " + person.split()[-1], people))
