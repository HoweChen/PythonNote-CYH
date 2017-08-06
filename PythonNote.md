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

```python
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

```python
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

```python
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

```python
>>> items = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
>>> sorted(items)
[(0, 'B'), (0, 'a'), (1, 'A'), (1, 'B'), (2, 'A')]
```

默认情况下内置的sort和sorted函数接收的参数是元组时，他将会先按元组的第一个元素进行排序再按第二个元素进行排序。 然而，注意到结果中(0, 'B’)在(0, 'a')的前面。这是因为大写字母B的ASCII编码比a小。然而，假设你想要一些更人性的排序并且不关注大小写。你或许会这么做：
```python
>>> sorted(items, key=str.lower)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: descriptor 'lower' requires a 'str' object but received a 'tuple'
```

我们将会得到一个错误，因为他不能正确处理元组的第一部分。（注：原文作者估计想说元组中第一项是数字，不能使用lower这个方法；正确的原因提示的很明显了，是因为你传递的是一个元组，而元组是没有lower这个方法的）

我们可以试着写一个lambda函数(eg.sorted(items, key=lambda x: x.lower() if isinstance(x, str) else x)),他将不会工作因为你只处理了元组的一个元素。（注：同上面，作者这么做必然是错的，思考给这个lambda传一个元组,返回的是什么？）

言归正传，下面就是你应该怎么做的方法。一个lambda，它会返回一个元组:

```python
>>> sorted(items, key=lambda x: (x[0], x[1].lower()))
[(0, 'a'), (0, 'B'), (1, 'A'), (1, 'B'), (2, 'A')]
```

如果是 sorted(items, key=lambda x: (x[1].lower())) 那么结果就是针对每一个 iterator 也就是每一个 tuple 里的第二个元素进行排序，那么原文里头的呢，是先对第一个元素进行排序，然后再对第二个元素进行排序。



现在你完成了它！谢谢Axel的分享！

作为你还在读本博文的奖励...

我确信你知道你可以倒序排列，仅仅使用sorted(items, reverse=True, …)，但是你怎么根据关键字来进行不同的排序？

使用lambda函数返回元组的技巧，下面是一个我们排序一个稍微高级的数据结构:

```python
>>> peeps = [{'name': 'Bill', 'salary': 1000}, {'name': 'Bill', 'salary': 500}, {'name': 'Ted', 'salary': 500}]
```

现在，使用lambda函数返回一个元组的特性来排序:

```python
>>> sorted(peeps, key=lambda x: (x['name'], x['salary']))
[{'salary': 500, 'name': 'Bill'}, {'salary': 1000, 'name': 'Bill'}, {'salary': 500, 'name': 'Ted'}]
```

很有意思，对吧？Bill 在Ted的前面，并且500在1000的前面。但是如何在相同的 name 下，对 salary 反向排序？很简单，对它取反:

```python
>>> sorted(peeps, key=lambda x: (x['name'], -x['salary']))
[{'salary': 1000, 'name': 'Bill'}, {'salary': 500, 'name': 'Bill'}, {'salary': 500, 'name': 'Ted'}]
```

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



```
在Python 中，函数用 *args 来获取不确定数量的参数算是一种经典写法了。 于是 Python 3 里，这个概念被扩展到了平行赋值中：

```
```python
>>> a, b, *rest = range(5)

>>> a, b, rest (0, 1, [2, 3, 4])

>>> a, b, *rest = range(3)

>>> a, b, rest (0, 1, [2])

>>> a, b, *rest = range(2)

>>> a, b, rest (0, 1, [])
```

# list.append() 和 list.extend() 的区别 (tuple have no append and extend method)

append 加入元素，extend 加入可迭代对象。


# Python 装饰器 ([原文来自 stack overflow](https://stackoverflow.com/a/1594484))

## Decorator Basics

### Python’s functions are objects

To understand decorators, you must first understand that functions are objects in Python. This has important consequences. Let’s see why with a simple example :

```python
def shout(word="yes"):
    return word.capitalize()+"!"

print(shout())
# outputs : 'Yes!'

# As an object, you can assign the function to a variable like any other object 
scream = shout

# Notice we don't use parentheses: we are not calling the function,
# we are putting the function "shout" into the variable "scream".
# It means you can then call "shout" from "scream":

print(scream())
# outputs : 'Yes!'

