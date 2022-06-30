import logging
logging.basicConfig(filename="logerr.log",level=logging.INFO)
logging.info("This is my very first code for logging")
logging.error("This is error from the system")

l=[1,2,3,4,5,6,7,7]
for i in l:
    if i%2==0:
        logging.info(f"{i} is even number")
        logging.warning("This is warning from the system")
logging.shutdown()
