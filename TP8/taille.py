import os

def taille(ref="."):
	return os.stat(ref).st_size