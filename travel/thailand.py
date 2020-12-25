class ThailandPackage:
    def detail(self):
        print("Thailand Travel Package")

if __name__ == "__main__": # if this name is main
    print("Thailand module started")
    print("this sentence only kicks when module runs itself")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("Thailand moudle has been called from outside of the module")