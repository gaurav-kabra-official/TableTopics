import random
with open("GD_Topics.txt") as f:
    topics=f.readlines()
    no_of_topics=len(topics)
    print('Enter the names of the participants a single line seperated by spaces.')
    try:
        persons=list(map(list,input().split()))
        random.shuffle(persons)
        for person in persons:
            name=''.join(person)    #list to string (name) again
            print(name,"your topic:")
            print(random.choice(topics))
            print("======================")
    except:
        print('Error in input')
        print('Sorry to leave')
        quit()
input()         #hold console window
input()

