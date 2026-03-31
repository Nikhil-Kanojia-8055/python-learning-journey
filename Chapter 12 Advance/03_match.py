# It is similar to switch keyword
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 300:
            return "404"
        case 400:
            return "NOT FOUND"
        case 500:
            return "SORRY"

        case _:
           return "UNKNOWN STATUS"

print(http_status(3006))

# NACHO 