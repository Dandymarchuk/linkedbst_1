from time import time
from random import randint, shuffle


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.height = 1


class LinkedBST:
	def add(self, root, key):
	
		if not root:
			return Node(key)
		elif key < root.data:
			root.left = self.add(root.left, key)
		else:
			root.right = self.add(root.right, key)

		root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

		balance = self.get_balance(root)

		if balance > 1 and key < root.left.data:
			return self.right_rotate(root)

		if balance < -1 and key > root.right.data:
			return self.left_rotate(root)

		if balance > 1 and key > root.left.data:
			root.left = self.left_rotate(root.left)
			return self.right_rotate(root)

		if balance < -1 and key < root.right.data:
			root.right = self.right_rotate(root.right)
			return self.left_rotate(root)

		return root


	def left_rotate(self, z):

		y = z.right
		T2 = y.left

		y.left = z
		z.right = T2

		z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

		return y


	def right_rotate(self, z):

		y = z.left
		T3 = y.right

		y.right = z
		z.left = T3

		z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
		y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

		return y


	def get_height(self, root):
		return 0 if not root else root.height


	def get_balance(self, root):
		if not root:
			return 0

		return self.get_height(root.left) - self.get_height(root.right)


	def pre_order(self, root):
		if not root:
			return

		print("{0} ".format(root.data), end="")
		self.pre_order(root.left)
		self.pre_order(root.right)


	def find(self, root, item: int):
		def recurse(node):
			if node is None:
				return None
			elif item == node.data:
				return node.data
			elif item < node.data:
				return recurse(node.left)
			else:
				return recurse(node.right)

		return recurse(root)


	def demo_bst(self, path: str):
		if path is None or path == '':
			raise ValueError()

		with open(path) as f:
			words = sorted(f.read().splitlines())

		CHOICES_AMOUNT = 10000
		WORDS_AMOUNT = len(words)

		# 1
		start = time()

		for _ in range(CHOICES_AMOUNT):
			index = randint(0, WORDS_AMOUNT - 1)
			word = words[index]
			_ = words.index(word)

		end = time()

		print(f'searching 10 000 random words in list in {end - start} seconds')

		# 2 - maximum recursion depth exceeded while adding words

		# 3
		shuffle(words)

		start = time()

		randomized_tree = LinkedBST()
		randomized_root = None

		for word in words:
			randomized_root = randomized_tree.add(randomized_root, word)

		for _ in range(CHOICES_AMOUNT):
			index = randint(0, WORDS_AMOUNT - 1)
			word = words[index]
			_ = randomized_tree.find(randomized_root, word)

		end = time()

		print(f'adding randomized list to tree and searching 10 000 random words in {end - start} seconds')

		# 4
		words.sort()
		
		start = time()

		tree = LinkedBST()
		root = None

		for word in words:
			root = tree.add(root, word)

		for _ in range(CHOICES_AMOUNT):
			index = randint(0, WORDS_AMOUNT - 1)
			word = words[index]
			_ = tree.find(root, word)

		end = time()

		print(f'adding sorted list to tree and searching 10 000 random words in {end - start} seconds')


# add YOUR FILE PATH HERE
LinkedBST().demo_bst("")
