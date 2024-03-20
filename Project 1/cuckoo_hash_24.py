# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List,Optional

class CuckooHash24:
    def __init__(self, init_size: int):
        self.__num_rehashes = 0
        self.bucket_size = 4
        self.CYCLE_THRESHOLD = 10
        self.table_size = init_size
        self.tables = [[None] * init_size for _ in range(2)]

    def get_rand_idx_from_bucket(self, bucket_idx: int, table_id: int) -> int:
		# you must use this function when you need to displace a random key from a bucket during insertion (see the description in requirements.py). 
		# this function randomly chooses an index from a given bucket for a given table. this ensures that the random 
		# index chosen by your code and our test script match.
		# 
		# for example, if you are inserting some key x into table 0, and hash_func(x, 0) returns 5, and the bucket in index 5 of table 0 already has 4 elements,
		# you will call get_rand_bucket_index(5, 0) to determine which key from that bucket to displace, i.e. if get_random_bucket_index(5, 0) returns 2, you
		# will displace the key at index 2 in that bucket.
        rand.seed(int(str(bucket_idx) + str(table_id)))
        return rand.randint(0, self.bucket_size - 1)

    def hash_func(self, key: int, table_id: int) -> int:
        key = int(str(key) + str(self.__num_rehashes) + str(table_id))
        rand.seed(key)
        return rand.randint(0, self.table_size - 1)

    def get_table_contents(self) -> List[List[Optional[List[int]]]]:
        # the buckets should be implemented as lists. Table cells with no elements should still have None entries.
        return self.tables

    def insert(self, key: int) -> bool:
        # TODO: Implement key insertion with double hashing
        current_table_id = 0
        for _ in range(self.CYCLE_THRESHOLD + 1):
            # Calculate the bucket index using hash_func
            current_bucket_idx = self.hash_func(key, current_table_id)
            # Retrieve the bucket at the calculated index
            current_bucket = self.tables[current_table_id][current_bucket_idx]

            # If the bucket is None, create a new bucket with the key
            if current_bucket is None:
                self.tables[current_table_id][current_bucket_idx] = [key]
                return True
            # If the bucket has space, append the key to it
            elif len(current_bucket) < self.bucket_size:
                current_bucket.append(key)
                return True
            # The bucket is full, so displace a key and continue the process
            else:
                displaced_idx = self.get_rand_idx_from_bucket(current_bucket_idx, current_table_id)
                temp = current_bucket[displaced_idx]
                current_bucket[displaced_idx] = key
                key = temp
                current_table_id = 1 - current_table_id
        return False


    def lookup(self, key: int) -> bool:
        # TODO: Implement key lookup with double hashing
        hash_value1 = self.hash_func(key, 0)
        hash_value2 = self.hash_func(key, 1)
        if (self.tables[0][hash_value1] is not None and key in self.tables[0][hash_value1]) or (self.tables[1][hash_value2] is not None and key in self.tables[1][hash_value2]):
            return True
        return False


    def delete(self, key: int) -> None:
        # TODO: Implement key deletion with double hashing
        for current_table_id in range(2):
            current_bucket_idx = self.hash_func(key, current_table_id)
            current_bucket = self.tables[current_table_id][current_bucket_idx]
            
            # Check if the bucket exists and the key is in the bucket
            if current_bucket is not None and key in current_bucket:
                # Remove the key from the bucket
                current_bucket.remove(key)

                # Check if the bucket is now empty, set to None if so
                if len(current_bucket) == 0:
                    self.tables[current_table_id][current_bucket_idx] = None
                return
        return

    def rehash(self, new_table_size: int) -> None:
        # Increase the number of rehashes
        self.__num_rehashes += 1; 
        old_table_size = self.table_size
        self.table_size = new_table_size # do not modify this line
        # TODO: Rehash the keys to the new table size
        
        # Check if the new table size is valid
        if new_table_size <= 0:
            raise ValueError("New table size must be a positive integer.")

        # Store the keys from the old tables
        old_tables = self.get_table_contents()
        # Initialize new empty tables with the new size
        self.tables = [[None] * new_table_size for _ in range(2)]
        
        # Copy keys from old tables to the new tables
        for i in range(old_table_size):
            if old_tables[0][i] is not None:
                for num in old_tables[0][i]:
                    self.insert(num)

        for i in range(old_table_size):
            if old_tables[1][i] is not None:
                for num in old_tables[1][i]:
                    self.insert(num)
