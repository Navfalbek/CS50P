file_name = str(input("Enter a file name: "))

if file_name.__contains__("jpg") or file_name.__contains__("jpeg"):
    print("image/jpeg")
elif file_name.__contains__("gif"):
    print("image/gif")
elif file_name.__contains__("png"):
    print("image/png")
elif file_name.__contains__("PDF") or file_name.__contains__("pdf"):
    print("application/pdf")
elif file_name.__contains__("zip"):
    print("application/zip")
elif file_name.__contains__("plain"):
    print("text/plain")
else:
    print("application/octet-stream")