# More than that, it means you can remove the old name 'shout',
# and the function will still be accessible from 'scream'

del shout
try:
    print(shout())
except NameError, e:
    print(e)
    #outputs: "name 'shout' is not defined"

print(scream())
# outputs: 'Yes!'
```

Keep this in mind. We’ll circle back to it shortly. 

Another interesting property of Python functions is they can be defined inside another function!

```python
def talk():

    # You can define a function on the fly in "talk" ...
    def whisper(word="yes"):
        return word.lower()+"..."

    # ... and use it right away!
    print(whisper())

# You call "talk", that defines "whisper" EVERY TIME you call it, then
# "whisper" is called in "talk". 
talk()
# outputs: 
# "yes..."

# But "whisper" DOES NOT EXIST outside "talk":

try:
    print(whisper())
except NameError, e:
    print(e)
    #outputs : "name 'whisper' is not defined"*
    #Python's functions are objects
```

### Functions references

Okay, still here? Now the fun part...

You’ve seen that functions are objects. Therefore, functions:

- can be assigned to a variable
- can be defined in another function

That means that **a function can return another function**.

```python
def getTalk(kind="shout"):

    # We define functions on the fly
    def shout(word="yes"):
        return word.capitalize()+"!"

    def whisper(word="yes") :
        return word.lower()+"...";

    # Then we return one of them
    if kind == "shout":
        # We don't use "()", we are not calling the function,
        # we are returning the function object
        return shout  
    else:
        return whisper

# How do you use this strange beast?

# Get the function and assign it to a variable
talk = getTalk()      

# You can see that "talk" is here a function object:
print(talk)
#outputs : <function shout at 0xb7ea817c>

# The object is the one returned by the function:
print(talk())
#outputs : Yes!

# And you can even use it directly if you feel wild:
print(getTalk("whisper")())
#outputs : yes...
```

There’s more! 

If you can `return` a function, you can pass one as a parameter:

```python
def doSomethingBefore(func): 
    print("I do something before then I call the function you gave me")
    print(func())

doSomethingBefore(scream)
#outputs: 
#I do something before then I call the function you gave me
#Yes!
```

Well, you just have everything needed to understand decorators. You see, decorators are “wrappers”, which means that **they let you execute code before and after the function they decorate** without modifying the function itself.

### Handcrafted decorators

How you’d do it manually:

```python
# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):

    # Inside, the decorator defines a function on the fly: the wrapper.
    # This function is going to be wrapped around the original function
    # so it can execute code before and after it.
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don't want to ever touch again.
def a_stand_alone_function():
    print("I am a stand alone function, don't you dare modify me")

a_stand_alone_function() 
#outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in 
# any code you want and return you a new function ready to be used:

a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs
```

Now, you probably want that every time you call `a_stand_alone_function`, `a_stand_alone_function_decorated` is called instead. That’s easy, just overwrite `a_stand_alone_function` with the function returned by `my_shiny_new_decorator`:

```python
a_stand_alone_function = my_shiny_new_decorator(a_stand_alone_function)
a_stand_alone_function()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs

# That’s EXACTLY what decorators do!
```

### Decorators demystified

The previous example, using the decorator syntax:

```python
@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")

another_stand_alone_function()  
#outputs:  
#Before the function runs
#Leave me alone
#After the function runs
```

Yes, that’s all, it’s that simple. `@decorator` is just a shortcut to:

```python
another_stand_alone_function = my_shiny_new_decorator(another_stand_alone_function)
```

Decorators are just a pythonic variant of the [decorator design pattern](http://en.wikipedia.org/wiki/Decorator_pattern). There are several classic design patterns embedded in Python to ease development (like iterators).

Of course, you can accumulate decorators:

```python
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
```

Using the Python decorator syntax:

```python
@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>
```

The order you set the decorators MATTERS:

```python
@ingredients
@bread
def strange_sandwich(food="--ham--"):
    print(food)

