def sort_contacts(contact_dict):
    #turn the dictionary into a list (of, hmm, items?)
    listy = list(contact_dict.items())
    #create an empty list (that the tuples will go into)
    output = []
    #iterate over the items in the list  (ex: for something in something)
    for item in listy:
        (name, number, email) = (item[0], item[1][0], item[1][1])
        tuple1 = (name, number, email)
        output.append(tuple1)
    #we assign, as a tuple, the values in the dictionary list
        #note a tuple is like this `(val1, val2, etc...)`
        #a tuple is different from a list in that it's values cannot be modified, or that it is `"immutable"`
        #but, you can access values in a `tuple` the same way you can access a `list`.
        #ie `tuple[0], tuple[1]`
    #sort the list
    output.sort()
    #return the list
    return output
