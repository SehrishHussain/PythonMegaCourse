contents = ["All carrots are to be sliced"
            "more to add",
            "The carrots were sliced","The slicing was done well"]

filenames = ["work.txt", "process.txt", "done.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)