strange_sandwich()
#outputs:
##tomatoes#
#</''''''\>
# --ham--
#<\______/>
# ~salad~
```

### Now: to answer the question...

As a conclusion, you can easily see how to answer the question:

```python
# The decorator to make it bold
def makebold(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<b>" + fn() + "</b>"
    return wrapper

# The decorator to make it italic
def makeitalic(fn):
    # The new function the decorator returns
    def wrapper():
        # Insertion of some code before and after
        return "<i>" + fn() + "</i>"
    return wrapper

@makebold
@makeitalic
def say():
    return "hello"

print(say())
#outputs: <b><i>hello</i></b>

# This is the exact equivalent to 
def say():
    return "hello"
say = makebold(makeitalic(say))

print(say())
#outputs: <b><i>hello</i></b>
```

You can now just leave happy, or burn your brain a little bit more and see advanced uses of decorators.

------

## Taking decorators to the next level

### Passing arguments to the decorated function

```python
# It’s not black magic, you just have to let the wrapper 
# pass the argument:

def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(arg1, arg2):
        print("I got args! Look: {0}, {1}".format(arg1, arg2))
        function_to_decorate(arg1, arg2)
    return a_wrapper_accepting_arguments

# Since when you are calling the function returned by the decorator, you are
# calling the wrapper, passing arguments to the wrapper will let it pass them to 
# the decorated function

@a_decorator_passing_arguments
def print_full_name(first_name, last_name):
    print("My name is {0} {1}".format(first_name, last_name))

print_full_name("Peter", "Venkman")
# outputs:
#I got args! Look: Peter Venkman
#My name is Peter Venkman
```

### Decorating methods

One nifty thing about Python is that methods and functions are really the same. The only difference is that methods expect that their first argument is a reference to the current object (`self`). 

That means you can build a decorator for methods the same way! Just remember to take `self`into consideration:

```python
def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3 # very friendly, decrease age even more :-)
        return method_to_decorate(self, lie)
    return wrapper


class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am {0}, what did you think?".format(self.age + lie))

l = Lucy()
l.sayYourAge(-3)
#outputs: I am 26, what did you think?
```

If you’re making general-purpose decorator--one you’ll apply to any function or method, no matter its arguments--then just use `*args, **kwargs`:

```python
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    # The wrapper accepts any arguments
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print("Do I have args?:")
        print(args)
        print(kwargs)
        # Then you unpack the arguments, here *args, **kwargs
        # If you are not familiar with unpacking, check:
        # http://www.saltycrane.com/blog/2008/01/how-to-use-args-and-kwargs-in-python/
        function_to_decorate(*args, **kwargs)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("Python is cool, no argument here.")

function_with_no_argument()
#outputs
#Do I have args?:
#()
#{}
#Python is cool, no argument here.

@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)
#outputs
#Do I have args?:
#(1, 2, 3)
#{}
#1 2 3 

@a_decorator_passing_arbitrary_arguments
def function_with_named_arguments(a, b, c, platypus="Why not ?"):
    print("Do {0}, {1} and {2} like platypus? {3}".format(a, b, c, platypus))

function_with_named_arguments("Bill", "Linus", "Steve", platypus="Indeed!")
#outputs
#Do I have args ? :
#('Bill', 'Linus', 'Steve')
#{'platypus': 'Indeed!'}
#Do Bill, Linus and Steve like platypus? Indeed!

class Mary(object):

    def __init__(self):
        self.age = 31

    @a_decorator_passing_arbitrary_arguments
    def sayYourAge(self, lie=-3): # You can now add a default value
        print("I am {0}, what did you think?".format(self.age + lie))

m = Mary()
m.sayYourAge()
#outputs
# Do I have args?:
#(<__main__.Mary object at 0xb7d303ac>,)
#{}
#I am 28, what did you think?
```

### Passing arguments to the decorator

Great, now what would you say about passing arguments to the decorator itself? 

This can get somewhat twisted, since a decorator must accept a function as an argument. Therefore, you cannot pass the decorated function’s arguments directly to the decorator.

Before rushing to the solution, let’s write a little reminder: 

```python
# Decorators are ORDINARY functions
def my_decorator(func):
    print("I am an ordinary function")
    def wrapper():
        print("I am function returned by the decorator")
        func()
    return wrapper

# Therefore, you can call it without any "@"

def lazy_function():
    print("zzzzzzzz")

decorated_function = my_decorator(lazy_function)
#outputs: I am an ordinary function

# It outputs "I am an ordinary function", because that’s just what you do:
# calling a function. Nothing magic.

@my_decorator
def lazy_function():
    print("zzzzzzzz")

