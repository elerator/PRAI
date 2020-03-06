import os
for x in range(1000):
    print("Hello world")

os.system("python ./manage.py runserver 0.0.0.0:5000")

#CMD ["python", "./manage.py", "runserver", "0.0.0.0:5000"]
