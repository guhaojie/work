class ORGANIZATION:
    def __init__(self, info):
        self.name = ""
        self.type = ""
        self.CEO = ""
        self.parent = None
        self.children = []
        self.__dict__.update(info)

    def __str__(self):
        x = "\\_" if self.parent else ""
        x += f"{self.name}"
        for _ in self.children:
            temp = f"\n{_}".replace('\n', '\n\t')
            x += f"{temp}"
        return x


a = ORGANIZATION({'name': '支部一'})
b = ORGANIZATION({'name': '总支二'})
c = ORGANIZATION({'name': '党委一'})
d = ORGANIZATION({'name': '党委二'})
e = ORGANIZATION({'name': '党委三'})

a.parent = b
b.children.append(a)
b.parent = c
c.children.append(b)
c.parent = e
e.children.append(c)
d.parent = e
e.children.append(d)
print(e)
