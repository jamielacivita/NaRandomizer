import requests
from lxml import etree
import random
import os
import pickle


def pickle_api_dict():
    """
    A utility function to pickle api_dict.  Used only for inital setup and not during program execution.
    :return:
    """
    with open("api_dict", "wb") as f:
        pickle.dump(api_dict, f)
    f.close()


def decrypt_api_dict():
    """
    A utility function to decrypt api_dict.gpg which holds api sensitive information in the repo.
    :return: saves a plaintext pickle file (api_dict) into the project directory.
    """
    debug = False
    if not os.path.isfile("api_dict"):
        if debug:
            print("api_dict does not exist.  Decrypting")
        os.system("gpg --batch --passphrase t3g7i -d api_dict.gpg > api_dict")
    else:
        if debug:
            print("api_dict exists.")


def load_api_dict():
    """
    api_dict is a pickle file of a dictionary which holds api sensitive information.
    api_dict is not added to the repo but an encrypted version, api_dict.gpg is.
    This function deserailzes the plaintext version.
    :return: sets api_dict as a global (i.e. module scope) variable so it can be referenced by other functions
    """
    with open("api_dict", "rb") as f:
        global api_dict
        api_dict = pickle.load(f)
    f.close()


def parse_na_lst():
    """
    Expects a file, na_list.xml which is the data returned from the api call to fetch na_list from RTM.
    :return: a list of task names
    """
    tasks = []
    tree = etree.parse("na_list.xml")
    root = tree.getroot()
    tasks_lst = root.findall("tasks")
    list_lst = tasks_lst[0].findall("list")
    for rtm_list in list_lst:
        taskseries_lst = rtm_list.findall("taskseries")
        for task in taskseries_lst:
            tasks.append(task.attrib["name"])
    return tasks


def get_random_task(tasks_lst):
    """
    Wrapper for random.choice.
    :param tasks_lst:
    :return: a task
    """
    return random.choice(tasks_lst)


def fetch_na_list():
    """
    :return: Write a file, "na_list.xml" with the results of the data call to Remember the Milk.
    """
    url = api_dict["url"]
    payload = ""
    headers = {
        'X-API-Key': api_dict["api_key"],
        'Content-Type': 'application/json',
        'Content-Length': '0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    with open("na_list.xml", "w") as f:
        f.writelines(response.text)
    f.close()


def delete_na_list():
    """
    Clean up the temporary na_list.xml file from the system.
    :return: None.
    """
    os.remove("na_list.xml")


# note : this code runs on module load to set the module scope dictionary api_dict.
# this dictionary contains api sensitive information and is not to be loaded as plain text to the repo.
global api_dict
decrypt_api_dict()
load_api_dict()
