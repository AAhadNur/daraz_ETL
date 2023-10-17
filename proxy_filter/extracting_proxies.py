
import re


# to check if our proxies contain any unnecessary characters
def has_numeric(string):
    for char in string:
        if not char.isdigit() and char != '.' and char != ':':
            return True
    return False


def free_proxy_list():
    # Open First file
    with open('free_proxy_list_one.txt', 'r') as file:
        proxy_content_one = file.read()

    # Open Second file
    with open('free_proxy_list_two.txt', 'r') as file:
        proxy_content_two = file.read()

    proxy_list = []

    # Processing of First file
    lines_of_first_file = proxy_content_one.split('\n')
    proxy_list_of_first_file = [line.strip()
                                for line in lines_of_first_file if line.strip()]

    # Processing and Cleaning of Second file
    lines_of_second_file = proxy_content_two.split('\n')
    proxy_list_of_second_file = [line.strip()
                                 for line in lines_of_second_file if line.strip()]

    # extracting ip and port from each proxy_details
    for line in proxy_list_of_second_file:
        proxy_detail = re.findall(r'"(.*?)"', line)
        proxy_string = proxy_detail[0] + ':' + proxy_detail[7]
        if not has_numeric(proxy_string):
            proxy_list.append(proxy_string)

    proxy_list += proxy_list_of_first_file
    proxy_list.reverse()

    # Saving the cleaned proxies with port number to a seperate file
    with open('free_proxy_list.txt', "w") as file:
        file.writelines("%s\n" % string for string in proxy_list)


if __name__ == "__main__":
    free_proxy_list()