#outputs: I am an ordinary function
```

It’s exactly the same. "`my_decorator`" is called. So when you `@my_decorator`, you are telling Python to call the function 'labelled by the variable "`my_decorator`"'. 

This is important! The label you give can point directly to the decorator—**or not**. 

Let’s get evil. ☺

```python
def decorator_maker():

    print("I make decorators! I am executed only once: "
          "when you make me create a decorator.")

    def my_decorator(func):

        print("I am a decorator! I am executed only when you decorate a function.")

        def wrapped():
            print("I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()

        print("As the decorator, I return the wrapped function.")

        return wrapped

    print("As a decorator maker, I return a decorator")
    return my_decorator

# Let’s create a decorator. It’s just a new function after all.
new_decorator = decorator_maker()       
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator

# Then we decorate the function

def decorated_function():
    print("I am the decorated function.")

decorated_function = new_decorator(decorated_function)
#outputs:
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function

# Let’s call the function:
decorated_function()
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
```

No surprise here. 

Let’s do EXACTLY the same thing, but skip all the pesky intermediate variables:

```python
def decorated_function():
    print("I am the decorated function.")
decorated_function = decorator_maker()(decorated_function)
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function.

# Finally:
decorated_function()    
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
```

Let’s make it *even shorter*:

```python
@decorator_maker()
def decorated_function():
    print("I am the decorated function.")
#outputs:
#I make decorators! I am executed only once: when you make me create a decorator.
#As a decorator maker, I return a decorator
#I am a decorator! I am executed only when you decorate a function.
#As the decorator, I return the wrapped function.

#Eventually: 
decorated_function()    
#outputs:
#I am the wrapper around the decorated function. I am called when you call the decorated function.
#As the wrapper, I return the RESULT of the decorated function.
#I am the decorated function.
```

Hey, did you see that? We used a function call with the "`@`" syntax! :-)

So, back to decorators with arguments. If we can use functions to generate the decorator on the fly, we can pass arguments to that function, right?

```python
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):

    print("I make decorators! And I accept arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))

    def my_decorator(func):
        # The ability to pass arguments here is a gift from closures.
        # If you are not comfortable with closures, you can assume it’s ok,
        # or read: https://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python
        print("I am the decorator. Somehow you passed me arguments: {0}, {1}".format(decorator_arg1, decorator_arg2))

        # Don't confuse decorator arguments and function arguments!
        def wrapped(function_arg1, function_arg2) :
            print("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator

@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("I am the decorated function and only knows about my arguments: {0}"
           " {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments("Rajesh", "Howard")
#outputs:
#I make decorators! And I accept arguments: Leonard Sheldon
#I am the decorator. Somehow you passed me arguments: Leonard Sheldon
#I am the wrapper around the decorated function. 
#I can access all the variables 
#   - from the decorator: Leonard Sheldon 
#   - from the function call: Rajesh Howard 
#Then I can pass them to the decorated function
#I am the decorated function and only knows about my arguments: Rajesh Howard
```

Here it is: a decorator with arguments. Arguments can be set as variable:

```python
c1 = "Penny"
c2 = "Leslie"

@decorator_maker_with_arguments("Leonard", c1)
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("I am the decorated function and only knows about my arguments:"
           " {0} {1}".format(function_arg1, function_arg2))

decorated_function_with_arguments(c2, "Howard")
#outputs:
#I make decorators! And I accept arguments: Leonard Penny
#I am the decorator. Somehow you passed me arguments: Leonard Penny
#I am the wrapper around the decorated function. 
#I can access all the variables 
#   - from the decorator: Leonard Penny 
#   - from the function call: Leslie Howard 
#Then I can pass them to the decorated function
#I am the decorated function and only knows about my arguments: Leslie Howard
```

As you can see, you can pass arguments to the decorator like any function using this trick. You can even use `*args, **kwargs` if you wish. But remember decorators are called **only once**. Just when Python imports the script. You can't dynamically set the arguments afterwards. When you do "import x", **the function is already decorated**, so you can't change anything.

------

## Let’s practice: decorating a decorator

Okay, as a bonus, I'll give you a snippet to make any decorator accept generically any argument. After all, in order to accept arguments, we created our decorator using another function. 

We wrapped the decorator.

Anything else we saw recently that wrapped function?

Oh yes, decorators!

Let’s have some fun and write a decorator for the decorators:

```python
def decorator_with_args(decorator_to_enhance):
    """ 
    This function is supposed to be used as a decorator.
    It must decorate an other function, that is intended to be used as a decorator.
    Take a cup of coffee.
    It will allow any decorator to accept an arbitrary number of arguments,
    saving you the headache to remember how to do that every time.
    """

    # We use the same trick we did to pass arguments
    def decorator_maker(*args, **kwargs):

        # We create on the fly a decorator that accepts only a function
        # but keeps the passed arguments from the maker.
        def decorator_wrapper(func):

            # We return the result of the original decorator, which, after all, 
            # IS JUST AN ORDINARY FUNCTION (which returns a function).
            # Only pitfall: the decorator must have this specific signature or it won't work:
            return decorator_to_enhance(func, *args, **kwargs)

        return decorator_wrapper

    return decorator_maker
```

It can be used as follows:

```python
# You create the function you will use as a decorator. And stick a decorator on it :-)
# Don't forget, the signature is "decorator(func, *args, **kwargs)"
@decorator_with_args 
def decorated_decorator(func, *args, **kwargs): 
    def wrapper(function_arg1, function_arg2):
        print("Decorated with {0} {1}".format(args, kwargs))
        return func(function_arg1, function_arg2)
    return wrapper

# Then you decorate the functions you wish with your brand new decorated decorator.

@decorated_decorator(42, 404, 1024)
def decorated_function(function_arg1, function_arg2):
    print("Hello {0} {1}".format(function_arg1, function_arg2))

decorated_function("Universe and", "everything")
#outputs:
#Decorated with (42, 404, 1024) {}
#Hello Universe and everything

# Whoooot!
```

I know, the last time you had this feeling, it was after listening a guy saying: "before understanding recursion, you must first understand recursion". But now, don't you feel good about mastering this?

------

## Best practices: decorators

- Decorators were introduced in Python 2.4, so be sure your code will be run on >= 2.4. 
- Decorators slow down the function call. Keep that in mind.
- **You cannot un-decorate a function.** (There *are* hacks to create decorators that can be removed, but nobody uses them.) So once a function is decorated, it’s decorated *for all the code*.
- Decorators wrap functions, which can make them hard to debug. (This gets better from Python >= 2.5; see below.)

The `functools` module was introduced in Python 2.5. It includes the function `functools.wraps()`, which copies the name, module, and docstring of the decorated function to its wrapper. 

(Fun fact: `functools.wraps()` is a decorator! ☺)

```python
# For debugging, the stacktrace prints you the function __name__
def foo():
    print("foo")

print(foo.__name__)
#outputs: foo

# With a decorator, it gets messy    
def bar(func):
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__)
#outputs: wrapper

# "functools" can help for that

import functools

def bar(func):
    # We say that "wrapper", is wrapping "func"
    # and the magic begins
    @functools.wraps(func)
    def wrapper():
        print("bar")
        return func()
    return wrapper

@bar
def foo():
    print("foo")

print(foo.__name__)
#outputs: foo
```

------

## How can the decorators be useful?

**Now the big question:** What can I use decorators for? 

Seem cool and powerful, but a practical example would be great. Well, there are 1000 possibilities. Classic uses are extending a function behavior from an external lib (you can't modify it), or for debugging (you don't want to modify it because it’s temporary). 

You can use them to extend several functions in a DRY’s way, like so:

```python
def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print("{0} {1}".format(func.__name__, time.clock()-t))
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("{0} {1} {2}".format(func.__name__, args, kwargs))
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return str(reversed(string))

print(reverse_string("Able was I ere I saw Elba"))
print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))

