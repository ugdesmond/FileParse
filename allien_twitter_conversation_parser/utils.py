class Utility():


    def read_file(self):
        follow_list = []
        f = open('follows.txt')
        line = f.readline()
        while line:
            follow_list.append(line)
            line = f.readline()
        f.close()
        return follow_list
