# syntax=docker/dockerfile:1

# https://docs.docker.com/language/python/build-images/

# tells Docker what base image to use for the ap
# this is the official python image rather than creating own base image
FROM python:3.8-slim-buster

# create a working dir, Docker should use this path as default location for subsequent commands
# can use relative file paths based on the wd instead of full file paths

WORKDIR /app

# normal to pip3 install things, need requirements.txt into the image. Use COPY to do this

COPY requirements.txt requirements.txt
#takes two param, what file like to copy in, where to copy to
# copy the file into the working dir

# can use RUN, same as running locally on a machine, pip installs modules into the image
RUN pip3 install -r requirements.txt
# now we have an image based on python3.8, and installed dependencies
# next lets add in code
#---


# take all files in the current dir, copy into the image
COPY . .

# tell docker what cmd to run when image is executed inside a container
CMD ["python3", "-m" , "flask", "run", "--port", "8000", "--host=0.0.0.0"]
# specifying the host makes the app externally visible