from tag import Tag


class ObjectCreator:
    """This is the controller class. This include the connect to the database, and call the SQL class methods, then\
    create some data manipulation"""

    def __init__(self, data):
        # Append it to the new list, because the data contain tuple!!
        self.data = []
        for row in data:
            self.data.append([row[0], row[1], row[2]])

        self.object_list = []

    def create_object(self):
        self.__normalized_text_size()

        for row in self.data:
            self.object_list.append(Tag(name=row[0], color=row[1], text_size=row[2]))

    def __normalized_text_size(self):
        length = len(self.data)

        for index, row in enumerate(self.data):
            if index <= length / 4:
                self.data[index] = [row[0], row[1], 55]
            elif index <= length / 2:
                self.data[index] = [row[0], row[1], 45]
            else:
                self.data[index] = [row[0], row[1], 30]
