# from faker import Faker
# fake = Faker()
# from user.models import PageViews, ClickActivities
# Faker.seed(0)
# 87 79
a ='''7
10
12
7
10
10
8
7
5
7
13
3'''
a = a.split('\n')
s = 0
for i in range(0, len(a)):
    s += int(a[i])
print(s)