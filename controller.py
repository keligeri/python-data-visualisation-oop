from connect_and_query import ConnectAndQuery
from object_creator import ObjectCreator
from wordcloud_creator import WordCloudCreator


class Controller:
    """This class the Controller. It means that, it first create a ConnectAndQuery instance,
       then call the necessary method (like company_w_random_color or bigger_than_average).
       After that call the ObjectCreator - create_object method, which create object from the returned list.
        Then call the create_word_cloud with the necessary parameter."""

    def __init__(self):
        self.query = ConnectAndQuery()

    def print_the_menu(self):
            print("\n- - - Menu - - -")
            print("1. Company by color")
            print("2. Project name by budget")
            print("3. Bigger than average")
            print("4. Name and status by color")
            print("0. Exit")

    def company_by_color(self):
        # ----> Get the company, with count of the project, and a random color from the projects <----
        # First call the query class's method - that method we need, it gives back a list,
        # then create the
        company_by_color = self.query.company_w_rand_color()
        converted_data1 = ObjectCreator(company_by_color)
        converted_data1.create_object()

        # Create the word cloud
        word_cloud = WordCloudCreator(data=converted_data1.object_list, background="#e8f2b3",
                                      text_style="Sylfaen.ttf", output_name="company_name_by_project.png")
        word_cloud.create_word_cloud()

    def project_name_by_budget(self):
            # ----> Get the project name, order by budget (change the currency to euro) <----
        project_n_by_budget_ls = self.query.project_name_by_budget()
        converted_data2 = ObjectCreator(project_n_by_budget_ls)
        converted_data2.create_object()

        word_cloud = WordCloudCreator(data=converted_data2.object_list, width=1200, height=1200,
                                      background="white", text_style="Sylfaen.ttf",
                                      output_name="project_name_by_budget.png")
        word_cloud.create_word_cloud()

    def bigger_than_average(self):
        # ----> Get that projects, which has bigger budget than the average <----
        bigger_than_average_ls = self.query.bigger_than_average()
        converted_data3 = ObjectCreator(bigger_than_average_ls)
        converted_data3.create_object()

        word_cloud = WordCloudCreator(data=converted_data3.object_list,
                                     background="black", text_style="Capture_it.ttf",
                                     output_name="bigger_than_average.png")
        word_cloud.create_word_cloud()

    def name_and_status(self):
            # ----> Get the name and status with different color <----
        name_and_status_ls = self.query.get_name_and_status()
        converted_data4 = ObjectCreator(name_and_status_ls)
        converted_data4.create_object()

        word_cloud = WordCloudCreator(data=converted_data4.object_list, background_picture="images/neutral.jpg",
                                      output_name="name_status_by_color.png")
        word_cloud.create_word_cloud()
