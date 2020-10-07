import os

pages = [
    'participants',
    'registration',
    'dates',
    'events',
    'organizers',
    'sponsors',
    'WiMIR',
    'presenter_instructions',
]

template = '''\
<!doctype html>
<meta charset="utf-8">
<title>Redirecting to https://ismir2020.org/{0}</title>
<meta http-equiv="refresh" content="0; url=https://ismir2020.org/{0}">
<link rel="canonical" href="https://ismir2020.org/{0}">\
'''

if __name__ == '__main__':
    for page in pages:
        try:
            os.mkdir(page)
        except:
            pass
        with open(f'{page}/index.html', 'w') as fd:
            fd.write(template.format(page))
