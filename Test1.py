import logging as log
log.basicConfig(filename = "Test1.log", level = log.DEBUG, format='%(levelname)s (%(asctime)s %(name)s %(message)s ')
def divide(a,b):
    try:
        log.info("We are into function")
        s= a/b
        log.info(f"output of division is {s}")
        log.info("We have completed a division")
        with open("test3.log","r"):
            log.info("Was able to read file test1.log")

        return s
    except Exception as  e:
        log.exception(e)
        log.critical("unable to read the file test1.log")
        log.error(e)


val1 = int(input("Enter first value : "))
val2 = int(input("Enter second value: "))

divide(val1,val2)
log.shutdown()