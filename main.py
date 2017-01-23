from connect_and_query import ConnectAndQuery
from create_object import CreateObject
from create_wordcloud import CreateWordCloud


def main():
    input_num = 1

    # Create instance
    query = ConnectAndQuery()

    while input_num != "0":
        print("\n- - - Menu - - -")
        print("1. Company by color")
        print("2. Project name by budget")
        print("3. Bigger than average")
        print("4. Name and status by color")
        print("0. Exit")
        input_num = input("Choose a number: ")

        # ----> Get the company, with count of the project, and a random color from the projects <----
        if input_num == "1":
            # First call the query class's method - that method we need, it gives back a list,
            # then create the
            company_by_color = query.company_w_rand_color()
            converted_data1 = CreateObject(company_by_color)

            converted_data1.create_object()
            # Create the word cloud
            word_cloud = CreateWordCloud(data=converted_data1.object_list, width=900, height=900,
                                         background="#e8f2b3", text_style="Sylfaen.ttf",
                                         output_name="company_name_by_project.png")
            word_cloud.create_word_cloud()

        # ----> Get the project name, order by budget (change the currency to euro) <----
        elif input_num == "2":
            project_n_by_budget_ls = query.project_name_by_budget()
#            converted_data_2 = CreateObject(project_n_by_budget_ls)
            converted_data2 = CreateObject(project_n_by_budget_ls)
            converted_data2.create_object()

            word_cloud = CreateWordCloud(data=converted_data2.object_list, width=1200, height=1200,
                                         background="white", text_style="Sylfaen.ttf",
                                         output_name="project_name_by_budget.png")
            word_cloud.create_word_cloud()

        # ----> Get that projects, which has bigger budget than the average <----
        elif input_num == "3":
            # It works
            bigger_than_average_ls = query.bigger_than_average()
            converted_data3 = CreateObject(bigger_than_average_ls)
            converted_data3.create_object()

            word_cloud = CreateWordCloud(data=converted_data3.object_list, width=900, height=900,
                                         background="black", text_style="Capture_it.ttf",
                                         output_name="bigger_than_average.png")
            word_cloud.create_word_cloud()

        # ----> Get the name and status with different color <----
        elif input_num == "4":
            # It works too
            name_and_status_ls = query.get_name_and_status()
            converted_data4 = CreateObject(name_and_status_ls)
            converted_data4.create_object()

            word_cloud = CreateWordCloud(data=converted_data4.object_list, width=900, height=900,
                                         background_picture="images/neutral.jpg",
                                         output_name="name_status_by_color.png")
            word_cloud.create_word_cloud()

        elif input_num == "0":
            break

        else:
            continue

if __name__ == "__main__":
    main()
