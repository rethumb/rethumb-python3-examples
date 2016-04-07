from urllib.request import urlopen

param_operation = "height"
param_value = 100 # New height in pixels.

image_url = "http://images.rethumb.com/image_coimbra_600x300.jpg"
image_filename = "resized-image.jpg"

response = urlopen("http://api.rethumb.com/v1/{0}/{1}/{2}".format(param_operation, param_value, image_url))
fh = open(image_filename, "wb")
fh.write(response.read())
fh.close()