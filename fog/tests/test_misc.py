#!/usr/bin/python2

from inspect import isfunction, isclass, ismethod

from .. import jobs


def test_docstrings():
    "Validate that all functions have docstrings"

    print "test"

    m = jobs
    for thing in m.__all__:
        if thing.startswith("__"):
            continue
        thething = getattr(m, thing)
        assert thething.__doc__ is not None, \
            repr(thing) + " is missing a doc string"

        if isclass(thething):  # we also want to check class members:
            print "checking", repr(thething), "is a class"
            for mthing in dir(thething):
                if mthing.startswith("__"):
                    continue
                themthing = getattr(thething, mthing)
                if isfunction(themthing) or ismethod(themthing):
                    assert themthing.__doc__ is not None, \
                        repr(themthing) + " is missing a doc string"