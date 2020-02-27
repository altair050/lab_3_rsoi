import requests
from flask_restful import current_app
from base64 import b64encode


class ServiceConnector(object):
    """
    Base class to connect with other services
    """

    def __init__(self, base_url, service_name=''):
        self.base_url = base_url
        self.service_name = service_name

    def send_get_request(self, url):
        """
        Send get request to url param
        :param url: second part of destination url
        :return: (response code, response data in json)
        """
        try:
            print([self.base_url, url])
            r = requests.get(self.base_url + url)
            print(self.base_url + url+"______________________")
            # r = requests.get(self.base_url + url, headers=headers)
        except requests.exceptions.ConnectionError:
            return 503, {'message': f'Service {self.service_name} is not available'}

        code = r.status_code
        data = r.json()

        return code, data

    def send_post_request(self, url, body):
        """
        Send post request to url param
        :param url: second part of destination url
        :param body: request body in json
        :return: (response code, response data in json)
        """

        try:
            r = requests.post(self.base_url + url, json=body)
        except requests.exceptions.ConnectionError:
            return 503, {'message': f'Service {self.service_name} is not available'}

        code = r.status_code
        data = r.json()

        return code, data

    def send_delete_request(self, url, with_token=False):
        """
        Send delete request to url param
        :param url: second part of destination url
        :param with_token: send request with access token or not
        :return: (response code, response data in json)
        """

        try:
            r = requests.delete(self.base_url + url)
        except requests.exceptions.ConnectionError:
            return 503, {'message': f'Service {self.service_name} is not available'}

        code = r.status_code

        if code == 204:
            return code, {'message': 'resource deleted'}

        return code, r.json()
    
    def send_patch_request(self, url, body):
        """
        Send post request to url param
        :param url: second part of destination url
        :param body: request body in json
        :return: (response code, response data in json)
        """

        try:
            r = requests.patch(self.base_url + url, json=body)
        except requests.exceptions.ConnectionError:
            return 503, {'message': f'Service {self.service_name} is not available'}

        
        code = r.status_code
        data = r.json()

        return code, data