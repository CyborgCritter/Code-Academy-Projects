
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

# Add your function below!
def average(lst):
    return (float(sum(lst))/len(lst))
    
def get_average(student):
    avgHW = average(student['homework']) * 0.1
    avgQ = average(student['quizzes']) * 0.3
    avgT = average(student['tests']) * 0.6
    return (avgHW + avgQ + avgT)

def get_letter_grade(scores):
    if scores >= 90:
        return ('A')
    elif scores >= 80 and scores < 90:
        return ('B')
    elif scores >= 70 and scores < 80:
        return ('C')
    elif scores >= 60 and scores < 70:
        return ('D')
    else:
        return ('F')

for student in students:
    weightedAvg = get_average(student)
    letterGrade = get_letter_grade(weightedAvg)
    print (letterGrade)

def get_class_average(students):
    classTot = 0.0
    for student in students:
        weightedAvg = get_average(student)
        classTot += weightedAvg
    return (classTot/len(students))

clsAvg = get_class_average(students)
print (clsAvg)
print (get_letter_grade(clsAvg))
