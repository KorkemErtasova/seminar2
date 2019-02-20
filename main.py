from mybox import MyBox
from myboxiterator import MyBoxIterator
from myclass import Cat
b = MyBox()
b.add(Cat('red', '3', 'Era'))
b.add(Cat('yellow', '2', 'Mera'))
b.add(Cat('white', '1', 'kora'))

b.remove(1)
for i in b:
	i.define()
