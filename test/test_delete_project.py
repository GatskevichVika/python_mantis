# -*- coding: utf-8 -*-
from random import randrange
from fixture.project import Project


def test_delete_project(app):
    app.project.open_main_page()
    app.session.login(username="administrator", password="root")
    app.project.open_project_management_page()
    app.project.open_project_page()

    if app.project.count() == 0:
        app.project.create_project(
            Project(project_name="test", project_description="test"))

    old_list = app.project.count()
    index = randrange(old_list)
    app.project.delete_from_index(index)
    new_list = app.project.count()
    assert old_list - 1 == new_list
    app.project.return_to_home_page()
    app.session.logout()