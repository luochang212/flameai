from flameai.sql import SQLConnect

sc = SQLConnect()
sc.create_table_with_csv('student', '../data/student.csv', sep='\t')
sc.create_table_with_csv('course', '../data/course.csv', sep='\t')

query = """
SELECT
    a.name,
    a.age,
    b.course
FROM student a
LEFT JOIN course b
ON a.name = b.name
"""
res = sc.sql(query)
print(res)
