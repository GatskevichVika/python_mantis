from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.1/login_page.php")

    def open_main_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-2.25.1/my_view_page.php")

    def open_project_management_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Управление").click()

    def open_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Управление проектами").click()

    def create_project(self, project):
        wd = self.app.wd
        # init create project
        wd.find_element_by_xpath("//button[@type='submit']").click()
        # fill form
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.project_name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.project_description)
        # submit create project
        wd.find_element_by_xpath(u"//input[@value='Добавить проект']").click()

    def delete_selected_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//a[contains(text(),'New project2')])[2]").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()

    def return_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Продолжить").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text(u"Обзор").click()

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                project_name = cells[1].text
                project_description = cells[2].text

                self.project_cache.append(Project(project_name=project_name, project_description=project_description))
        return list(self.project_cache)

    def count(self):
        wd = self.app.wd
        self.open_project_page()
        return len(wd.find_elements_by_css_selector("i.fa.fa-check"))

    def delete_from_index(self, index):
        wd = self.app.wd
        #wd.find_element_by_xpath("(//a[contains(text(),'New project2')])[2]").click()
        wd.find_elements_by_css_selector("td a")[index].click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath(u"//input[@value='Удалить проект']").click()


