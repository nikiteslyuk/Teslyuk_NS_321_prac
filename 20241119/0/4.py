class Sender:
    bl = True

    @classmethod
    def reprot(cls):
        if cls.bl:
            print("first")
        else:
            print("second")
        cls.bl = False


class Asker:
    @staticmethod
    def askall(lst):
        for elem in lst:
            elem.reprot()
