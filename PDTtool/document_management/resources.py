def handle_uploaded_file(f,location):
    with open(location, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return location