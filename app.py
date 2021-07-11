from flask import Flask

from common.utils.configuration_utils import create_app

app = create_app(__name__)

if __name__ == '__main__':
    app.run()