#outputs:
#reverse_string ('Able was I ere I saw Elba',) {}
#wrapper 0.0
#wrapper has been used: 1x 
#ablE was I ere I saw elbA
#reverse_string ('A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!',) {}
#wrapper 0.0
#wrapper has been used: 2x
#!amanaP :lanac a ,noep a ,stah eros ,raj a ,hsac ,oloR a ,tur a ,mapS ,snip ,eperc a ,)lemac a ro( niaga gab ananab a ,gat a ,nat a ,gab ananab a ,gag a ,inoracam ,elacrep ,epins ,spam ,arutaroloc a ,shajar ,soreh ,atsap ,eonac a ,nalp a ,nam A
```

Of course the good thing with decorators is that you can use them right away on almost anything without rewriting. DRY, I said:

```python
@counter
@benchmark
@logging
def get_random_futurama_quote():
    from urllib import urlopen
    result = urlopen("http://subfusion.net/cgi-bin/quote.pl?quote=futurama").read()
    try:
        value = result.split("<br><b><hr><br>")[1].split("<br><br><hr>")[0]
        return value.strip()
    except:
        return "No, I'm ... doesn't!"


print(get_random_futurama_quote())
print(get_random_futurama_quote())

#outputs:
#get_random_futurama_quote () {}
#wrapper 0.02
#wrapper has been used: 1x
#The laws of science be a harsh mistress.
#get_random_futurama_quote () {}
#wrapper 0.01
#wrapper has been used: 2x
#Curse you, merciful Poseidon!
```

Python itself provides several decorators: `property`, `staticmethod`, etc. 

- Django uses decorators to manage caching and view permissions. 
- Twisted to fake inlining asynchronous functions calls.

This really is a large playground.

# 关于 Dictionary 的 View Object:

在 Python 3 中的字典 Dictionary 中，有 ```dict.keys() ```，```dict.values()```和 ```dict.items()```，使用它们返回的都将是被称作是  ```View objects``` 的对象。



在 python 3 的文档中：

> The objects returned by [`dict.keys()`](https://docs.python.org/3.3/library/stdtypes.html#dict.keys), [`dict.values()`](https://docs.python.org/3.3/library/stdtypes.html#dict.values) and [`dict.items()`](https://docs.python.org/3.3/library/stdtypes.html#dict.items) are *view objects*. They provide a dynamic view on the dictionary’s entries, which means that when the dictionary changes, the view reflects these changes.
>
> Dictionary views can be iterated over to yield their respective data, and support membership tests:
>
> - `len(dictview)`
>
>   Return the number of entries in the dictionary.
>
>
> - `iter(dictview)`
>
>   Return an iterator over the keys, values or items (represented as tuples of `(key, value)`) in the dictionary.Keys and values are iterated over in an arbitrary order which is non-random, varies across Python implementations, and depends on the dictionary’s history of insertions and deletions. If keys, values and items views are iterated over with no intervening modifications to the dictionary, the order of items will directly correspond. This allows the creation of `(value, key)` pairs using [`zip()`](https://docs.python.org/3.3/library/functions.html#zip): `pairs = zip(d.values(),d.keys())`. Another way to create the same list is `pairs = [(v, k) for (k, v) in d.items()]`.Iterating views while adding or deleting entries in the dictionary may raise a [`RuntimeError`](https://docs.python.org/3.3/library/exceptions.html#RuntimeError) or fail to iterate over all entries.

接下来我们可以做个试验：



```python
x = {'a':1,'b':2}
In [2]: x.items()
Out[2]: dict_items([('a', 1), ('b', 2)])
    
