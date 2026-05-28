import webbrowser, time
url = input("Enter the URL to open: ")
duration = (input("Enter the duration in seconds to keep the browser open: "))
for i in range(int(duration)):
    webbrowser.open(url)
    time.sleep(int(duration))