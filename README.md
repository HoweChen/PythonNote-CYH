# About

This repo is a note about Python of myself.

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