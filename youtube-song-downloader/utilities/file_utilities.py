#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint

def read_file(filename):
    results = []
    with open(filename, "r") as stream:
        for line in stream:
            results.append(line.strip())

    return results

def write_to_file(filename, contents):
    with open(filename, "w") as stream:
        for content in contents:
            stream.write(content + '\n')
