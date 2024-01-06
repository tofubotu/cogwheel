import sys
class Linkable:
    _id_counter = 1

    def __init__(self,name="Link"):
        self._id_counter = 1 # ainult iga instantsi puhul...
        self.links = []  # linkide tuplid 
        self.name = f"{name}-{Linkable._id_counter:04d}"
        print(self.name)
        Linkable._id_counter += 1
        #self._id_counter += 1

    def link_to(self, other, threshold=1.0):
        if not any(link[0] == other for link in self.links):
            self.links.append((other, threshold))

    def unlink_from(self, other):
        #self.links = [(link, thres) for link, thres in self.links if link != other]
        for i, (link, thres) in enumerate(self.links):
            if link == other:
                self.links[i]=(None,thres)
            


    def print_links(self):
        sorted_links = sorted(self.links, key=lambda x: x[1], reverse=True)
        for link, thres in sorted_links:
            link_status = link.name if isinstance(link, Linkable) else 'DEAD'
            print(f"{self.name} -> {link_status} (Strength: {thres})")

class ClassA(Linkable):
    pass

class ClassB(Linkable):
    pass

class Linker:
    def __init__(self):
        self.objects = []

    def create_object(self, cls, name='Link'):
        obj = cls(name)
        self.objects.append(obj)
        return obj

    def link_objects(self, obj1, obj2, threshold=1.0):
        obj1.link_to(obj2, threshold)
        obj2.link_to(obj1, threshold)

    def delete_object(self, obj):
        for o in self.objects:
            o.unlink_from(obj)
        self.objects.remove(obj)

# Example usage
if __name__ == "__main__":

    linker = Linker()

    a1 = linker.create_object(ClassA, 'a1')
    b1 = linker.create_object(ClassB, 'b1')
    b2 = linker.create_object(ClassB, 'b2')
    b3 = linker.create_object(ClassB, 'b3')
    b4 = linker.create_object(ClassB, 'b4')
    b5 = linker.create_object(ClassB, 'b5')

    linker.link_objects(a1, b1, 0.8)
    linker.link_objects(a1, b2, 0.9)
    linker.link_objects(a1, b3, 0.4)
    linker.link_objects(a1, b4, 1.0)
    linker.link_objects(b4, b2, 1.0)
    linker.link_objects(b4, b1, 1.0)
    linker.link_objects(b5,a1,0.714)

    #del b1
    #linker.delete_object(b1)
    b2.unlink_from(a1)
    a1.print_links()
    b2.print_links()
    #print("b1")
    b1.print_links()



