class Test:
    leaves = 8
    @classmethod
    def august_leaves(cls,name):
        print(f"{name} has {cls.leaves} for the month of august")

    @staticmethod
    def yearly_leaves():
        print("Capgemini employees should take 25 leaves in 1 year")


sreekar = Test()

sreekar.august_leaves("sreekar")
sreekar.yearly_leaves()
Test.august_leaves("Aditya")


