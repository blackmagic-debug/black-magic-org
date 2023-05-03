from livereload import Server, shell
import os

if __name__ == '__main__':
    os.system('make html')
    print("To stop the server press CTRL-C...")
    server = Server()
    server.watch('*.rst', shell('make html'), delay=1)
    server.watch('*/*.rst', shell('make html'), delay=1)
    server.watch('*.md', shell('make html'), delay=1)
    server.watch('*/*.md', shell('make html'), delay=1)
    server.watch('*.py', shell('make html'), delay=1)
    server.watch('_static/*', shell('make html'), delay=1)
    server.watch('_templates/*', shell('make html'), delay=1)
    server.serve(root='_build/html')
