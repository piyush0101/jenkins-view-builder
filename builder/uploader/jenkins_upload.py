import requests
from functools import partial

headers = {'Content-type': 'text/xml'}


def krb_request(request_fn, config):
    response = None
    try:
        from requests_kerberos import HTTPKerberosAuth, DISABLED
        # mutual auth disabled because
        # https://github.com/requests/requests-kerberos/issues/54
        response = request_fn(auth=HTTPKerberosAuth(
            mutual_authentication=DISABLED))
        # if something goes wrong with requests_kerberos (eg. the issue
        # linked above) an exception is not thrown but requests.post
        # returns None object
        if ((response is None) or
           (response is not None and response.status_code == 401)):
            response = request_fn(auth=(config['user'],
                                        config['password']))
    except ImportError:
        response = request_fn(auth=(config['user'],
                                    config['password']))
    return response


def post(url, payload, config):
    do_post = partial(requests.post, url,
                      data=payload,
                      headers=headers,
                      verify=False)
    response = krb_request(do_post, config)
    if response is not None and response.status_code != 200:
        print response.text


def update(config, view_name, view_xml):
        get_url = config['url'] + '/view/%s' % view_name
        create_url = config['url'] + '/createView?name=%s' % view_name
        update_url = get_url + '/config.xml'

        do_get = partial(requests.get, get_url, verify=False)
        response = krb_request(do_get, config)
        if response is not None:
            if response.status_code != 200:
                print "Creating view %s" % view_name
                post(create_url, view_xml, config)
            else:
                print "Updating view %s" % view_name
                post(update_url, view_xml, config)
