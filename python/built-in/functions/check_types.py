# only nums

print('123a'.isnumeric())
#=> False

print('123'.isnumeric())
#=> True

# only alpha

print('123a'.isalpha())
#=> False

print('a'.isalpha())
#=> True

# only nums and alpha

print('123abc...'.isalnum())
#=> False

print('123abc'.isalnum())
#=> True