FROM quay.io/azavea/raster-vision:pytorch-0.13

RUN useradd -ms /bin/bash hitl-user
USER hitl-user


COPY requirements.txt /tmp/

RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /opt/src

ENV PYTHONPATH=/opt/src:/opt/lib:$PYTHONPATH

COPY hitl /opt/src/hitl

COPY entrypoints/hitl-job.sh /opt/src/hitl-job.sh

ENTRYPOINT [ "/opt/src/entrypoints/hitl-job.sh" ]
