
def test_get_project_list(app):

    user = app.config['webadmin']

    list = app.soap.project_list(user['username'], user['password'])
    return(list)