import psycopg2
import random


class ConnectAndQuery:
    """This class contains the methods of sql queries. Return with the following structure - list:
        name, color, text_size
        Every method returns the query as string."""

    def __init__(self):
        self.query = ""
        # use our connection values to establish a connection
        self.conn = psycopg2.connect("dbname='keli' user='keli' host='localhost' password='***'")
        # set autocommit option, to do every query when we call it
        self.conn.autocommit = True
        # create a psycopg2 cursor that can execute queries
        self.cursor = self.conn.cursor()

    def company_w_rand_color(self):
        company_by_color_ls = self.__company_by_color()
        company_by_rand_color = self.__choose_random_color(company_by_color_ls)

        return company_by_rand_color

    def __company_by_color(self):
        self.query = "SELECT company_name, main_color\
                      FROM project\
                      WHERE main_color IS NOT NULL;"

        # execute the query
        self.cursor.execute(self.query)
        # Fetch and print the result of the last execution
        rows = self.cursor.fetchall()

        return rows

    def __choose_random_color(self, company_list):
        data = {}

        # Create a dict, which include: company_name: color, color ...
        for index, row in enumerate(company_list):
            if row[0] not in data:
                data[row[0]] = row[1]
            else:
                data[row[0]] += "," + row[1]

        # Choose a color, from the dict, and add it to the new list
        company_w_random_color = []
        for key, value in data.items():
            current_color = value.split(",")
            company_w_random_color.append([key, random.choice(current_color), len(current_color)])

        # Sorted the list, order by the number of project
        sort_company_b_random_color = sorted(company_w_random_color, key=lambda x: x[2], reverse=True)

        return sort_company_b_random_color

    def project_name_by_budget(self):
        self.query = "CREATE OR REPLACE VIEW from_gbp AS SELECT name, ((budget_value::float) * 1.15212953) as budget, main_color, id\
                      FROM project\
                      WHERE budget_currency LIKE 'GBP'\
                      AND name || main_color is NOT NULL\
                      ORDER BY budget DESC;\
                      CREATE OR REPLACE VIEW from_usd AS SELECT name, ((budget_value::float) * 0.947404821) as budget, main_color, id\
                      FROM project\
                      WHERE budget_currency LIKE 'USD'\
                      AND name || main_color is NOT NULL\
                      ORDER BY budget DESC;\
                      CREATE OR REPLACE VIEW from_eur AS SELECT name, budget_value::float as budget, main_color, id\
                      FROM project\
                      WHERE budget_currency LIKE 'EUR'\
                      AND name || main_color is NOT NULL\
                      ORDER BY budget DESC;\
                      CREATE OR REPLACE VIEW budget_in_eur AS\
                      SELECT * FROM from_eur\
                      UNION\
                      SELECT * FROM from_usd\
                      UNION\
                      SELECT * FROM from_gbp;\
                      SELECT name, main_color, budget FROM budget_in_eur ORDER BY budget DESC;"

        # execute the query
        self.cursor.execute(self.query)
        # Fetch and print the result of the last execution
        rows = self.cursor.fetchall()

        return rows

    def bigger_than_average(self):
        self.query = "SELECT name, main_color, budget_value\
                      FROM project\
                      WHERE name IS NOT NULL AND main_color IS NOT NULL AND budget_value::float >\
                      (SELECT AVG(budget_value::float) FROM project)\
                      ORDER BY budget_value::float DESC\
                      LIMIT 30"

        # execute the query
        self.cursor.execute(self.query)
        # Fetch and print the result of the last execution
        rows = self.cursor.fetchall()

        return rows

    def get_name_and_status(self):
        self.query = "SELECT name, main_color, status\
                      FROM project\
                      WHERE name || main_color IS NOT NULL\
                      ORDER BY status DESC;"

        # execute the query
        self.cursor.execute(self.query)
        # Fetch and print the result of the last execution
        rows = self.cursor.fetchall()

        return rows
