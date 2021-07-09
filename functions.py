

def get_navbar_titles(name, status):
    nav_bar_titles = [
        {
            'name': 'Home',
            'link': '/',
            'status': ''
        },
        {
            'name': 'About',
            'link': '/about',
            'status': ''
        },
        {
            'name': 'Analysis',
            'link': '/analysis',
            'status': 'disabled'
        },
    ]
    for i in nav_bar_titles:
        if i['name'] == name:
            i['status'] = status
            break
    nav_bar_titles[2]['status'] = 'disabled'
    return nav_bar_titles









