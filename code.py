import requests
import urllib3
import os
import sys

args = sys.argv

for i in range(0,3):
    args.append(None)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def is_url_image(image_url):
   image_formats = ("image/png", "image/jpeg", "image/jpg")
   r = requests.head(image_url,verify=False)
   if r.headers["content-type"] in image_formats:
      return True
   return False

def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)


lib = open("lib.dat","r")

segs = lib.readlines()

specification = args[1]
inbound = args[2]
outbound = args[3]

first = False

if (inbound == None):
    inbound = 1
else:
    inbound = int(inbound)
    first = True
if (outbound == None):
    outbound = 20000
    if (first):
        outbound = inbound+1
else:
    outbound = int(outbound)+1


for seg in segs:

    seg = seg.rstrip("\n")

    if (specification != None):
        if (specification != seg):
            continue

    make_dir(seg)

    url = "https://content0.fwwgo.com/"

    for sub_folder in range(inbound,outbound):

        folder_url = "/{}/{:04d}/".format(seg,sub_folder)
        status_code = int(requests.get(url+folder_url,verify=False).status_code)

        if (status_code == 404):
            print(seg + " Done.")
            break

        for image in range(0,100):
            image_url = "/{}/{:04d}/{:02d}.jpg".format(seg,sub_folder,image)
            print(url+image_url)
            if (not is_url_image(url+image_url)):
                break
            else:
                response = requests.get(url+image_url,verify=False)

                make_dir("{}/{:04d}".format(seg,sub_folder))

                file = open("{}/{:04d}/{:02d}.jpg".format(seg,sub_folder,image),"wb")

                file.write(response.content)

                file.close()
