# About

This repo is a note about Python which I collect them or summerize them.

# 不要用 for 循环去修改其中的元素

```python
a = [1, 2, 3, 4, 5, 6]

for itr in range(len(a)):

    if a[itr] == 1:

        a.append(7)

    print(a[itr])

print(a)

1

2

3

4

5

6

[1, 2, 3, 4, 5, 6, 7]

a = [1, 2, 4, 4, 5, 6]

for itr, val in enumerate(a):

    if a[itr] == 4:

        del a[itr]

    print(a[itr])

print(a)

1

2

4

5

6

[1, 2, 4, 5, 6]

```



正确的处理方法是用 while 循环，其写法是符合满足条件的进行处理，否则+1，这样的话 itr 在遇到情况处理后还停留在原地

#  Set 保留 list 的顺序

#  sort() 和 sorted() 的区别

1. `sorted()` returns a **new** sorted list, leaving the original list unaffected. `list.sort()` sorts the list **in-place**, mutating the list indices, and returns `None` (like all in-place operations).
2. `sorted()` works on any iterable, not just lists. Strings, tuples, dictionaries (you'll get the keys), generators, etc., returning a list containing all elements, sorted.
3. - Use `list.sort()` when you want to mutate the list, `sorted()` when you want a new sorted object back. Use `sorted()` when you want to sort something that is an iterable, not a list *yet*.
   - For lists, `list.sort()` is faster than `sorted()` because it doesn't have to create a copy. For any other iterable, you have no choice.
   - No, you cannot retrieve the original positions. Once you called `list.sort()` the original order is gone.

#  默认参数注意事项

```python
An example:

>>> def function(data=[]):



...     data.append(1)



...     return data



...



>>> function()



[1]



>>> function()



[1, 1]



>>> function()



[1, 1, 1]

```



As you can see, the list keeps getting longer and longer. If you look at the list identity, you’ll see that the function keeps returning the same object:

```python
>>> id(function())



12516768



>>> id(function())



12516768



>>> id(function())



12516768

```



The reason is simple: the function keeps using the same object, in each call. The modifications we make are “sticky”.

Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

所以，定义默认参数要牢记一点：默认参数必须指向不变对象

​    

#  生成器的用法，以及() 和 [] 在生成器当中的区别 (内容来自廖雪峰博客)

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的`[]`改成`()`，就创建了一个generator：

```
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x104feab40>
```

创建`L`和`g`的区别仅在于最外层的`[]`和`()`，`L`是一个list，而`g`是一个generator。

我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过generator的`next()`方法：

```
>>> g.next()
0
>>> g.next()
1
>>> g.next()
4
>>> g.next()
9
>>> g.next()
16
>>> g.next()
25
>>> g.next()
36
>>> g.next()
49
>>> g.next()
64
>>> g.next()
81
>>> g.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

我们讲过，generator保存的是算法，每次调用`next()`，就计算出下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

当然，上面这种不断调用`next()`方法实在是太变态了，正确的方法是使用`for`循环，因为generator也是可迭代对象：

```
>>> g = (x * x for x in range(10))
>>> for n in g:
...     print n
...
0
1
4
9
16
25
36
49
64
81
```

所以，我们创建了一个generator后，基本上永远不会调用`next()`方法，而是通过`for`循环来迭代它。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的`for`循环无法实现的时候，还可以用函数来实现。


# 对 tuple list 进行的排序

我的同事Axel Hecht 给我展示了一些我所不知道的关于python排序的东西。 在python里你可以对一个元组进行排序。例子是最好的说明：

    >>> items = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
    >>> sorted(items)
    [(0, 'B'), (0, 'a'), (1, 'A'), (1, 'B'), (2, 'A')]

默认情况下内置的sort和sorted函数接收的参数是元组时，他将会先按元组的第一个元素进行排序再按第二个元素进行排序。 然而，注意到结果中(0, 'B’)在(0, 'a')的前面。这是因为大写字母B的ASCII编码比a小。然而，假设你想要一些更人性的排序并且不关注大小写。你或许会这么做：

    >>> sorted(items, key=str.lower)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: descriptor 'lower' requires a 'str' object but received a 'tuple'

我们将会得到一个错误，因为他不能正确处理元组的第一部分。（注：原文作者估计想说元组中第一项是数字，不能使用lower这个方法；正确的原因提示的很明显了，是因为你传递的是一个元组，而元组是没有lower这个方法的）

我们可以试着写一个lambda函数(eg.sorted(items, key=lambda x: x.lower() if isinstance(x, str) else x)),他将不会工作因为你只处理了元组的一个元素。（注：同上面，作者这么做必然是错的，思考给这个lambda传一个元组,返回的是什么？）

言归正传，下面就是你应该怎么做的方法。一个lambda，它会返回一个元组:

    >>> sorted(items, key=lambda x: (x[0], x[1].lower()))
    [(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]

如果是 sorted(items, key=lambda x: (x[1].lower())) 那么结果就是针对每一个 iterator 也就是每一个 tuple 里的第二个元素进行排序，那么原文里头的呢，是先对第一个元素进行排序，然后再对第二个元素进行排序。



现在你完成了它！谢谢Axel的分享！

作为你还在读本博文的奖励...

我确信你知道你可以倒序排列，仅仅使用sorted(items, reverse=True, …)，但是你怎么根据关键字来进行不同的排序？

使用lambda函数返回元组的技巧，下面是一个我们排序一个稍微高级的数据结构:

    >>> peeps = [{'name': 'Bill', 'salary': 1000}, {'name': 'Bill', 'salary': 500}, {'name': 'Ted', 'salary': 500}]

现在，使用lambda函数返回一个元组的特性来排序:

    >>> sorted(peeps, key=lambda x: (x['name'], x['salary']))
    [{'salary': 500, 'name': 'Bill'}, {'salary': 1000, 'name': 'Bill'}, {'salary': 500, 'name': 'Ted'}]

很有意思，对吧？Bill 在Ted的前面，并且500在1000的前面。但是如何在相同的 name 下，对 salary 反向排序？很简单，对它取反:

    >>> sorted(peeps, key=lambda x: (x['name'], -x['salary']))
    [{'salary': 1000, 'name': 'Bill'}, {'salary': 500, 'name': 'Bill'}, {'salary': 500, 'name': 'Ted'}]

原文地址：http://www.peterbe.com/plog/in-python-you-sort-with-a-tuple


# 元组拆包，或者称之为可迭代对象拆包 (来自[流畅的 Python](http://www.ituring.com.cn/book/1564))

[拓展阅读](https://www.python.org/dev/peps/pep-3132/)



```python
>>> lax_coordinates = (33.9425, -118.408056)

>>> latitude, longitude = lax_coordinates # 元组拆包

>>> latitude

33.9425

>>> longitude -118.408056
```

另外一个很优雅的写法当属不使用中间变量交换两个变量的值：

```python
>>> b, a = a, b
```

还可以用 * 运算符把一个可迭代对象拆开作为函数的参数：

```python
>>> divmod(20, 8) (2, 4)

>>> t = (20, 8)

>>> divmod(*t) (2, 4)

>>> quotient, remainder = divmod(*t)

>>> quotient, remainder (2, 4)
```

下面是另一个例子，这里元组拆包的用法则是让一个函数可以用元组的形式返回多个值， 然后调用函数的代码就能轻松地接受这些返回值。比如 os.path.split() 函数就会返回以 路径和最后一个文件名组成的元组 (path, last_part) :

```python
>>> import os

>>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')

>>> filename 'idrsa.pub'
```

在进行拆包的时候，我们不总是对元组里所有的数据都感兴趣， _ 占位符能帮助处理这种 情况，上面这段代码也展示了它的用法。



在Python 中，函数用 *args 来获取不确定数量的参数算是一种经典写法了。 于是 Python 3 里，这个概念被扩展到了平行赋值中：

```python
>>> a, b, *rest = range(5)

>>> a, b, rest (0, 1, [2, 3, 4])

>>> a, b, *rest = range(3)

>>> a, b, rest (0, 1, [2])

>>> a, b, *rest = range(2)

>>> a, b, rest (0, 1, [])
```

# .append() 和 .extend() 的区别

append 加入元素，extend 加入可迭代对象。