# Match statement

browser_name = input("Enter the browser name\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Execute firefox")
    case "chrome":
        print("Execute Chrome")
    case"edge":
        print("Execute edge")
    case"safari":
        print("Execute safari")
    case _:
        print("Browser not found")
