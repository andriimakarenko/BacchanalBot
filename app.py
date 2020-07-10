#!/usr/bin/env python3
#####################################################################
#     ____       ____  _________    ____  ____  __________________  #
#    / __ \_  __/ __ \/ ____/   |  / __ \/ __ )/ ____/ ____/ ____/  #
#   / / / / |/_/ / / / __/ / /| | / / / / __  / __/ / __/ / /       #
#  / /_/ />  </ /_/ / /___/ ___ |/ /_/ / /_/ / /___/ /___/ __/      #
#  \____/_/|_/_____/_____/_/  |_/_____/_____/_____/_____/_/         #
#                                                                   #
#####################################################################

import json
from bacchanalbot.bot import Bot
from flask import Flask, request, render_template
app = Flask(__name__)
bot = Bot()


@app.route('/', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        return render_template('settings.html')

    if request.method == 'POST':
        req_data = request.get_json(force=True)
        bot.handleMessage(req_data['message'])
        return 'OK'

@app.route('/triggers', methods=['GET', 'POST'])
def manageTriggers():
    if request.method == 'GET':
        return bot.getTriggers()
    
    if request.method == 'POST':
        req_data = request.get_json(force=True)
        if bot.setTriggers(req_data):
            return 'OK'
        else:
            return 'FAIL'

if __name__ == "__main__":
    app.run()
