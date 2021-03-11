#!/usr/bin/python3

from zadarma import api


z_api = api.ZadarmaAPI(key='YOUR_KEY', secret='YOUR_SECRET', is_sandbox=True)


def get_balance():
    return z_api.call('/v1/info/balance/')


def get_tariff():
    return z_api.call('/v1/tariff/')


def caller_id():
    return z_api.call('/v1/sip/callerid/', {'id': '1234567', 'number': '71234567890'}, 'PUT')


def get_timezone():
    return z_api.call('/v1/info/timezone/')


def get_price():
    return z_api.call('/v1/info/price/', {'number': '71234567891', 'caller_id': '71234567890'})


def send_sms():

    body = 'An official documentation on Zadarma API is here: https://zadarma.com/en/support/api/#intro'

    numbers = '71234567891'

    params = {
        'number': numbers,
        'message': body,
        'caller_id': '71234567890'
    }

    return z_api.call('/v1/sms/send', params, 'POST')


if __name__ == '__main__':

    # get tariff information
    print(get_tariff())
    # # set callerid for your sip number
    # print(caller_id())

    # get information about coast
    print(get_price())

    # get balance information
    print(get_balance())

    # send SMS
    print(send_sms())

    # get timezone
    print(get_timezone())
