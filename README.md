# python-easy-logging

A simple decorator that cuts down on the lines of code added when logging function start and stop.

Also! Logs saved in logs/ can be ingested by elasticsearch using filebeat without any further parsing, 'cause JSON!


## Refer `main.py` for the magic!

### Old school logging
```python3
def func_old():
    start = datetime.datetime.now()
    logger.info('func_old started')
    logger.info('I hail from the stone age')
    logger.warning('This is how you would have done logging normally!')
    time.sleep(3)
    end = datetime.datetime.now()
    logger.critical('Not anymore.')
    logger.info('func_old ended')
    logger.info('Exec took: {}'.format(end-start))
```

### New Era

```python3
@timeit
def func_new():
    """new way of logging function in main"""
    # doc string is compulsory. Last keyword gets used to identify the parent file from where function is defined.
    import time
    time.sleep(5)
```

### Additional parameters

If there is other metadata you'd like to attach with your log, use this instead of the default `logging`

```python3
from helpers import log_line
import logging

# define logger 
logger = logging.getLogger(__name__)


def some_function(parameters_dict):
    # function code
    #     levels['info','debug','critical',etc (same as logging module levels)]
    #     trace - include python trace
    #     exit - exit gracefully if program shouldn't proceed ahead if a critical error is logged
    #     extras - key value dict with other parameters to be logged
    log_line(logger,level='info',msg='The actual Log Message',trace=False,exit=True, extras=parameters_dict):
    # more function code
    # blah
    
```

