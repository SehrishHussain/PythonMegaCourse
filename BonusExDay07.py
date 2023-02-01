filenames = ["1.doc", "1.report", "1.presentation"]
filenames_new = []
def replace(items):
    return items.replace('.', '-')
for items in filenames:
    print(map(replace, items))
    #print("items", items)

