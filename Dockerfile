FROM python:3.9

ARG APP_HOME=/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ARG USERNAME=$USERNAME
#ARG USER_UID=1000
#ARG USER_GID=$USER_UID

RUN mkdir -p $APP_HOME
# install python dependencies
RUN pip install --upgrade pip
COPY ./ $APP_HOME/
RUN pip install --no-cache-dir --trusted-host pypy.org --trusted-host files.pythonhosted.org -r $APP_HOME/requirements.txt
#RUN groupadd --gid $USER_GID $USERNAME && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME
#RUN chown -R $USERNAME $APP_HOME/
#USER $USERNAME
#RUN echo "APP_HOME=$APP_HOME"
#RUN echo "USER=$USERNAME"
WORKDIR $APP_HOME

