import requests
import time
import threading


if __name__ == "__main__":
    url_list = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
        "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
        "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
        "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
    ]

    def calculate_time(func):
        def inner1(*args, **kwargs):
            begin = time.time()
            func(*args, **kwargs)
            end = time.time()
            print(f"The running time {end - begin}")

        return inner1


@calculate_time
def get_url(url: list):
    img_num = 1
    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                with open(f"image{img_num}.jpg", "wb") as f:
                    f.write(response.content)
                    img_num +=1
        except:
                print(f"it was error in {url}")       
                   


x1 = threading.Thread(target=get_url, args=get_url(url_list[0],))
x2 = threading.Thread(target=get_url, args=get_url(url_list[1],))
x3 = threading.Thread(target=get_url, args=get_url(url_list[2],))
x4 = threading.Thread(target=get_url, args=get_url(url_list[3],))

x1.start()
x2.start()
x3.start()
x4.start()

x1.join()
x2.join()
x3.join()
x4.join()

get_url(url_list)
