import json


def log_line(logger,level='debug',msg='',trace=False,exit=True, extras={}):
    if extras:
        if msg != '':
            msg = msg + '",'+ json.dumps(extras)[1:-1]
        else:
            msg = json.dumps(extras)[1:-1]
    if level=='critical':
        logger.critical(msg,exc_info=trace)
        if exit:
            raise SystemExit(0)
    if level=='error':
        logger.error(msg,exc_info=trace)
        if exit:
            raise SystemExit(0)
    if level=='warning':
        logger.warning(msg,exc_info=trace)
    if level=='info':
        logger.info(msg,exc_info=trace)
    if level=='debug':
        logger.debug(msg,exc_info=trace)




