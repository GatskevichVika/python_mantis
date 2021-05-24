# -*- coding: utf-8 -*-
from model.project import Project


def test_add_project(app):

    app.project.open_main_page()
    app.session.login(username="administrator", password="root")
    app.project.open_project_management_page()
    app.project.open_project_page()
    old_list = app.soap.project_list(username="administrator", password="root")
    text = app.generator.random_string()
    app.project.create_project(Project(project_name="%s" % text,
                                       project_description="%s" % text))
    app.project.return_to_project_page()
    new_list = app.soap.project_list(username="administrator", password="root")
    assert old_list + 1 == new_list

    app.project.return_to_home_page()
    app.session.logout()