In [3]: x.values()
Out[3]: dict_values([1, 2])
    
In [4]: x.keys()
Out[4]: dict_keys(['a', 'b'])
```

我们可以看到整个 dict 中 keys，values 和 items 的视图。



```python
In [8]: len(x.keys())
Out[8]: 2


In [9]: len(x.values())
Out[9]: 2


In [10]: len(x.items())
Out[10]: 2
```

我们可以获得这个 object 的一些属性。



接下来，我们这样做：

```python
In [11]: iter(x.items())
Out[11]: <dict_itemiterator at 0x1103661d8>
```



我们就将这个 view object 转化成了一个iterator



如果我们想输出这个 iterator 的值，就用 next(itr)

```python
In [12]: next(iter(x.items()))
Out[12]: ('a', 1)
```

返回的就是一个 tuple。



还有一个函数，叫做 `iteritems()`，这个函数在 Python3 中已经被弃用了，现在的 `items()`函数实现的就是`iteritems()`的功能，这里就不再赘述。



# 关于generator, iterator 以及 range() 的一些问题

`a = range(100)`是一个 iterator 吗？

不是。

是一个 generator 吗？ 

也不是。

实时上 `generator`是`iterator`的一个特殊情况。



`range()`实际上是一个 class，这个通过这个 class 创造出来得实例（例如`range(100)`）是不可变的但是可迭代的对象 Object：immutable iterable objects.

所以 range() 创造出来得只是一个对象。



这个问题来自于https://stackoverflow.com/a/13092317

`range` is a <u>class of immutable iterable objects</u>. Their iteration behavior can be compared to `list`s: you can't call `next` directly on them; you have to get an iterator by using `iter`.

So no, `range` is not a generator.

You may be thinking, "why didn't they make it directly iterable"? Well, `range`s have some useful properties that wouldn't be possible that way:

- They are immutable, so they can be used as dictionary keys.
- They have the `start`, `stop` and `step` attributes (since Python 3.3), `count` and `index`methods and they support `in`, `len` and `__getitem__` operations.
- You can iterate over the same `range` multiple times.

------

```python
>>> myrange = range(1, 21, 2)
>>> myrange.start
1
>>> myrange.step
2
>>> myrange.index(17)
8
>>> myrange.index(18)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 18 is not in range
>>> it = iter(myrange)
>>> it
<range_iterator object at 0x7f504a9be960>
>>> next(it)
1
>>> next(it)
3
>>> next(it) 
5
```

但是 range() 这个类自身的方法当中，可以有类似于生成器的使用方法，例如`start()`, `step()`.

# 关于字典 update()

update() 返回 None，并不返回一个新的数组

如果字典当中有同样的 key，update() 只会把新的替换旧的，而不会因为大小而进行改变



```python
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

