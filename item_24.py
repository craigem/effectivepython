#!/usr/bin/env python3

'''Item 24 from Effective Python'''


# Example 1
''' you’re writing a MapReduce implementation and you want a common class to
represent the input data, define such a class with a read method that must be
defined by subclasses '''

class InputData(object):
    def read(self):
        raise NotImplementedError


# Example 2
''' a concrete subclass of InputData that reads data from a file on disk '''

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


# Example 3
''' You'd want a similar abstract interface for the MapReduce worker that
consumes the input data in a standard way '''

class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


# Example 4
''' define a concrete subclass of Worker to implement the specific MapReduce
function '''

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


# Example 5
''' simplest approach is to manually build and connect the objects with some
helper functions '''

import os

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


# Example 6
''' create the LineCountWorker instances using the InputData instances returned
by generate_inputs '''

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


# Example 7
''' execute these Worker instances by fanning out the map step to multiple
threads. Call reduce repeatedly to combine the results into one final value '''

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


# Example 8
''' connect all of the pieces together in a function to run each step '''

def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


# Example 9
''' Running this function on a set of test input files works great '''
print('Example 9:\n==========')

from tempfile import TemporaryDirectory
import random

def write_test_files(tmpdir):
    for i in range(100):
        with open(os.path.join(tmpdir, str(i)), 'w') as f:
            f.write('\n' * random.randint(0, 100))

with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = mapreduce(tmpdir)

print('There are', result, 'lines')


# Example 10
''' extend the InputData class with a generic class method thats responsible
for creating new InputData instances using a common interface '''

class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


# Example 11
''' use the config to find the directory to list for input files '''

class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


# Example 12
''' construct instances of the GenericWorker concrete subclass using cls() as a
generic constructor '''

class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


# Example 13
''' The effect on GenericWorker subclass is nothing more than changing its
parent class '''

class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


# Example 14
''' rewrite the mapreduce function to be completely generic '''

def mapreduce(worker_class, input_class, config):
	workers = worker_class.create_workers(input_class, config)
	return execute(workers)


# Example 15
''' difference is that the mapreduce function requires more parameters so that it can operate generically '''
print('\nExample 15:\n==========')

with TemporaryDirectory() as tmpdir:
	write_test_files(tmpdir)
	config = {'data_dir': tmpdir}
	result = mapreduce(LineCountWorker, PathInputData, config)
print('There are', result, 'lines')
