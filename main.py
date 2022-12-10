import data


def main():
    # pull down the data from Remember the Milk.
    data.fetch_na_list()

    # parse the returned data into a python list of tasks.
    tasks = data.parse_na_lst()

    # chose and display a task from the set of tasks.
    random_task = data.get_random_task(tasks)
    print(random_task)

    # cleanup.
    data.delete_na_list()


if __name__ == "__main__":
    main()