x.update(y)

{'a': 1, 'b': 3, 'c': 4}
```



如果我们对调一个顺序：



```python
x = {'a': 1, 'b': 3}
y = {'b': 2, 'c': 4}

x.update(y)

{'a': 1, 'b': 2, 'c': 4}
```

在 python 3.5 当中也有新的针对字典的拆包符 **

所以还有一个新的语法，可以把两个字典拼在一起：`z = {**x, **y}`

# 关于 Python 迭代器

生成器用完就被释放了，具体作用于：



```python
c = zip(a,b)
# 这时候 c 是一个 zip， 其实就是一个迭代器 iterator。
d = list(c)  # 经过 list 操作之后，作为迭代器的 zip 也就是 c 变量被释放了
print(list(c))  # 结果将是一个空的 list, 因为迭代器 c 当中已经没有元素了

```

同样，当我们对一个 iterator 进行 next 操作之后，被抛出的元素即刻被释放，再也找不回来了

所以如果我们先 next() 了一个迭代器，再 list 的话，结果不是原来版本的迭代器了

所以，迭代器是不能 reset 的，唯一的办法就是复制一个新的迭代器。

I see many answers suggesting [itertools.tee](http://docs.python.org/library/itertools.html?highlight=itertools.tee#itertools.tee), but that's ignoring one crucial warning in the docs for it:

> This itertool may require significant auxiliary storage (depending on how much temporary data needs to be stored). In general, if one iterator uses most or all of the data before another iterator starts, it is faster to use `list()` instead of `tee()`.

Basically, `tee` is designed for those situation where two (or more) clones of one iterator, while "getting out of sync" with each other, don't do so *by much* -- rather, they say in the same "vicinity" (a few items behind or ahead of each other). Not suitable for the OP's problem of "redo from the start".

`L = list(DictReader(...))` on the other hand is perfectly suitable, as long as the list of dicts can fit comfortably in memory. A new "iterator from the start" (very lightweight and low-overhead) can be made at any time with `iter(L)`, and used in part or in whole without affecting new or existing ones; other access patterns are also easily available.

# 如何将 26 个字母和它们的数字序号组成一个 Dictionary

```python
>>> import string

>>> a = list(string.ascii_lowercase)  # 产生所有的小写字母
... b = [x for x in range(1,26+1)]

>>> c=dict(zip(a,b))

>>> print(c)
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
```

# global 和 nonlocal 关键字的作用

```python
x = 5

def myfnc():

 print("inside myfnc", x)

 y = 10

 def myfnc2():

  global x

  nonlocal y

  print("inside myfnc2", x, y)

  x = 10

  print("x = ", x)

  y = 1

  print("y = ", y)

 myfnc2()

myfnc()

```



global 作用于 global 的作用域，nonlocal 试用于非 global 的父级作用域

# 如何去除 list 里多余的项目，最快的方法

思路，转换成 dict 然后再转回 list
```python
def function(seq):
    # Not order preserving
    return {}.fromkeys(seq).keys()
    # 这里用 keys() 是为了转换成以 key 为基础的视图，防止因为 list 太大而造成的内存浪费
    # fromkeys() 是以一个 sequence 来当做 key 生成 dict
```