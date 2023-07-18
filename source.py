#ete stexcvox class-um linen aynpisi attribut-ner voronc arjeqy chi hamapatasxanum __annotations__-um nshvac type-in apa ayd attribut-y kjnjvi ayd class-ic
class checkMeta(type):
    def __new__(cls, name, bases, attrs):
        self = super().__new__(cls, name, bases, attrs)
        for attr_name, attr_value in attrs.items():
            if hasattr(cls, '__annotations__'):
                if self.__annotations__.get(attr_name):
                    if isinstance(attr_value, self.__annotations__.get(attr_name)):
                        print(f"{attr_name} valid")
                    else:
                        delattr(self, attr_name)
            else:
                print('this class cannot be checked because it does not contain the "annotations" field')
        return self

class Point(metaclass=checkMeta):#orinak ays depqum kjnjvi name-y qani vor parunakum e int type-i arjeq
    name:str
    age:int
    name = 10
    age = 100

print(Point.__dict__)

