import logging
import logging as log
log.basicConfig(filename = "test2.log",level=logging.DEBUG, format='%(levelname)s (%(asctime)s %(name)s %(message)s ')
def divide(a,b):
    try:
        logging.info("We are into function")
        s= a/b

        logging.info(f"output of division is {s}")
        logging.info("We have completed a division")
        return s
    except Exception as  e:
        log.exception(e)


divide(4,3)