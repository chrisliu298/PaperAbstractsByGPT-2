f = open("valid_set_generation.md", "r").readlines()


with open("valid_set_generation_numbered.md", "w+") as numbering:
    count = 1
    for i in f:
        if count % 3 == 1:
            numbering.write(f"{count}. " + i)
        else:
            numbering.write(i)
        count += 1

numbering.close()