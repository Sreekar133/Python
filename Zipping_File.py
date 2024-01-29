a = [(1,"one","ek"),(2,"two","do"),(3,"three","teen")]

b = ["number","spelling","hindi_spelling"]

for i in a:
    zip_object = zip(b,i)
    # print(zip_object)
    # for j in zip(b,i):
    #     print(j)
    output_dict=dict(zip_object)
    print(output_dict)