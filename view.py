def view(variable):
    myIdNAME = 0
    myFIND = globals().copy().keys()
    myID = id(variable)
    
    for i in myFIND:
        if id(globals()[i]) == myID :
            myIdNAME = i
            break
            
    print("Variable Name : \" "+myIdNAME+" \"\n")
    print("Methods and Result : \n")
    
    myFIND = dir(variable)
    
    for i in myFIND :  
        print(i)
        print(eval(myIdNAME+"."+i))
        print("\n")   
        
    return

if "__name__" == "__main__" :
    a = 0
    view(a)
"""
a = 0
view(a)

It may output likes that :

Variable Name : " a "

Methods and Result : 

__abs__
<method-wrapper '__abs__' of int object at 0x00000275C17D6910>


__add__
<method-wrapper '__add__' of int object at 0x00000275C17D6910>


__and__
<method-wrapper '__and__' of int object at 0x00000275C17D6910>


__bool__
<method-wrapper '__bool__' of int object at 0x00000275C17D6910>


__ceil__
<built-in method __ceil__ of int object at 0x00000275C17D6910>


__class__
<class 'int'>


__delattr__
<method-wrapper '__delattr__' of int object at 0x00000275C17D6910>


__dir__
<built-in method __dir__ of int object at 0x00000275C17D6910>


__divmod__
<method-wrapper '__divmod__' of int object at 0x00000275C17D6910>


__doc__
int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4


__eq__
<method-wrapper '__eq__' of int object at 0x00000275C17D6910>


__float__
<method-wrapper '__float__' of int object at 0x00000275C17D6910>


__floor__
<built-in method __floor__ of int object at 0x00000275C17D6910>


__floordiv__
<method-wrapper '__floordiv__' of int object at 0x00000275C17D6910>


__format__
<built-in method __format__ of int object at 0x00000275C17D6910>


__ge__
<method-wrapper '__ge__' of int object at 0x00000275C17D6910>


__getattribute__
<method-wrapper '__getattribute__' of int object at 0x00000275C17D6910>


__getnewargs__
<built-in method __getnewargs__ of int object at 0x00000275C17D6910>


__gt__
<method-wrapper '__gt__' of int object at 0x00000275C17D6910>


__hash__
<method-wrapper '__hash__' of int object at 0x00000275C17D6910>


__index__
<method-wrapper '__index__' of int object at 0x00000275C17D6910>


__init__
<method-wrapper '__init__' of int object at 0x00000275C17D6910>


__init_subclass__
<built-in method __init_subclass__ of type object at 0x00007FFA17020FD0>


__int__
<method-wrapper '__int__' of int object at 0x00000275C17D6910>


__invert__
<method-wrapper '__invert__' of int object at 0x00000275C17D6910>


__le__
<method-wrapper '__le__' of int object at 0x00000275C17D6910>


__lshift__
<method-wrapper '__lshift__' of int object at 0x00000275C17D6910>


__lt__
<method-wrapper '__lt__' of int object at 0x00000275C17D6910>


__mod__
<method-wrapper '__mod__' of int object at 0x00000275C17D6910>


__mul__
<method-wrapper '__mul__' of int object at 0x00000275C17D6910>


__ne__
<method-wrapper '__ne__' of int object at 0x00000275C17D6910>


__neg__
<method-wrapper '__neg__' of int object at 0x00000275C17D6910>


__new__
<built-in method __new__ of type object at 0x00007FFA17020FD0>


__or__
<method-wrapper '__or__' of int object at 0x00000275C17D6910>


__pos__
<method-wrapper '__pos__' of int object at 0x00000275C17D6910>


__pow__
<method-wrapper '__pow__' of int object at 0x00000275C17D6910>


__radd__
<method-wrapper '__radd__' of int object at 0x00000275C17D6910>


__rand__
<method-wrapper '__rand__' of int object at 0x00000275C17D6910>


__rdivmod__
<method-wrapper '__rdivmod__' of int object at 0x00000275C17D6910>


__reduce__
<built-in method __reduce__ of int object at 0x00000275C17D6910>


__reduce_ex__
<built-in method __reduce_ex__ of int object at 0x00000275C17D6910>


__repr__
<method-wrapper '__repr__' of int object at 0x00000275C17D6910>


__rfloordiv__
<method-wrapper '__rfloordiv__' of int object at 0x00000275C17D6910>


__rlshift__
<method-wrapper '__rlshift__' of int object at 0x00000275C17D6910>


__rmod__
<method-wrapper '__rmod__' of int object at 0x00000275C17D6910>


__rmul__
<method-wrapper '__rmul__' of int object at 0x00000275C17D6910>


__ror__
<method-wrapper '__ror__' of int object at 0x00000275C17D6910>


__round__
<built-in method __round__ of int object at 0x00000275C17D6910>


__rpow__
<method-wrapper '__rpow__' of int object at 0x00000275C17D6910>


__rrshift__
<method-wrapper '__rrshift__' of int object at 0x00000275C17D6910>


__rshift__
<method-wrapper '__rshift__' of int object at 0x00000275C17D6910>


__rsub__
<method-wrapper '__rsub__' of int object at 0x00000275C17D6910>


__rtruediv__
<method-wrapper '__rtruediv__' of int object at 0x00000275C17D6910>


__rxor__
<method-wrapper '__rxor__' of int object at 0x00000275C17D6910>


__setattr__
<method-wrapper '__setattr__' of int object at 0x00000275C17D6910>


__sizeof__
<built-in method __sizeof__ of int object at 0x00000275C17D6910>


__str__
<method-wrapper '__str__' of int object at 0x00000275C17D6910>


__sub__
<method-wrapper '__sub__' of int object at 0x00000275C17D6910>


__subclasshook__
<built-in method __subclasshook__ of type object at 0x00007FFA17020FD0>


__truediv__
<method-wrapper '__truediv__' of int object at 0x00000275C17D6910>


__trunc__
<built-in method __trunc__ of int object at 0x00000275C17D6910>


__xor__
<method-wrapper '__xor__' of int object at 0x00000275C17D6910>


as_integer_ratio
<built-in method as_integer_ratio of int object at 0x00000275C17D6910>


bit_length
<built-in method bit_length of int object at 0x00000275C17D6910>


conjugate
<built-in method conjugate of int object at 0x00000275C17D6910>


denominator
1


from_bytes
<built-in method from_bytes of type object at 0x00007FFA17020FD0>


imag
0


numerator
0


real
0


to_bytes
<built-in method to_bytes of int object at 0x00000275C17D6910>

"""
  
