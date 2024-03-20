# explanations for member functions are provided in requirements.py
# each file that uses a cuckoo hash should import it from this file.
import random as rand
from typing import List,Optional

class CuckooHash:
	def __init__(self, init_size: int):
		self.__num_rehashes = 0
		self.CYCLE_THRESHOLD = 10

		self.table_size = init_size
		self.tables = [[None]*init_size for _ in range(2)]

	def hash_func(self, key: int, table_id: int) -> int:
		key = int(str(key) + str(self.__num_rehashes) + str(table_id))
		rand.seed(key)
		return rand.randint(0, self.table_size-1)

	def get_table_contents(self) -> List[List[Optional[int]]]:
		return self.tables

	# you should *NOT* change any of the existing code above this line
	# you may however define additional instance variables inside the __init__ method.
    
	def insert(self, key: int) -> bool:
		# Initialize the table_id to 0
		table_id = 0
		# Loop for the specified number of cycles (CYCLE_THRESHOLD + 1)
		for _ in range(self.CYCLE_THRESHOLD + 1):
			# Calculate the index using the hash function
			index = self.hash_func(key, table_id)
			# Check if the slot is empty
			if self.tables[table_id][index] is None:
				# Insert the key if the slot is empty
				self.tables[table_id][index] = key
				return True
			else:
				# Swap the current key with the new key and continue searching in the other table
				key, self.tables[table_id][index] = self.tables[table_id][index], key
				table_id = 1 - table_id

		# If CYCLE_THRESHOLD is reached, return False to indicate a cycle
		return False

	def lookup(self, key: int) -> bool:
		# Loop through both tables
		for table_id in range(2):
			# Calculate the index using the hash function
			index = self.hash_func(key, table_id)
			# Check if the key is found in the current slot
			if self.tables[table_id][index] == key:
				# Key found in the current slot
				return True

		# Key not found in either table
		return False

	def delete(self, key: int) -> None:
		# Loop through both tables
		for table_id in range(2):
			# Calculate the index using the hash function
			index = self.hash_func(key, table_id)
			# Check if the key is found in the current slot
			if self.tables[table_id][index] == key:
				# Delete the key by setting the slot to None
				self.tables[table_id][index] = None
				return

	def rehash(self, new_table_size: int) -> None:
		# Increment the number of rehashes
		self.__num_rehashes += 1
		# Set the new table size
		self.table_size = new_table_size  # do not modify this line
		# Create a copy of the current tables
		old_tables = self.tables.copy()

		# Initialize new tables with the updated size
		self.tables = [[None] * new_table_size for _ in range(2)]

		# Reinsert keys from the old tables into the new tables
		for table_id in range(2):
			for key in old_tables[table_id]:
				if key is not None:
					self.insert(key)


	# feel free to define new methods in addition to the above
	# fill in the definitions of each required member function (above),
	# and for any additional member functions you define

