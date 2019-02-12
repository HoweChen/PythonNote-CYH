import collections
import itertools
from multiprocessing import Pool


class SimpleMapReduce():
    def __init__(self, map_func, reduce_func=None, processes=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = Pool(processes=processes)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(self.map_func, inputs, chunksize=chunksize)

        if self.reduce_func is None:
            return
        partitioned_data = self.partition(itertools.chain(*map_responses))
        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values
