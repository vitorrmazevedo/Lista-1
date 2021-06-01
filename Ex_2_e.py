sentence = "Practice Problems to Drill List Comprehension in Your Head."
sentence = sentence.split()
for i in sentence: 
    if len(i) < 5:
        print(i)

