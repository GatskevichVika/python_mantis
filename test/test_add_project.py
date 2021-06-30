from model.project import Project


def test_add_project(app):

    app.session.login(username="administrator", password="root")

    old_list = app.project.count()
    text = app.generator.random_string()
    app.project.create_project(Project(name="%s" % text,
                                       description="%s" % text))
    app.project.return_to_project_page()
    new_list = app.project.count()
    assert old_list + 1 == new_list

    app.project.return_to_home_page()
    app.session.logout()
