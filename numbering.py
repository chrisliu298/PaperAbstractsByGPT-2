f = open("valid_set_generation.md", "r").readlines()


with open("valid_set_generation_numbered.md", "w+") as numbering:
    count = 1
    for i in f:
        numbering.write(f"{count}. " + i)
        count += 1

numbering.close()