import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename="myapp.log",
    filemode="+a",
)

logging.debug("Debug message")

logging.info("Informative message")

logging.error("Error message")
