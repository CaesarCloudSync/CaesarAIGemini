# Use the official Python 3.9 image
FROM python:3.10
RUN export PYTHONPATH=$PWD
RUN apt-get update && apt-get install uvicorn -y
RUN pip install uvicorn
RUN pip install pillow
RUN pip install -q -U google-generativeai
RUN pip install pandas
# Set the working directory to /code
WORKDIR /code
#VOLUME /home/amari/Desktop/MaturityAI/MaturityFastAPI /code
# Copy the current directory contents into the container at /code
COPY ./requirements.txt /code/requirements.txt
 
# Install requirements.txt 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app
EXPOSE 8080
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860","--reload"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080","--reload"]