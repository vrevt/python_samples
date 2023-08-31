import logging
import requests


logging.basicConfig(level='DEBUG', filename='log')
logger = logging.getLogger()
print(logger)

for key in logging.Logger.manager.loggerDict:
    print(key)

logging.getLogger('urllib3').setLevel('CRITICAL')


logger.setLevel('DEBUG')  # logging.DEBUG

print(logger.level)


def main(name):
    logger.debug(f'func: {name}')

    r = requests.get('https://www.google.ru')


if __name__ == '__main__':
    main('Ivan')
