#! /usr/bin/env python3
#-*- conding utf-8 -*-

class Dict():
    """
    A dictionary that can be sorted and wich keep the order of insertion
    """


    def __init__(self, **kwargs):
        self.keys = []
        self.values = []

        for k, v in kwargs.items():
            self.keys.append(k)
            self.values.append(v)

    def __getitem__(self, index):

        i = self.keys.index(index)
        return self.values[i]

    def __setitem__(self, index, value):

        try :
            i = self.keys.index(index)
            self.values[i] = value

        except ValueError:
            self.keys.append(index)
            self.values.append(value)

    def __delitem__(self, index):

        i = self.keys.index(index)
        del self.keys[i]
        del self.values[i]

    def __contains__(self, index):

        if (index in self.keys) :
            return True
        else :
            return False

    def __len__(self):
        return len(self.keys)

    def __str__(self):
        string = "{"
        for i in range (len(self.keys)):
            if (i != 0):
                string += ", "
            string += "{}: {}".format(self.keys[i], self.values[i])
        string += "}"
        return string

    def __repr__(self):
        return str(self)

    def __add__(self, val):
        if isinstance(self, type(val)):
            new = Dict()
            new.keys = self.keys.copy()
            new.values = self.values.copy()
            new.keys += val.keys
            new.values += val.values
            return new

        return self

    def swap(self, first, sec):

        if first >= len(self) or first < 0:
            raise IndexError("Dict index out of range")

        if sec >= len(self) or sec < 0:
            raise IndexError("Dict index out of range")

        ktmp = self.keys[first]
        vtmp = self.values[first]

        self.keys[first] = self.keys[sec]
        self.values[first] = self.values[sec]

        self.keys[sec] = ktmp
        self.values[sec] = vtmp

    def lkeys(self):
        return self.keys

    def lvalues(self):
        return self.values

    def litems(self):
        return self.keys, self.values

    def reverse(self):

        newk = []
        newv = []
        i = len(self.keys) - 1
        while (i >= 0):
            newk.append(self.keys[i])
            newv.append(self.values[i])
            i -= 1

        self.keys = newk
        self.values = newv

    def sort(self):

        tmpk = sorted(self.keys)
        tmpv = []
        for key in tmpk:
            tmpv.append(self[key])

        self.keys = tmpk
        self.values = tmpv
