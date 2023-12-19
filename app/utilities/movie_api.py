# importing the module
import imdb
# creating an instance of the IMDB()
ia = imdb.IMDb()
# Using the Search movie method
items = ia.search_movie('Surreal Estate')


for i in items:
	print(dir(i))
	# print(i.items())
	print(i.keys())
	# print(i.summary())
	print(i)
