from google_images_download import google_images_download  # importing the library


def Image_Scrape(cheese):
    response = google_images_download.googleimagesdownload()  # class instantiation

    arguments = {"keywords": cheese + " " + "cheese", "limit": 1,
                 "print_urls": True, "no_download": True}  # creating list of arguments

    # passing the arguments to the function
    paths = response.download(arguments)

    images_paths = []
    for k, v in paths[0].items():
        images_paths += v
    print(images_paths)
    return(images_paths)
