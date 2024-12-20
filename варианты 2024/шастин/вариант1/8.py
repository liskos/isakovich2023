k = 0
for s1 in "аклош":
    for s2 in "аклош":
        for s3 in "аклош":
            for s4 in "аклош":
                for s5 in "аклош":
                    s = s1 + s2 + s3 + s4 + s5
                    k += 1
                    if s == "шалаш":
                        print(k)
