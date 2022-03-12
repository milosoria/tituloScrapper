from webScrapper import WebScrapper
from sys import stdout
from banner import print_banner
from selenium import webdriver


if __name__ == "__main__":
    print_banner(title="Titulo Scrappper")

    with open("cursos_titulo.txt", "r") as f:
        courses = dict(map(lambda x: x.split(" ", 1), f.readlines()))
        f.close()
    _WebScrapper = WebScrapper("https://buscacursos.uc.cl/")
    _WebScrapper.load_page()
    with open("courses_list_curated.txt", "w") as f:
        courses_copy = courses.copy()
        for course in courses_copy.keys():
            _WebScrapper.send_input(course)
            _WebScrapper.submit()
            if not _WebScrapper.check_existance("bordeBonito"):
                courses.pop(course)
            else:
                stdout.write("Writing course\n")
                f.write(f"{course}: {courses[course]}")
    _WebScrapper.finish()
    stdout.write("New file was created\n")
