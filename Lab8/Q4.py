import numpy as np

students = np.array([
    ("Ali", 5.5, 10),
    ("Abser", 5.3, 12),
    ("Owais", 5.2, 11),
    ("Fasih", 5.1, 10)
], dtype=np.dtype([
    ('name', 'U10'),
    ('height', 'f4'),
    ('class', 'i8'),
]))

print(np.sort(students, order=['class', 'height']))