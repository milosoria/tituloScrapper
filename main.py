from webScrapper import WebScrapper
from sys import stdout

if __name__ == "__main__":
    with open("cursos_titulo.txt","r") as f:
        courses = dict(map(lambda x: x.split(" ",1),f.readlines()))
        f.close() 
    _WebScrapper = WebScrapper("https://buscacursos.uc.cl/")
    _WebScrapper.load_page()
    with open("courses_list_curated.txt","w") as f:
        courses_copy = courses.copy()
        for course in courses_copy.keys():
            _WebScrapper.send_input(course)
            _WebScrapper.submit()
            # xD
            if not _WebScrapper.check_existance("bordeBonito"):
                courses.pop(course)
            else:
                stdout.write("Writing course\n")
                f.write(f"{course}: {courses[course]}\n")
                
        _WebScrapper.finish()
        stdout.write("New file was created\n")
